# .rst -> MD Conversion Process

- This is a one-time conversion process; it requires changing the Sphinx build system, building as markdown, replacing all the older rst files with the new markdown files, and then going through and cleaning up by hand.
- It is tedious, but the bulk of the work is cleaning vs actual conversion– and we can leverage the existing Sphinx setup.
- This relies on the [sphinx_markdown_builder](https://github.com/liran-funaro/sphinx-markdown-builder/) Sphinx plugin.

?> **Note:** It is *highly* recommended to do this work in a child branch of the repo, vs working directly in main. This will be extremely destructive.

This works in several main phases:

1. Setup – installing required systems for the automated conversion
2. Convert – running these systems to convert the .rst docs to .md
3. Initialize Docsify – set up the new system that will serve the files
4. Text Cleanup – all of the work to turn the converted docs to a final product
5. Project Cleanup – removing the legacy build system files

---

## 1. Setup

1. Install `sphinx` & `sphinx_markdown_builder` (for converting from .rst to .md):
    ```sh
    pip3 install sphinx sphinx_markdown_builder
    ```
2. Update Sphinx config to convert to Markdown
    - Navigate to `./docs/conf.py`
    - Replace all of the contents with only this: `extensions = ["sphinx_markdown_builder"]`
3. Install `docsify` (which will be used to serve the resulting .md files):
    ```sh
    npm i docsify-cli -g
    ```

---

## 2. Convert

1. Run the sphinx command to convert the docs
    ```sh
    sphinx-build -M markdown ./docs ./build
    ```
2. For simplicity, we're going to merge these files from `./build/markdown`/ straight into `./docs/`, so that all of each subfolder's .rst files sit alongside their .md files
    - If you're iffy on this / want more caution, feel free to do this later (but the rest of this doc will assume you've made this change)
3. Delete the `./build/` folder, as it won't be needed
4. Rename `./docs/index.md` to `./docs/_sidebar.md`

---

## 3. Initialize Docsify

Instead of initializing Docsify from scratch, we're going to just copy files over from the [After Effects Scripting Guide](https://github.com/docsforadobe/after-effects-scripting-guide/) and tweak those to fit.

1. Copy the following files from the above guide into this repo, overwriting if existing:
    - `./docs/.nojekyll`
    - `./docs/index.html`
    - `./docs/index.md`
    - `./.editorconfig`
    - `./.gitignore`
    - `./Conversion Process.md`
2. Update anything related to "After Effects Scripting Guide" and make it relevant for this repo
    - `./docs/index.html`
      - `<title>` tag at the top
      - `<meta>` tag at the top
      - The project name & repo url under `// THIS GUIDE ONLY`
    - `./docs/index.md`
      - Page title & text content; this can be pulled from the main project readme, to start

---

## 4. Text Cleanup

### Bulk Cleanup

#### Search & Replace Steps

1. Remove generated `<a>` links
    - Using regex, search for `<a id=".+"></a>(\n|\r)(\n|\r)` and replace with blank
2. Update notes admonitions
    - Using regex, search for `#### NOTE\n(.+)` and replace with `?> **Note:** $1`
3. Update warning admonitions
    - Using regex, search for `#### WARNING\n(.+)` and replace with `!> **Warning:** $1`
4. Update case-sensitive syntax highlighting languages
    - Using regex, search for `` ```AppleScript `` and replace with `` ```applescript ``
5. Replace nonstandard
    - Using regex, search for `“|”` and replace with `"`
    - Using regex, search for `‘|’` and replace with `'`
    - Using regex, search for `–` and replace with `-`
6. Update offset sublist settings
    - Using regex, search for`(\n|\r)  : - ` and replace with `:\n    - ` – only seems to be an issue with changelog

#### Look for lingering bulk-conversion issues

1. Search for lines starting with `  : - ` and
2. Search for rst-specific syntax such as the below, and fix them as needed
    - `.. note::`
    - `::`
    - `:ref:`
    - `.. WARNING::`

### Manual Cleanup

#### Sidebar

Reformat the `./docs/_sidebar.md` file to match the exact same list layout as the same file in the [After Effects Scripting Guide](https://github.com/docsforadobe/after-effects-scripting-guide/)

#### Links

1. Search for hyphenated cross-links and replace with plain slugs, i.e.
    - `[CharacterRange.pasteFrom()](../text/characterrange.md#characterrange-pastefrom)` to
    - `[CharacterRange.pasteFrom()](../text/characterrange.md#characterrangepastefrom)`
    - This regex search can help, but fails when the link is also a header (see changelog):
      - `(?:#)(.*?)-(.*?)(?:\))` => `#$1$2)`
2. Search for anchored links to the top-level page & replace with direct page link, i.e.
    - `[Settings object](../other/settings.md#settings)` to
    - `[Settings object](../other/settings.md)`
    - This regex search / replace can help:
      - `(.*)\.md#(\1)\)` => `$1.md)`
3. Search for empty in-page links and replace them with the proper format, i.e.
    - `[app.watchFolder()]()` to
    - `[app.watchFolder()](#appwatchfolder)`

#### Update Tables

In RST, tables didn't need to have header rows. In markdown, they do (should). This, unfortunately, means a lot of work is needed as the conversion method isn't capable of generating table headers.

?> **Note:** We're also going to use this opportunity to add in property types for arguments & parameters, making the docs friendlier to use.

- Set up table headers (see below)
- Remove any html linebreaks (`<br>`) unless explicitly required – *this is very rare, but sometimes does occur*
- Format tables

Here are the table header formats to use:

**Function parameters**

```
| Parameter | Type | Description |
| --------- | ---- | ----------- |
```

**Returned objects**

```
| Property | Type | Description |
| -------- | ---- | ----------- |
```

#### Titles

```
# Page
## Category ("Attributes", "Methods")
### Attribute/Method Name ("CharacterRange.characterEnd")
#### Info Header ("Description", "Type", "Parameters", "Returns")
```

#### Other

- Check that images are properly linked to the root `./docs/_static` folder
- Value ranges should be formatted as: `` `[0.0..10800.0]` `` (surrounded by backticks, two periods between min and max)

---

## 5. Project Cleanup

Now that we've got a full suite of .md files, we can remove some old cruft:

- `./.readthedocs.yaml`
- `./build/`
- `./docs/**/*.rst`
- `./docs/conf.py`
- `./make.bat`
- `./Makefile`
- `./requirements.txt`
