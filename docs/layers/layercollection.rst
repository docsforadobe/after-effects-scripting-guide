.. highlight:: javascript
.. _LayerCollection:

LayerCollection object
################################################

``app.project.item(index).layers``

**Description**

The LayerCollection object represents a set of layers. The LayerCollection belonging to a :ref:`CompItem` contains all the layer objects for layers in the composition. The methods of the collection object allow you to manipulate the layer list.

    LayerCollection is a subclass of :ref:`Collection`. All methods and attributes of Collection, in addition to those listed below, are available when working with LayerCollection.

**Example**

Given that the first item in the project is a CompItem and the second item is an AVItem, this example shows the number of layers in the CompItem's layer collection, adds a new layer based on an AVItem in the project, then displays the new number of layers.

.. code:: javascript

    var firstComp = app.project.item(1);
    var layerCollection = firstComp.layers;
    alert("number of layers before is " + layerCollection.length);
    var anAVItem = app.project.item(2);
    layerCollection.add(anAVItem);
    alert("number of layers after is " + layerCollection.length);

----

=======
Methods
=======

.. _LayerCollection.add:

LayerCollection.add()
*********************

``app.project.item(index).layers.add(item[, duration])``

**Description**

Creates a new :ref:`AVLayer` containing the specified item, and adds it to this collection. The new layer honors the "Create Layers at Composition Start Time" preference. This method generates an exception if the item cannot be added as a layer to this CompItem.

**Parameters**

============  ================================================================
``item``      The AVItem object for the item to be added.
``duration``  Optional, the length of a still layer in seconds, a
              floating-point value. Used only if the item contains a piece of
              still footage. Has no effect on movies, sequences or audio. If
              supplied, sets the du r at i on value of the new layer.
              Otherwise, the duration value is set according to user
              preferences. By default, this is the same as the duration of the
              containing CompItem. To set another preferred value, choose
              Edit > Preferences > Import (Windows) or After Effects >
              Preferences > Import (Mac OS), and specify options under Still
              Footage.
============  ================================================================

**Returns**

:ref:`AVLayer`;

----

.. _LayerCollection.addBoxText:

LayerCollection.addBoxText()
*********************************************

``app.project.item(index).layers.addBoxText([width, height])``

**Description**

Creates a new paragraph (box) text layer with :ref:`TextDocument.lineOrientation` set to ``LineOrientation.HORIZONTAL`` and adds the new :ref:`TextLayer` to this collection. To create a point text layer, use the :ref:`LayerCollection.addText` method.

**Parameters**

===================  =======================================================
``[width, height]``  An Array containing the dimensions of the new text box.
===================  =======================================================

**Returns**

TextLayer object.

----

.. _LayerCollection.addCamera:

LayerCollection.addCamera()
*********************************************

``app.project.item(index).layers.addCamera(name, centerPoint)``

**Description**

Creates a new camera layer and adds the :ref:`CameraLayer` to this collection. The new layer honors the "Create Layers at Composition Start Time" preference.

**Parameters**

===============  =============================================================
``name``         A string containing the name of the new layer.
``centerPoint``  The center of the new camera, a floating-point array [x, y].
                 This is used to set the initial x and y values of the new
                 camera's Point of Interest property. The z value is set to 0.
===============  =============================================================

**Returns**

:ref:`CameraLayer`.

----

.. _LayerCollection.addLight:

LayerCollection.addLight()
*********************************************

``app.project.item(index).layers.addLight(name, centerPoint)``

**Description**

Creates a new light layer and adds the :ref:`LightLayer` to this collection. The new layer honors the "Create Layers at Composition Start Time" preference.

**Parameters**

===============  ===========================================================
``name``         A string containing the name of the new layer.
``centerPoint``  The center of the new light, a floating-point array [x, y].
===============  ===========================================================

**Returns**

:ref:`LightLayer`.

----

.. _LayerCollection.addNull:

LayerCollection.addNull()
*********************************************

``app.project.item(index).layers.addNull([duration])``

**Description**

Creates a new null layer and adds the :ref:`AVLayer` to this collection. This is the same as choosing Layer > New > Null Object.

**Parameters**

============  ================================================================
``duration``  Optional, the length of a still layer in seconds, a
              floating-point value. If supplied, sets the ``duration`` value of
              the new layer. Otherwise, the ``duration`` value is set according
              to user preferences. By default, this is the same as the duration
              of the containing CompItem. To set another preferred value,
              choose Edit > Preferences > Import (Windows) or After Effects >
              Preferences > Import (Mac OS), and specify options under Still
              Footage.
============  ================================================================

**Returns**

:ref:`AVLayer`.

----

.. _LayerCollection.addShape:

LayerCollection.addShape()
*********************************************

``app.project.item(index).layers.addShape()``

**Description**

Creates a new :ref:`ShapeLayer` for a new, empty Shape layer. Use the ShapeLayer object to add properties, such as shape, fill, stroke, and path filters. This is the same as using a shape tool in "Tool Creates Shape" mode. Tools automatically add a vector group that includes Fill and Stroke as specified in the tool options.

**Parameters**

None.

**Returns**

