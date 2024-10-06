# Modified from https://github.com/mihaigalos/mkdocs-breadcrumbs-plugin
# Copyright (c) 2024 Mihai Galos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import mkdocs
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

DELIMITER = '<span class="breadcrumb md-nav__icon md-icon"></span>'

def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, files: Files, **kwargs):
    breadcrumbs = []
    path_parts = page.url.strip("/").split("/")
    accumulated_path = []

    ii = 0
    num_ancestors = len(page.ancestors)
    num_parts = len(path_parts)

    # If the 'sections' ancestry tree matches URL:
    # Crawl the tree, capturing URLs of each root page (if extant), else the section ID
    if num_ancestors == num_parts - 1:
        while ii < num_parts - 1:
            part = path_parts[ii]

            # Build current_url
            accumulated_path.append(part)
            current_path = "/".join(accumulated_path)
            crumb_url = f"/{current_path}/"

            # Check whether this page exists
            url_to_check = crumb_url.strip("/")
            url_file = files.get_file_from_path(url_to_check)

            # If an ancestor has a page, use that page's title & link
            if url_file is not None and url_file.page is not None:
                breadcrumbs.append(f"[{url_file.page.title}]({crumb_url})")

            # Else, if the number of parts matches section title ancestry, use that title
            else:
                ancestor = page.ancestors[num_ancestors - ii - 1]
                ancestor_title = ancestor.title
                breadcrumbs.append(ancestor_title)

            ii = ii + 1

    # If they don't match, just build static text breadcrumbs based on section headings
    else:
        for ancestor in page.ancestors:
            breadcrumbs.append(f"{ancestor.title}")

    current_page = path_parts[-1].replace('.md', '')
    if current_page:
        breadcrumbs.append(page.title)

    home_breadcrumb = "[Home](/)"
    if breadcrumbs:
        breadcrumb_str = DELIMITER.join(breadcrumbs)
        breadcrumb_str = home_breadcrumb + DELIMITER + breadcrumb_str
    else:
        breadcrumb_str = home_breadcrumb

    return breadcrumb_str + "\n" + markdown
