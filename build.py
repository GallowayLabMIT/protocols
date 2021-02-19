import shutil
import os
import subprocess
import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")
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

    if args.parallel:
        builds = []
        builds.append(subprocess.Popen(html_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        if args.latex:
            builds.append(subprocess.Popen(latex_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        for build in builds:
            stdout, stderr = build.communicate()
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'), file=sys.stderr)
    else:
        subprocess.run(html_args)
        if args.latex:
            subprocess.run(latex_args)
    if args.latex:
        shutil.copyfile('output/latex/latex/gallowaylabprotocols.pdf', 'output/html/galloway_lab_protocols.pdf')
