import shutil
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")
parser.add_argument('--skip-latex', action='store_true')
parser.add_argument('--force-rebuild', action='store_true')

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
    # Run sphinx
    subprocess.run(['python', '-m', 'sphinx.cmd.build', '-b', 'html', 'docs', 'output/html'])
    if not args.skip_latex:
        subprocess.run(['python', '-m', 'sphinx.cmd.build', '-M', 'latexpdf', 'docs', 'output/latex'])
        shutil.copyfile('output/latex/latex/gallowaylabprotocols.pdf', 'output/html/galloway_lab_protocols.pdf')
