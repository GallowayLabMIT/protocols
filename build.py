import shutil
import os
import subprocess
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description="Generates HTML and PDFs from Markdown files")

def update_toc(directory):
    """
    Given a directory that contains HTML files,
    attempts to open and rewrite their ToC's to
    include links to the other documents.
    """
    for root, dirs, files in os.walk(directory):
        # Ignore subdirs
        dirs = []
        # Extract HTML soup of each HTML file
        soups = {}
        for filename in [f for f in files if
                os.path.splitext(f)[1] == '.html']:
            with open(os.path.join(directory, filename)) as raw_html:
                soups[filename] = BeautifulSoup(
                        raw_html,
                        features='html.parser')
        
        
        # Generate new a-tags for the other files in the same
        # directory
        extra_links = []
        for filename, soup in soups.items():
            a_tag = soup.find('div', id='sidebar').ul.li.a
            a_tag['href'] = filename
            extra_links.append((filename, a_tag))

        # Update the HTML in each entry, using the extra links
        # After updating the sidebar, write out the HTML
        for filename, soup in soups.items():
            sidebar_ul = soup.find('div', id='sidebar').ul
            before_link = True
            for insert_filename, link in extra_links:
                if insert_filename == filename:
                    # Skip!
                    before_link = False
                    continue

                new_tag = soup.new_tag("li");
                new_tag.append(link)

                if before_link:
                    sidebar_ul.insert(0, new_tag)
                else:
                    sidebar_ul.append(new_tag)
            
            # Add a link to the generated PDF
            pdf_link = soup.new_tag('a',
                href=os.path.splitext(filename)[0] + '.pdf')
            pdf_link.string = 'PDF version'
            soup.find('div', {'class':'main'}).append(pdf_link)

            with open(os.path.join(directory, filename), 'wb') as f:
                f.write(soup.prettify('utf-8'))
        


if __name__ == '__main__':
    # Remove the output folder if it exists and recreate it
    if os.path.isdir('output'):
        shutil.rmtree('output')
    os.mkdir('./output')
    # Copy over the js, css, and fonts folders
    shutil.copytree('pandoc-toc-sidebar/css', 'output/css')
    shutil.copytree('pandoc-toc-sidebar/fonts', 'output/fonts')
    shutil.copytree('pandoc-toc-sidebar/js', 'output/js')

    # Convert the index page
    subprocess.run(['pandoc', 'docs/index.md',
        '--template=pandoc-toc-sidebar/toc-sidebarL.html',
        '-B', 'docs/nav',
        '-o', 'output/index.html'])
    # Recursively walk, converting md files as we go
    for root, dirs, files in os.walk('docs'):
        # Make subdirectories we need
        for d in dirs:
            # Strip docs prefix, add output path
            relpath = os.path.relpath(os.path.join(root, d), 'docs')
            os.mkdir(os.path.join('output', relpath))

        # Skip the top level->we already generated it
        if root == 'docs':
            continue

        # Create the output path for this folder
        output_path = os.path.join('output',
                os.path.relpath(root, 'docs'))
        # Convert each md file, into HTML and PDF files
        for file in files:
            (filename, extension) = os.path.splitext(file)
            output_filename = os.path.join(output_path, filename + '.html')
            pdf_filename = os.path.join(output_path, filename + '.pdf')
            if extension == '.md':
                subprocess.run(['pandoc',
                    os.path.join(root, file),
                    '--template=pandoc-toc-sidebar/toc-sidebarL.html',
                    '-B', 'docs/nav', '--toc', '-o',
                    output_filename])
                subprocess.run(['pandoc',
                    os.path.join(root, file),
                    '-V', 'geometry:margin=1in', '-o',
                    pdf_filename])
        # Fixup the ToCs
        update_toc(output_path)