ShapeLayer object.

----

.. _LayerCollection.addSolid:

LayerCollection.addSolid()
*********************************************

``app.project.item(index).layers.addSolid(color, name, width, height, pixelAspect[, duration])``

**Description**

Creates a new :ref:`SolidSource`, with values set as specified; sets the new SolidSource as the ``mainSource`` value of a new :ref:`FootageItem`, and adds the FootageItem to the project. Creates a new :ref:`AVLayer`, sets the new Footage Item as its ``source``, and adds the layer to this collection.

**Parameters**

===============  =============================================================
``color``        The color of the solid, an array of three floating-point
                 values,
                 ``[R, G, B]``, in the range ``[0.0..1.0]``.
``name``         A string containing the name of the solid.
``width``        The width of the solid in pixels, an integer in the range
                 ``[4..30000]``.
``height``       The height of the solid in pixels, an integer in the range
                 ``[4..30000]``.
``pixelAspect``  The pixel aspect ratio of the solid, a floating-point value
                 in the range ``[0.01..100.0]``.
``duration``     Optional, the length of a still layer in seconds, a
                 floating-point value. If supplied, sets the ``duration``
                 value of the new layer. Otherwise, the ``duration`` value is
                 set according to user preferences. By default, this is the
                 same as the duration of the containing CompItem. To set
                 another preferred value, choose Edit > Preferences > Import
                 (Windows) or After Effects > Preferences > Import (MacOS), and
                 specify options under Still Footage.
===============  =============================================================

**Returns**

:ref:`AVLayer`.

----

.. _LayerCollection.addText:

LayerCollection.addText()
*********************************************

``app.project.item(index).layers.addText([sourceText])``

**Description**

Creates a new point text layer with :ref:`TextDocument.lineOrientation` set to ``LineOrientation.HORIZONTAL`` and adds the new :ref:`TextLayer` to this collection. To create a paragraph (box) text layer, use :ref:`LayerCollection.addBoxText`.

**Parameters**

==============  ===============================================================
``sourceText``  Optional; a string containing the source text of the new
                layer, or a :ref:`TextDocument` containing the source text of
                the new layer.
==============  ===============================================================

**Returns**

:ref:`TextLayer`.

----

.. _LayerCollection.addVerticalBoxText:

LayerCollection.addVerticalBoxText()
*********************************************

``app.project.item(index).layers.addVerticalBoxText([width, height])``

.. note::
   This functionality was added in After Effects 24.2.

**Description**

Creates a new paragraph (box) text layer with :ref:`TextDocument.lineOrientation` set to ``LineOrientation.VERTICAL_RIGHT_TO_LEFT`` and adds the new :ref:`TextLayer` to this collection. To create a point text layer, use the :ref:`LayerCollection.addText` or :ref:`LayerCollection.addVerticalText` methods.

**Parameters**

===================  =======================================================
``[width, height]``  An Array containing the dimensions of the new text box.
===================  =======================================================

**Returns**

TextLayer object.

----

.. _LayerCollection.addVerticalText:

LayerCollection.addVerticalText()
*********************************************

``app.project.item(index).layers.addVerticalText([sourceText])``

.. note::
   This functionality was added in After Effects 24.2.

**Description**

Creates a new point text layer with :ref:`TextDocument.lineOrientation` set to ``LineOrientation.VERTICAL_RIGHT_TO_LEFT`` and adds the new :ref:`TextLayer` to this collection. To create a paragraph (box) text layer, use the :ref:`LayerCollection.addBoxText` or :ref:`LayerCollection.addVerticalBoxText` methods.

**Parameters**

==============  ===============================================================
``sourceText``  Optional; a string containing the source text of the new
                layer, or a :ref:`TextDocument` containing the source text of
                the new layer.
==============  ===============================================================

**Returns**

:ref:`TextLayer`.

----

.. _LayerCollection.byName:

LayerCollection.byName()
*********************************************

``app.project.item(index).layers.byName(name)``

**Description**

Returns the first (topmost) layer found in this collection with the specified name, or null if no layer with the given name is found.

**Parameters**

========  =============================
``name``  A string containing the name.
========  =============================

**Returns**

:ref:`Layer` or null.

----

.. _LayerCollection.precompose:

LayerCollection.precompose()
*********************************************

``app.project.item(index).layers.precompose(layerIndicies, name[, moveAllAttributes])``

**Description**

Creates a new :ref:`CompItem` and moves the specified layers into its layer collection. It removes the individual layers from this collection, and adds the new CompItem to this collection.

**Parameters**

=====================  ========================================================
``layerIndices``       The position indexes of the layers to be collected. An
                       array of integers.
``name``               The name of the new CompItem object.
``moveAllAttributes``  Optional. When true (the default), retains all
                       attributes in the new composition. This is the same as
                       selecting the "Move all attributes into the new
                       composition" option in the Pre-compose dialog box. You
                       can only set this to false if there is just one index in
                       the ``layerIndices`` array. This is the same as
                       selecting the "Leave all attributes in" option in the
                       Pre-compose dialog box.
=====================  ========================================================

**Returns**

:ref:`CompItem`.
