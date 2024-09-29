# After Effects Scripting Guide

This repo hosts the After Effects Scripting Guide community docs, hosted at https://ae-scripting.docsforadobe.dev/

This initially came from the Adobe After Effects CS6 Scripting Guide, and has been added to and adjusted to reflect the current state of scripting within AE.

---

## Contribution

Contributors are welcome and encouraged to suggest fixes, adjustments, notes/warnings, and anything else that may help the project.

This project is written in [Markdown](https://en.wikipedia.org/wiki/Markdown), styled & served using [Docsify](https://docsify.js.org).

---

## Build HTML Locally

Before pushing to the online project (or submitting a PR), we ask that you develop & test the project locally to ensure the result is what you'd expect.

To build locally, follow [Docsify's "Quick Start" guide](https://docsify.js.org/#/quickstart).

- Install node.js & npm
- Install docsify
- Navigate to the project directory and use the command `docsify serve ./docs`
- Open your browser to `http://localhost:3000` to view the live-updating docs

---

## Admonitions Usage

Currently, the following [callouts](https://docsify.js.org/#/helpers?id=important-content) are in use in this project. Try to keep one piece of data per note, for easier parsing.

```
?> **Note:** Notes detail version added, and/or relevant pieces of information.

?> **Tip:** Tips detail version added, and/or relevant pieces of information.

!> **Warning:** Warnings convey negative behaviours, or when something won't work the way you'd expect.
```

---

## Adding undocumented attributes or methods

If you find attributes or methods that are not mentioned in this documentation, and they are not publically announced by Adobe, please add this warning to attribute/method so the user knows to use it at their own risk.

```
!> **Warning:** This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!
```

---

## Licensing & Ownership

This project exists for educational purposes only.

All content is copyright Adobe Systems Incorporated.
