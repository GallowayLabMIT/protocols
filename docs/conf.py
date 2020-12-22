# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import time
sys.path.insert(0, os.path.abspath('./_ext'))

if hasattr(time, 'tzset'):
    os.environ['TZ'] = 'US/Eastern'
    time.tzset()


# -- Project information -----------------------------------------------------

project = 'Galloway Lab Protocols'
copyright = '2020, Galloway Lab. Shared under the Creative Commons 4.0 Attribution International license'
author = 'Galloway Lab'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'time_estimate',
    'sphinx_last_updated_by_git',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css'
]

# sphinx-rtd options
html_theme_options = {
    'collapse_navigation': False,
    'prev_next_buttons_location': None,
    'style_nav_header_background': '#2c6854'
}

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{charter}
        
        \newenvironment{sphinxtime}[1]{\begin{sphinxlightbox}}{\end{sphinxlightbox}}
    ''',
}

# Setup lower-left menu. Modified from:
# https://tech.michaelaltfield.net/2020/07/23/sphinx-rtd-github-pages-2/

try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

if 'REPO_NAME' in os.environ:
	REPO_NAME = os.environ['REPO_NAME']
else:
	REPO_NAME = ''

current_language = 'en'

# tell the theme which language to we're currently building
html_context['current_language'] = current_language

# SET CURRENT_VERSION
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   current_version = 'latest'

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version

# Set language links
html_context['languages'] = [ ('en', '/' +REPO_NAME+ '/en/' +current_version+ '/') ]

# Set links to other branches
html_context['versions'] = list()

#versions = [branch.name for branch in repo.branches]
versions = ['latest']
for version in versions:
   html_context['versions'].append( (version, '/' +REPO_NAME+ '/'  +current_language+ '/' +version+ '/') )

# Populate PDF Downloads

html_context['downloads'] = list()
html_context['downloads'].append( ('pdf', '/' +REPO_NAME+ '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.pdf') )