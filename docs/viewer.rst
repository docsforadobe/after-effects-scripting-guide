.. highlight:: javascript
.. _Viewer:

Viewer object
################################################

``app.activeViewer``

**Description**

The Viewer object represents a Composition, Layer, or Footage panel.

**Example**

This maximizes the active viewer panel, and displays its type if it contains a composition::

    var activeViewer = app.activeViewer;
    activeViewer.maximized = true;
    if (activeViewer.type == ViewerType.VIEWER_COMPOSITION)
        alert("Compositionpanelisactive.");

----

==========
Attributes
==========

.. _Viewer.active:

Viewer.active
*********************************************

``viewer.active``

**Description**

When true, indicates if the viewer panel is focused, and thereby frontmost.

**Type**

Boolean; read-only.

----

.. _Viewer.maximized:

Viewer.maximized
*********************************************

``viewer.maximized``

**Description**

When true, indicates if the viewer panel is at its maximized size.

**Type**

Boolean; read/write.

----

.. _Viewer.type:

Viewer.type
*********************************************

``viewer.type``

**Description**

The content in the viewer panel.

**Type**

A ``ViewerType`` enumerated value; read-only. One of:

-  ``ViewerType.VIEWER_COMPOSITION``
-  ``ViewerType.VIEWER_LAYER``
-  ``ViewerType.VIEWER_FOOTAGE``

----

=======
Methods
=======

.. _Viewer.setActive:

Viewer.setActive()
*********************************************

``viewer.setActive()``

**Description**

Moves the viewer panel to the front and places focus on it, making it active. Calling this method will set the :ref:`viewer’s active attribute <viewer.active>` to true.

**Parameters**

None.

**Returns**

Boolean indicating if the viewer panel was made active.
