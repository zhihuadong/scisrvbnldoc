# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import myst_parser


project = 'BNL SciServer User Guide'
copyright = '2024, BNL SDCC Team'
author = 'BNL SDCC Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
myst_heading_anchors = 2
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']


html_theme_options = {
#    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
#    'logo_only': False,
#    'display_version': True,
    'prev_next_buttons_location': None,
#    'style_external_links': False,
    'vcs_pageview_mode': 'edit',
    'style_nav_header_background': '#343131',
#    # Toc options
#    'collapse_navigation': True,
    'sticky_navigation': True,
#    'navigation_depth': 4,
#    'includehidden': True,
    'titles_only': True
}
