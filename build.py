import shutil
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")

if __name__ == '__main__':
    # Remove the output folder if it exists and recreate it
    if os.path.isdir('output'):
        shutil.rmtree('output')
    os.mkdir('./output')
    os.mkdir('./output/latex')
    os.mkdir('./output/html')
    # Run sphinx
    subprocess.run(['sphinx-build', '-b', 'html', 'docs', 'output/html'])
    subprocess.run(['sphinx-build', '-M', 'latexpdf', 'docs', 'output/latex'])
    shutil.copyfile('output/latex/latex/gallowaylabdocumentation.pdf', 'output/html/galloway_documentation.pdf')