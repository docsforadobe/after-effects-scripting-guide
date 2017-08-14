**Description**

Repo hosting the AE Scripting Guide RST docs, linked into a http://readthedocs.io system hosted at http://docs.aenhancers.com

This came from the Adobe After Effects CS6 Scripting Guide, and has been added to and adjusted to reflect the current state of scripting within AE, up to AE14.2 (CC2017.2).

----

**Contribution**

Contributors are welcome and encouraged to suggest fixes, adjustments, notes/warnings, and anything else that may help the project.

----

**Build HTML Locally**

You may want to build the HTML locally before pushing, in order to ensure that the result is what you'd expect. These files aren't included in the git repo, nor are they used online; this is solely to create a local, offline version of the online docs.

- Install ``Python 2.7``
- Install ``pip``
- Navigate to the project directory and use the command ``pip install -r requirements.txt``

----

**Admonitions Usage**


Currently, the following `admonitions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions>`_ are in use in this project. Try to keep one piece of data per note, for easier parsing.

	.. note::
		Notes detail version added, and/or relevant pieces of information.

	.. tip::
		Tips supply helpful suggestions on usage or behaviours.

	.. warning::
		Warnings convey negative behaviours, or when something won't work the way you'd expect.

----

**Licensing & Ownership**

This project exists for educational purposes only.

All content is copyright Adobe Systems Incorporated.