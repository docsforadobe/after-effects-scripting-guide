# .rst -> MD Conversion Process

- This is a one-time conversion process; it requires changing the Sphinx build system, building as markdown, replacing all the older rst files with the new markdown files, and then going through and cleaning up by hand.
- It is tedious, but the bulk of the work is cleaning vs actual conversion– and we can leverage the existing Sphinx setup.
- This relies on the [sphinx_markdown_builder](https://github.com/liran-funaro/sphinx-markdown-builder/) Sphinx plugin.

!!! tip
    It is *highly* recommended to do this work in a child branch of the repo, vs working directly in main. This will be extremely destructive.

This works in several main phases:

1. Setup – installing required systems for the automated conversion
2. Convert – running these systems to convert the .rst docs to .md
3. Initialize Mkdocs – set up the new system that will serve the files
4. Text Cleanup – all of the work to turn the converted docs to a final product
5. Project Cleanup – removing the legacy build system files
6. Deploy

---

## 1. Setup

### Setting up RST -> MD Conversion

1. Install `sphinx` & `sphinx_markdown_builder` (for converting from .rst to .md):
    ```sh
    pip install sphinx sphinx_markdown_builder
    ```
2. Update Sphinx config to convert to Markdown
    - Navigate to `./docs/conf.py`
    - Replace all of the contents with only this: `extensions = ["sphinx_markdown_builder"]`

### Setting up the new system

1. Install `mkdocs`, `mkdocs-material` (the theme), and any required plugins:
    ```sh
    pip install -r requirements.txt
    ```

### Setting up the repo for deployment

- From the repo:
  - `Settings` > `Pages` > Enable Pages
  - `Deploy from a Branch` > Choose "gh-pages"
  - For folder, choose "/ (root)"

---

## 2. Convert

1. Run the sphinx command to convert the docs
    ```sh
    sphinx-build -M markdown ./docs ./build
    ```
2. For simplicity, we're going to merge these files from `./build/markdown`/ straight into `./docs/`, so that all of each subfolder's .rst files sit alongside their .md files
   - Move all files from `./build/markdown/` into `./docs/`
3. Delete the `./build/` folder, as it won't be needed
4. Rename `./docs/index.md` to `./docs/_nav.md`
   - This is a temporary process that we'll resolve later
   - It needs to be rewritten in a different format, and moved into `./mkdocs.yml`, with this file deleted

---

## 3. Initialize Mkdocs

Instead of initializing Mkdocs from scratch, we're going to just copy files over from the [After Effects Scripting Guide](https://github.com/docsforadobe/after-effects-scripting-guide/) and tweak those to fit.

1. Copy the following files from the above guide into this repo, overwriting if existing:
    - `./docs/index.md`
    - `./.editorconfig`
    - `./.gitignore`
    - `./.mkdocs.yml`
    - `./Conversion Process.md`
2. Update anything related to "After Effects Scripting Guide" and make it relevant for this repo
    - `./.mkdocs.yml`
    - `./docs/index.md`
3. Open a terminal to the root folder, and run the below command to serve the docs
    ```sh
    mkdocs serve
    ```

---

## 4. Text Cleanup

### Bulk Cleanup

#### Search & Replace Steps


1. Remove generated `<a>` links
    - Using regex, search for `<a id=".+"></a>(\n|\r)(\n|\r)` and replace with blank
2. Update notes, warnings, tips admonitions
    - Valid admonitions [can be found here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types)
    - Using regex, search for `#### NOTE\n(.+)` and replace with `!!! note\n    $1`
    - Using regex, search for `#### WARNING\n(.+)` and replace with `!!! warning\n    $1`
    - Using regex, search for `#### TIP\n(.+)` and replace with `!!! tip\n    $1`
3. Update case-sensitive syntax highlighting languages
    - Using regex, search for `` ```AppleScript `` and replace with `` ```applescript ``
4. Replace nonstandard
    - Using regex, search for `“|”` and replace with `"`
    - Using regex, search for `‘|’` and replace with `'`
    - Using regex, search for `–` and replace with `-`
5. Update offset sublist settings
    - Using regex, search for`(\n|\r)  : - ` and replace with `:\n    - ` – only seems to be an issue with changelog

#### Look for lingering bulk-conversion issues

1. Search for lines starting with `  : - ` and
2. Search for rst-specific syntax such as the below, and fix them as needed
    - `.. note::`
    - `::`
    - `:ref:`
    - `.. WARNING::`

### Manual Cleanup

#### Sidebar / Navigation

The sidebar / navigation needs to be present inside of `./mkdocs.yml`, formatted identically to how it's presented in the [After Effects Scripting Guide](https://github.com/docsforadobe/after-effects-scripting-guide/) repo.

Earlier, we set aside `./docs/_nav.md` as a reference point. Now, use that file as the basis for how to display the nav within the `nav` section within `./mkdocs.yml`.

When finished, delete `./docs/_nav.md`.

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

!!! note
    We're also going to use this opportunity to add in property types for arguments & parameters, making the docs friendlier to use.

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

---

## Deploy

- Any commits to the main branch will rebuild the repo
