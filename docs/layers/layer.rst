.. highlight:: javascript
.. _Layer:

Layer object
################################################

``app.project.item(index).layer(index)``

**Description**

The Layer object provides access to layers within compositions. It can be accessed from an item's layer collection either by index number or by a name string.

    Layer is a subclass of :ref:`PropertyGroup <PropertyGroup>`, which is a subclass of :ref:`PropertyBase <PropertyBase>`. All methods and attributes of PropertyGroup, in addition to those listed below, are available when working with Layer, with the exception that ``propertyIndex`` attribute is set to ``undefined``.

    Layer is the base class for :ref:`CameraLayer`, :ref:`LightLayer`, and :ref:`AVLayer`, so Layer attributes and methods are available when working with all layer types. Layers contain AE properties, in addition to their JavaScript attributes and methods. For examples of how to access properties in layers, see :ref:`PropertyBase`.

**Example**

If the first item in the project is a :ref:`CompItem <CompItem>`, this example disables the first layer in that composition and renames it. This might, for example, turn an icon off in the composition.

.. code:: javascript

    var firstLayer = app.project.item(1).layer(1);
    firstLayer.enabled = false;
    firstLayer.name = "DisabledLayer";

----

==========
Attributes
==========

.. _Layer.autoOrient:

Layer.autoOrient
*********************************************

``app.project.item(index).layer(index).autoOrient``

**Description**

The type of automatic orientation to perform for the layer.

**Type**

An ``AutoOrientType`` enumerated value; read/write. One of:

-  ``AutoOrientType.ALONG_PATH`` Layer faces in the direction of the motion path.
-  ``AutoOrientType.CAMERA_OR_POINT_OF_INTEREST`` Layer always faces the active camera or points at its point of interest.
-  ``AutoOrientType.CHARACTERS_TOWARD_CAMERA`` Each character in a per-character 3D text layer automatically faces the active camera.
-  ``AutoOrientType.NO_AUTO_ORIENT`` Layer rotates freely, independent of any motion path, point of interest, or other layers.

----

.. _Layer.comment:

Layer.comment
*************

``app.project.item(index).layer(index).comment``

**Description**

A descriptive comment for the layer.

**Type**

String; read/write.

----

.. _Layer.containingComp:

Layer.containingComp
*********************************************

``app.project.item(index).layer(index).containingComp``

**Description**

The composition that contains this layer.

**Type**

CompItem object; read-only.

----

.. _Layer.hasVideo:

Layer.hasVideo
*********************************************

``app.project.item(index).layer(index).hasVideo``

**Description**

When true, the layer has a video switch (the eyeball icon) in the Timeline panel; otherwise false.

**Type**

Boolean; read-only.

----

.. _Layer.id:

Layer.id
*********************************************

``app.project.item(index).layer(index).id``

.. note::
   This functionality was added in After Effects 22.0 (2022)

**Description**

Instance property on Layer which returns a unique and persistent identification number used internally to identify a Layer between sessions.
The value of the ID remains the same when the project is saved to a file and later reloaded.
However, when you import this project into another project, new IDs are assigned to all Layers in the imported project.
The ID is not displayed anywhere in the user interface..

**Type**

Integer; read-only.

----

.. _Layer.index:

Layer.index
*********************************************

``app.project.item(index).layer(index).index``

**Description**

The index position of the layer.

**Type**

Integer in the range ``[1..numLayers]``; read-only.

----

.. _Layer.inPoint:

Layer.inPoint
*********************************************

``app.project.item(index).layer(index).inPoint``

**Description**

The "in" point of the layer, expressed in composition time (seconds).

**Type**

Floating-point value in the range ``[-10800.0..10800.0]`` (minus or plus three hours); read/write.

----

.. _Layer.isNameSet:

Layer.isNameSet
*********************************************

``app.project.item(index).layer(index).isNameSet``

**Description**

True if the value of the name attribute has been set explicitly, rather than automatically from the source.

.. note::
   This always returns `true` for layers that do not have a :ref:`AVLayer.source`

**Type**

Boolean; read-only.

----

.. _Layer.label:

Layer.label
*********************************************

``app.project.item(index).layer(index).label``

**Description**

The label color for the item. Colors are represented by their number (0 for None, or 1 to 16 for one of the preset colors in the Labels preferences).

.. note::
   Custom label colors cannot be set programmatically.

**Type**

Integer (0 to 16); read/write.

----

.. _Layer.locked:

Layer.locked
*********************************************

``app.project.item(index).layer(index).locked``

**Description**

When true, the layer is locked; otherwise false. This corresponds to the lock toggle in the Layer panel.

**Type**

Boolean; read/write.

----

.. _Layer.marker:

Layer.marker
*********************************************

``app.project.item(index).layer(index).marker``

**Description**

A :ref:`PropertyGroup` that contains all a layer's markers. Layer marker scripting has the same functionality as :ref:`Comp markers <CompItem.markerProperty>`.

See :ref:`MarkerValue`.

