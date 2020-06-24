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
    # Run sphinx
    subprocess.run(['sphinx-build', '-b', 'html', 'docs', 'output'])
    # Recursively walk, converting md files as we go
    #for root, dirs, files in os.walk('docs'):
    #    # Make subdirectories we need
    #    for d in dirs:
    #        # Strip docs prefix, add output path
    #        relpath = os.path.relpath(os.path.join(root, d), 'docs')
    #        os.mkdir(os.path.join('output', relpath))
#
#        # Skip the top level->we already generated it
#        if root == 'docs':
#            continue
#
#        # Create the output path for this folder
#        output_path = os.path.join('output',
#                os.path.relpath(root, 'docs'))
#        # Convert each md file, into HTML and PDF files
#        for file in files:
#            (filename, extension) = os.path.splitext(file)
#            output_filename = os.path.join(output_path, filename + '.html')
#            pdf_filename = os.path.join(output_path, filename + '.pdf')
#            if extension == '.md':
#                subprocess.run(['pandoc',
#                    os.path.join(root, file),
#                    '--template=pandoc-toc-sidebar/toc-sidebarL.html',
#                    '-B', 'docs/nav', '--toc', '-o',
#                    output_filename])
#                subprocess.run(['pandoc',
#                    os.path.join(root, file),
#                    '-V', 'geometry:margin=1in', '-o',
#                    pdf_filename])
#        # Fixup the ToCs
#        update_toc(output_path)
