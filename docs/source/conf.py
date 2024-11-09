# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
project = 'PISTL'
copyright = '2024, Suman Saurabh'
author = 'Suman Saurabh'
release = '2023'

import pistl

def auto_doc_module():
    """Automatically generate the .rst files for the pistl package."""
    import subprocess

    module_path = os.path.dirname(pistl.__file__)
    subprocess.call(f'sphinx-apidoc -o . {module_path}', shell=False)

auto_doc_module()

master_doc = 'index'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
]

autosummary_generate = True

autodoc_default_options = {
    'members': True,
    'private-members': True,
    'special-members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
