# -*- coding: utf-8 -*-

import sys
import os
#from better import better_theme_path

# -- General configuration ------------------------------------------------

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'After Effects Scripting Guide'
copyright = u'1992-2012 Adobe Systems Incorporated'
author = u'Adobe Systems Incorporated'

version = u'0.0.1'
release = u'0.0.1'

pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

#html_theme = 'better'

html_theme_options = {
    'sidebarwidth': '20rem',
    'cssfiles': ['_static/extra.css']
}


#html_theme_path = [better_theme_path]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "After Effects Scripting Guide"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Home"

# html_logo = None

# html_favicon = None

html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
    ],
}

# html_extra_path = []

# html_last_updated_fmt = ''

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['searchbox.html', 'localtoc.html', 'globaltoc.html'],
    'index': ['searchbox.html']
}

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

html_show_sphinx = True

html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

html_search_language = 'en'

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ae-scripting-guide'
