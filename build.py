import shutil
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")
parser.add_argument('--skip-latex', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    # Remove the output folder if it exists and recreate it
    if os.path.isdir('output'):
        shutil.rmtree('output')
    os.mkdir('./output')
    os.mkdir('./output/latex')
    os.mkdir('./output/html')
    # Run sphinx
    python -m sphinx.cmd.build
    subprocess.run(['python3', '-m', 'sphinx.cmd.build', '-b', 'html', 'docs', 'output/html'])
    if not args.skip_latex:
        subprocess.run(['python3', '-m', 'sphinx.cmd.build', '-M', 'latexpdf', 'docs', 'output/latex'])
        shutil.copyfile('output/latex/latex/gallowaylabdocumentation.pdf', 'output/html/galloway_documentation.pdf')
