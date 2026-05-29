import shutil
import os
import collections
import subprocess
import argparse
import sys
from pathlib import Path
import zipfile

########################
# GH annotations parser
########################
# Vendored and modified from https://github.com/ammaraskar/sphinx-action/
# Apache 2.0 license
class AnnotationLevel:
    NOTICE = "notice"
    WARNING = "warning"
    ERROR = "error"

CheckAnnotation = collections.namedtuple(
    "CheckAnnotation", ["path", "start_line", "end_line", "annotation_level", "message"]
)


def output_annotation(annotation, where_to_print=sys.stdout):
    level_to_command = {
        AnnotationLevel.WARNING: "warning",
        AnnotationLevel.ERROR: "error",
        AnnotationLevel.NOTICE: "notice",
    }

    command = level_to_command[annotation.annotation_level]

    print(
        "::{command} file={file},line={line}::{message}".format(
            command=command,
            file=annotation.path,
            line=annotation.start_line,
            message=annotation.message,
        ),
        file=where_to_print,
    )

def extract_line_information(line_information):
    r"""Lines from sphinx log files look like this

        C:\Users\ammar\workspace\sphinx-action\tests\test_projects\warnings\index.rst:22: WARNING: Problems with "include" directive path:
        InputError: [Errno 2] No such file or directory: 'I_DONT_EXIST'.

        /home/users/ammar/workspace/sphix-action/tests/test_projects/warnings/index.rst:22: WARNING: Problems with "include" directive path:
        InputError: [Errno 2] No such file or directory: 'I_DONT_EXIST'.

        /home/users/ammar/workspace/sphix-action/tests/test_projects/warnings/index.rst: Something went wrong with this whole file

    This method is responsible for parsing out the line number and file name from these lines.
    """
    file_and_line = line_information.split(":")
    # This is a dirty windows specific hack to deal with drive letters in the
    # start of the file-path, i.e D:\
    if len(file_and_line[0]) == 1:
        # If the first component is just one letter, we did an accidental split
        file_and_line[1] = file_and_line[0] + ":" + file_and_line[1]
        # Join the first component back up with the second and discard it.
        file_and_line = file_and_line[1:]

    if len(file_and_line) != 2 and len(file_and_line) != 3:
        return None
    # The case where we have no line number, in this case we return the line
    # number as 1 to mark the whole file.
    if len(file_and_line) == 2:
        line_num = 1
    if len(file_and_line) == 3:
        try:
            line_num = int(file_and_line[1])
        except ValueError:
            return None

    file_name = os.path.relpath(file_and_line[0])
    return file_name, line_num


def parse_sphinx_log(logs):
    """Parses a sphinx file containing warnings and errors into a list of
    CheckAnnotation objects.
    """
    annotations = []

    split_logs = logs.split('\n')
    for i, line in enumerate(split_logs):
        if "WARNING" not in line and "ERROR" not in line:
            continue

        is_warning = "WARNING" in line
        diagnostic_token = "WARNING" if is_warning else "ERROR"
        

        diagnostic_tokens = line.split(f"{diagnostic_token}:")
        if len(diagnostic_tokens) != 2:
            continue
        file_and_line, message = diagnostic_tokens

        file_and_line = extract_line_information(file_and_line)
        if not file_and_line:
            continue
        file_name, line_number = file_and_line

        diagnostic_message = message
        # If this isn't the last line and the next line isn't a warning,
        # treat it as part of this warning message.
        if (i != len(split_logs) - 1) and diagnostic_token not in split_logs[i + 1]:
            diagnostic_message += split_logs[i + 1]
        diagnostic_message = diagnostic_message.strip()

        annotations.append(
            CheckAnnotation(
                path=file_name,
                message=diagnostic_message,
                start_line=line_number,
                end_line=line_number,
                annotation_level=AnnotationLevel.WARNING if is_warning else AnnotationLevel.ERROR,
            )
        )

    return annotations

