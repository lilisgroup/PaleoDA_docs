# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Paleoclimate Data Assimilation'
copyright = '2024, Sun H., Z. Zhao, and L. Lei'
author = 'Sun H., Z. Zhao, and L. Lei'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions = [
    'recommonmark',
    'sphinx_rtd_theme',
]
source_suffix = ['.rst','.md']

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']