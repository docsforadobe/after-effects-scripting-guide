.. highlight:: javascript
.. _View:

View object
################################################

``app.activeViewer.views[0]``

**Description**

The View object represents a specific view.

----

==========
Attributes
==========

.. _View.active:

View.active
*********************************************

``app.activeViewer.views[0].active``

**Description**

When true, indicates if the viewer panel is focused, and thereby frontmost.

**Type**

Boolean; read-only.

----

.. _View.options:

View.options
*********************************************

``app.activeViewer.views[0].options``

**Description**

Options object for this View

**Type**

:ref:`ViewOptions`

----

=======
Methods
=======

.. _View.setActive:

View.setActive()
*********************************************

``app.activeViewer.views[0].setActive()``

**Description**

Moves this view panel to the front and places focus on it, making it active.
Calling this method will set the :ref:`view's active attribute <View.active>` to true.

**Parameters**

None.

**Returns**

Boolean, indicating if the view panel was made active.