**Type**

PropertyGroup object or null; read-only.

**Example**

The following sample code creates two layer markers with different properties

.. code:: javascript

    var solidLayer = comp.layers.addSolid([1, 1, 1], "mylayer", 1920, 1080, 1.0);

    var layerMarker = new MarkerValue("This is a layer marker!");
    layerMarker.duration = 1;

    var layerMarker2 = new MarkerValue("Another comp marker!");
    layerMarker2.duration = 1;

    solidLayer.marker.setValueAtTime(1, layerMarker);
    solidLayer.marker.setValueAtTime(3, layerMarker2);

----

.. _Layer.nullLayer:

Layer.nullLayer
*********************************************

``app.project.item(index).layer(index).nullLayer``

**Description**

When true, the layer was created as a null object; otherwise false.

**Type**

Boolean; read-only.

----

.. _Layer.outPoint:

Layer.outPoint
*********************************************

``app.project.item(index).layer(index).outPoint``

**Description**

The "out" point of the layer, expressed in composition time (seconds).

**Type**

Floating-point value in the range ``[-10800.0..10800.0]`` (minus or plus three hours); read/write.

----

.. _Layer.parent:

Layer.parent
*********************************************

``app.project.item(index).layer(index).parent``

**Description**

The parent of this layer; can be null.

Offset values are calculated to counterbalance any transforms above this layer in the hierarchy, so that when you set the parent there is no apparent jump in the layer's transform.

For example, if the new parent has a rotation of 30 degrees, the child layer is assigned a rotation of -30 degrees.

To set the parent without changing the child layer's transform values, use the :ref:`setParentWithJump <layer.setParentWithJump>` method.

**Type**

Layer object or null; read/write.

----

.. _Layer.selectedProperties:

Layer.selectedProperties
*********************************************

``app.project.item(index).layer(index).selectedProperties``

**Description**

An array containing all of the currently selected Property and PropertyGroup objects in the layer.

**Type**

Array of PropertyBase objects; read-only.

----

.. _Layer.shy:

Layer.shy
*********************************************

``app.project.item(index).layer(index).shy``

**Description**

When true, the layer is "shy", meaning that it is hidden in the Layer panel if the composition's "Hide all shy layers" option is toggled on.

**Type**

Boolean; read/write.

----

.. _Layer.solo:

Layer.solo
*********************************************

``app.project.item(index).layer(index).solo``

**Description**

When true, the layer is soloed, otherwise false.

**Type**

Boolean; read/write.

----

.. _Layer.startTime:

Layer.startTime
*********************************************

``app.project.item(index).layer(index).startTime``

**Description**

The start time of the layer, expressed in composition time (seconds).

**Type**

Floating-point value in the range ``[-10800.0..10800.0]`` (minus or plus three hours); read/write.

----

.. _Layer.stretch:

Layer.stretch
*********************************************

``app.project.item(index).layer(index).stretch``

**Description**

The layer's time stretch, expressed as a percentage. A value of 100 means no stretch. Values between 0 and 1 are set to 1, and values between -1 and 0 (not including 0) are set to -1.

**Type**

Floating-point value in the range ``[-9900.0..9900.0]``; read/write.

----

.. _Layer.time:

Layer.time
*********************************************

``app.project.item(index).layer(index).time``

**Description**

The current time of the layer, expressed in composition time (seconds).

**Type**

Floating-point value; read-only.

----

=======
Methods
=======

.. _Layer.activeAtTime:

Layer.activeAtTime()
*********************************************

``app.project.item(index).layer(index).activeAtTime(time)``

**Description**

Returns true if this layer will be active at the specified time.

To return ``true``, the layer must be enabled, no other layer may be soloing unless this layer is soloed too, and the time must be between the ``inPoint`` and ``outPoint`` values of this layer.

**Parameters**

========  ============================================
``time``  The time in seconds, a floating-point value.
========  ============================================

**Returns**

Boolean.

----

.. _Layer.applyPreset:

Layer.applyPreset()
*******************

``app.project.item(index).layer(index).applyPreset(presetName);``

**Description**

Applies the specified collection of animation settings (an animation preset) to all the currently selected layers of the comp to which the layer belongs. If no layer is selected, it applies the animation preset to a new solid layer.

Predefined animation preset files are installed in the Presets folder, and users can create new animation presets through the user interface.

.. warning::
   The animation preset is applied to the the selected layer(s) of the comp, not to the layer whose applyPreset function is called. Hence, the layer whose applyPreset function is called effectively just determines the comp whose layers are processed.

**Parameters**

==============  =======================================================
``presetName``  An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file containing the animation preset.
==============  =======================================================

**Returns**

Nothing.

----

.. _Layer.copyToComp:

Layer.copyToComp()
*********************************************

``app.project.item(index).layer(index).copyToComp(intoComp)``

**Description**

Copies the layer into the specified composition. The original layer remains unchanged.

