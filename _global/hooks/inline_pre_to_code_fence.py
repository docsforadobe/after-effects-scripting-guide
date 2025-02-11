# Converts inline <pre lang="langcode">code</pre> blocks to pygments-highlighted html
# Custom hook to highlight and format <pre lang="langcode">code</br>code</pre> blocks
#
# This is used for <pre/> blocks embedded in tables, as these otherwise are skipped by pygments
#
# Note: It's possible this can be done better with Python-markdown inline patterns (https://python-markdown.github.io/reference/markdown/inlinepatterns),
#   but the below works For Now

import re
import markdown

import mkdocs
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

from pymdownx.highlight import HighlightExtension

# Get current mkdocs config
user_extensions = MkDocsConfig.markdown_extensions.__dict__.get('configdata');
highlight_config = dict()

if 'pymdownx.highlight' in user_extensions:
    highlight_config = user_extensions.get('pymdownx.highlight')

ExistingHighlighter = HighlightExtension().get_pymdownx_highlighter()(**highlight_config)

def on_page_content(html: str, page: Page, config: MkDocsConfig, files: Files, **kwargs):
    def inline_pre_to_code_fence(match):
        raw = match.group()

        ## Check for language
        lang = ''
        langmatch = re.search('lang="(.*?)"', raw)

        if langmatch:
            lang = langmatch.group(1)

        ## Remove first tag
        pre = re.sub('<pre( lang=(".+"))?>', '', raw)

        ## Strip end tag
        pre = re.sub('</pre>', '', pre)

        ## Swap html linebreaks
        pre = re.sub('<br/>', '\n', pre)

        return ExistingHighlighter.highlight(pre, lang)

    result = re.sub('<pre( lang=(".+"))?>(.+)</pre>', inline_pre_to_code_fence, html)

    return result
