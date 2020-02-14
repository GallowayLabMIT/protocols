import shutil
import os
import subprocess

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
        '--self-contained', '--resource-path=pandoc-toc-sidebar',
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
        # Convert each md file
        for file in files:
            (filename, extension) = os.path.splitext(file)
            if extension == '.md':
                subprocess.run(['pandoc',
                    os.path.join(root, file),
                    '--template=pandoc-toc-sidebar/toc-sidebarL.html',
                    '--self-contained', '--resource-path=pandoc-toc-sidebar',
                    '-B', 'docs/nav', '--toc', '-o',
                    os.path.join(output_path, filename + '.html')])
