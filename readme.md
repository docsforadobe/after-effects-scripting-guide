# After Effects Scripting Guide

This repo hosts the After Effects Scripting Guide community docs.

This initially came from the Adobe After Effects CS6 Scripting Guide, and has been added to and adjusted to reflect the current state of scripting within AE.

---

## Contribution

This endeavour is primarily community-supported & run; contributors are welcome and encouraged to suggest fixes, adjustments, notes/warnings, and anything else that may help the project.

This project is written in [Markdown](https://en.wikipedia.org/wiki/Markdown), styled & served using [mkdocs](https://www.mkdocs.org/).

---

## Build HTML Locally

Before pushing to the online project (or submitting a PR), we ask that you develop & test the project locally to ensure the result is what you'd expect.

To build locally:

- Install python & pip
- From a terminal, navigate to the project directory and run the following command to install dependencies:
```sh
pip install -r requirements.txt
```
- When done, run the following command to serve the docs:
```sh
mkdocs serve
```
- Open your browser to the provided url (`http://127.0.0.1:8000`) by default to view the live-updating docs

---

## Admonitions Usage

Currently, the following [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) are in use in this project. Try to keep one piece of data per note, for easier parsing.

```
!!! note
    Notes detail version added, and/or relevant pieces of information.

!!! tip
    Tips detail version added, and/or relevant pieces of information.

!!!! warning
    Warnings convey negative behaviours, or when something won't work the way you'd expect.
```

---

## Adding undocumented attributes or methods

If you find attributes or methods that are not mentioned in this documentation, and they are not publically announced by Adobe, please add this warning to attribute/method so the user knows to use it at their own risk.

```
!!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!
```

---

## Licensing & Ownership

This project exists for educational purposes only.

All content is copyright Adobe Systems Incorporated.
