# After Effects Scripting Guide

This repo hosts the After Effects Scripting Guide RST docs, linked into a http://readthedocs.io system hosted at https://ae-scripting.docsforadobe.dev/

This came from the Adobe After Effects CS6 Scripting Guide, and has been added to and adjusted to reflect the current state of scripting within AE.

----

## Contribution

Contributors are welcome and encouraged to suggest fixes, adjustments, notes/warnings, and anything else that may help the project.

This project uses reStructuredText. For a reference on how to write reStructuredText check out this [quickref](http://docutils.sourceforge.net/docs/user/rst/quickref.html).

----

## Build HTML Locally

You may want to build the HTML locally before pushing, in order to ensure that the result is what you'd expect. These files aren't included in the git repo, nor are they used online; this is solely to create a local, offline version of the online docs.

- Install ``Python``
- Install ``pip``
- Navigate to the project directory and use the command ``pip install -r requirements.txt``
- Build the docs using ``make html``

----

## Admonitions Usage

Currently, the following [admonitions](http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions) are in use in this project. Try to keep one piece of data per note, for easier parsing.

	.. note::
		Notes detail version added, and/or relevant pieces of information.

	.. tip::
		Tips supply helpful suggestions on usage or behaviours.

	.. warning::
		Warnings convey negative behaviours, or when something won't work the way you'd expect.

----

## Adding undocumented attributes or methods

If you find attributes or methods that are not mentioned in this documentation, and they are not publically announced by Adobe, please add this warning to attribute/method so the user knows to use it at their own risk.

	.. warning::
	  	This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

----

To check the build status, visit [Read The Docs](https://readthedocs.org/projects/after-effects-scripting-guide/builds/).

----

## Licensing & Ownership

This project exists for educational purposes only.

All content is copyright Adobe Systems Incorporated.