def summarize_latex_logfile(logs):
    p = subprocess.Popen(['texlogsieve',
                          '--no-page-delay', '--no-summary', '--no-shipouts', '--no-file-banner', '--no-heartbeat']
                         + [f'--silence-package={p}' for p in ['fancyhdr', 'textcomp', 'sphinxhighlight', 'wrapfig']]
                         + [f'--silence-string={s}' for s in ['<./', r'Underfull \hbox', r'Overfull \hbox', r'Underfull \vbox', r'Overfull \vbox', r'LaTeX Font Info', 'Float too large']]
                         , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = p.communicate(logs)
    try:
        return [CheckAnnotation(
            path='latex',
            message=stdout.decode('utf-8').replace('\n',"%0A"),
            start_line=1,
            end_line=1,
            annotation_level=AnnotationLevel.NOTICE
        )]
    except UnicodeDecodeError:
        return []

# Argparse and main

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")
parser.add_argument('--emit-gh-annotations', action='store_true')
parser.add_argument('--latex', action='store_true')
parser.add_argument('--force-rebuild', action='store_true')
parser.add_argument('--parallel', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    # Remove the output folder if it exists and we force a rebuild
    if args.force_rebuild and os.path.isdir('output'):
        shutil.rmtree('output')
    if not os.path.isdir('output'):
        os.mkdir('./output')
    if not os.path.isdir('output/latex'):
        os.mkdir('./output/latex')
    if not os.path.isdir('output/html'):
        os.mkdir('./output/html')
    # Run sphinx in parallel
    python_exe = sys.executable
    # Calculate docs path:
    docs_path = Path(__file__).resolve().parent / 'docs'
    html_path = Path(__file__).resolve().parent / 'output' / 'html'
    latex_path = Path(__file__).resolve().parent / 'output' / 'latex'
    html_args = [python_exe, '-m', 'sphinx.cmd.build', '-b', 'html', str(docs_path), str(html_path)]
    latex_args = [python_exe, '-m', 'sphinx.cmd.build','-M', 'latexpdf', str(docs_path), str(latex_path)]
    if args.parallel or args.emit_gh_annotations:
        html_args.insert(3, '--no-color')
    latex_env = os.environ.copy()
    latex_env["LATEXMKOPTS"] = "-interaction=batchmode"

    gh_annotations = []

    if args.parallel:
        builds = []
        builds.append(subprocess.Popen(html_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        if args.latex:
            builds.append(subprocess.Popen(latex_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=latex_env))
        for build, name in zip(builds, ['HTML', 'LaTeX']):
            stdout, stderr = build.communicate()
            try:
                if args.emit_gh_annotations:
                    gh_annotations.extend(parse_sphinx_log(stderr.decode('utf-8')))
                    print(f"::endgroup::") # end the group started by build_helper
                    print(f"::group::{name} build")
                print(stdout.decode('utf-8'))
                print(stderr.decode('utf-8'), file=sys.stderr)
                if args.emit_gh_annotations:
                    print("::endgroup::")
            except UnicodeDecodeError:
                pass
    else:
        if not args.emit_gh_annotations:
            subprocess.run(html_args)
            if args.latex:
                subprocess.run(latex_args, env=latex_env)
        else:
            build = subprocess.Popen(html_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = build.communicate()
            gh_annotations.extend(parse_sphinx_log(stderr.decode('utf-8')))
            try:
                print(f"::endgroup::") # end the group started by build_helper
                print("::group::HTML build")
                print(stdout.decode('utf-8'))
                print(stderr.decode('utf-8'), file=sys.stderr)
                print("::endgroup::")
            except UnicodeDecodeError:
                pass

            if args.latex:
                build = subprocess.Popen(latex_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=latex_env)
                stdout, stderr = build.communicate()
                try:
                    print("::group::LaTeX build")
                    print(stdout.decode('utf-8'))
                    print(stderr.decode('utf-8'), file=sys.stderr)
                    print("::endgroup::")
                except UnicodeDecodeError:
                    pass

    if args.emit_gh_annotations:
        if args.latex:
            # filter the output log file
            with open("output/latex/latex/gallowaylabprotocols.log", 'br') as f:
                latex_log = f.read()
                gh_annotations.extend(summarize_latex_logfile(latex_log))
        print("::group::Line-level job annotations")
        for annotation in gh_annotations:
            output_annotation(annotation)
        print("::endgroup::")

    # Zip up plot gallery data files
    with zipfile.ZipFile('output/html/_static/files/plot_gallery_data.zip', 'w') as plot_data_zip:
        for file in Path('docs/plot_gallery/data/').glob('*'):
            plot_data_zip.write(file, arcname='data/'+file.name)

    if args.latex:
        # Run ghostscript
        # You can switch to `/printer` if you want a higher quality output (less image compression)
        # see https://unix.stackexchange.com/questions/274428/how-do-i-reduce-the-size-of-a-pdf-file-that-contains-images
        subprocess.run(['gs', '-sDEVICE=pdfwrite', '-dPDFSETTINGS=/ebook', '-q', '-o', 'output/html/galloway_lab_protocols.pdf', 'output/latex/latex/gallowaylabprotocols.pdf'])
        #shutil.copyfile('output/latex/latex/gallowaylabprotocols.pdf', 'output/html/galloway_lab_protocols.pdf')
    
    if args.emit_gh_annotations:
        for annotation in gh_annotations:
            if annotation.annotation_level == AnnotationLevel.ERROR:
                sys.exit(1)