Creates a new Layer object with the same values as this one, and prepends the new object to the :ref:`layercollection` in the target CompItem. Retrieve the copy using into ``Comp.layer(1)``.

Copying in a layer changes the index positions of previously existing layers in the target composition.

This is the same as copying and pasting a layer through the user interface.

.. note::
   As of After Effects 13.6, this method no longer causes After Effects to crash when the layer has a parent.

.. warning::
   As of After Effects 13.7 (13.6, has not been tested), if the copied layer has an effect on it and the user undoes the action, After Effects will Crash.

.. tip::
   The scripting guide says this method copies the layer to the top of the comp. It actually copies it to above the first selected layer, or to the top, if nothing is selected. To retrieve the copy you have to check ``CompItem.selectedLayers`` for the layer with the topmost index, and use ``comp.layer( topmost_index_of_selected_layers - 1 )`` to retrieve the layer.

**Parameters**

============  ============================================
``intoComp``  The target composition, and :ref:`CompItem`.
============  ============================================

**Returns**

Nothing.

----

.. _Layer.doSceneEditDetection:

Layer.doSceneEditDetection()
*********************************************

``app.project.item(index).layer(index).doSceneEditDetection(applyOptions)``

.. note::
   This functionality was added in After Effects 22.3 (2022)

**Description**

Runs Scene Edit Detection on the layer that the method is called on and returns an array containing the times of any detected scenes. This is the same as selecting a layer in the Timeline and choosing "Layer > Scene Edit Detection" with the single argument determining whether the edits are applied as markers, layer splits, pre-comps, or are not applied to the layer.

Just as in the UI, ``doSceneEditDetection`` will fail and error if called on a non-video layer or a video layer with Time Remapping enabled.

**Parameters**

================  =====================================================================
``applyOptions``  How the detected edits will be applied. A ``SceneEditDetectionMode``
                  enumerated value, one of:
                  
                  -  ``SceneEditDetectionMode.MARKERS``: Create markers at edit points.
                  -  ``SceneEditDetectionMode.SPLIT``: Split layer .
                  -  ``SceneEditDetectionMode.SPLIT_PRECOMP``: Split layer at edit
                     points and pre-compose each one.
                  -  ``SceneEditDetectionMode.NONE``: Detected edits are not applied
                     to the layer.
================  =====================================================================

**Returns**

Array of floating-point values; the times of the detected edit points expressed in composition time.

----

.. _Layer.duplicate:

Layer.duplicate()
*****************

``app.project.item(index).layer(index).duplicate()``

**Description**

Duplicates the layer. Creates a new Layer object in which all values are the same as in this one. This has the same effect as selecting a layer in the user interface and choosing Edit > Duplicate, except the selection in the user interface does not change when you call this method.

**Parameters**

None.

**Returns**

Layer object.

----

.. _Layer.moveAfter:

Layer.moveAfter()
*********************************************

``app.project.item(index).layer(index).moveAfter(layer)``

**Description**

Moves this layer to a position immediately after (below) the specified layer.

**Parameters**

=========  =========================================================
``layer``  The target layer, a layer object in the same composition.
=========  =========================================================

**Returns**

Nothing.

----

.. _Layer.moveBefore:

Layer.moveBefore()
*********************************************

``app.project.item(index).layer(index).moveBefore(layer)``

**Description**

Moves this layer to a position immediately before (above) the specified layer.

**Parameters**

=========  =========================================================
``layer``  The target layer, a layer object in the same composition.
=========  =========================================================

**Returns**

Nothing.

----

.. _Layer.moveToBeginning:

Layer.moveToBeginning()
*********************************************

``app.project.item(index).layer(index).moveToBeginning()``

**Description**

Moves this layer to the topmost position of the layer stack (the first layer).

**Parameters**

None.

**Returns**

Nothing.

----

.. _Layer.moveToEnd:

Layer.moveToEnd()
*********************************************

``app.project.item(index).layer(index).moveToEnd()``

**Description**

Moves this layer to the bottom position of the layer stack (the last layer).

**Parameters**

None.

**Returns**

Nothing.

----

.. _Layer.remove:

Layer.remove()
*********************************************

``app.project.item(index).layer(index).remove()``

**Description**

Deletes the specified layer from the composition.

**Parameters**

None.

**Returns**

Nothing.

----

.. _Layer.setParentWithJump:

Layer.setParentWithJump()
*********************************************

``app.project.item(index).layer(index).setParentWithJump([newParent])``

**Description**

Sets the parent of this layer to the specified layer, without changing the transform values of the child layer.

There may be an apparent jump in the rotation, translation, or scale of the child layer, as this layer's transform values are combined with those of its ancestors.

If you do not want the child layer to jump, set the :ref:`parent <layer.parent>` attribute directly. In this case, an offset is calculated and set in the child layer's transform fields, to prevent the jump from occurring.

**Parameters**

=============  ========================================================
``newParent``  Optional, a layer object in the same composition. If not
               specified, it sets the parent to None.
=============  ========================================================

**Returns**

Nothing.
