.. highlight:: javascript
.. _Layer:

Layer object
################################################

``app.project.item(index).layer(index)``

**Description**

The Layer object provides access to layers within compositions. It can be accessed from an item's layer collection either by index number or by a name string.

    Layer is the base class for :ref:`CameraLayer`, :ref:`LightLayer`, and :ref:`AVLayer`, so Layer attributes and methods are available when working with all layer types. Layers contain AE properties, in addition to their JavaScript attributes and methods. For examples of how to access properties in layers, see :ref:`PropertyBase`.

**Example**

If the first item in the project is a :ref:`CompItem <CompItem>`, this example disables the first layer in that composition and renames it. This might, for example, turn an icon off in the composition.

::

    var firstLayer = app.project.item(1).layer(1);
    firstLayer.enabled = false;
    firstLayer.name = "DisabledLayer";

----

==========
Attributes
==========

.. _Layer.active:

Layer.active
*********************************************

``app.project.item(index).layer(index).active``

**Description**

When true, the layer's video is active at the current time. For this to be true, the layer must be enabled, no other layer may be soloing unless this layer is soloed too, and the time must be between the ``inPoint``
and
``outPoint`` values of this layer. This value is never true in an audio layer; there is a separate ``audioActive`` attribute in the AVLayer object.

**Type**

Boolean; read-only.

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

.. _Layer.enabled:

Layer.enabled
*********************************************

``app.project.item(index).layer(index).enabled``

**Description**

When true, the layer is enabled; otherwise false. This corresponds to the video switch state of the layer in the Timeline panel.

**Type**

Boolean; read/write.

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

**Type**

Boolean; read-only.

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

.. _Layer.name:

Layer.name
*********************************************

``app.project.item(index).layer(index).name``

**Description**

The name of the layer. By default, this is the same as the Source name (which cannot be changed in the Layer panel), but you can set it to be different.

**Type**

String; read/write.

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

The parent of this layer; can be null. Offset values are calculated to counterbalance any transforms above this layer in the hierarchy, so that when you set the parent there is no apparent jump in the layer's transform. For example, if the new parent has a rotation of 30 degrees, the child layer is assigned a rotation of -30 degrees. To set the parent without changing the child layer's transform values, use the :ref:`setParentWithJump <layer.setParentWithJump>` method.

**Type**

Layer object or null; read/write.

----

.. _Layer.samplingQuality:

Layer.samplingQuality
*********************************************

``app.project.item(index).layer(index).samplingQuality``

.. note::
   This functionality was added in After Effects 12.0 (CC)

**Description**

Set/get layer sampling method (bicubic or bilinear)

**Type**

A ``LayerSamplingQuality`` enumerated value; read/write. One of:

-  ``LayerSamplingQuality.BICUBIC``
-  ``LayerSamplingQuality.BILINEAR``

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

Returns true if this layer will be active at the specified time. To return true, the layer must be enabled, no other layer may be soloing unless this layer is soloed too, and the time must be between the i n Poi nt and out Poi nt values of this layer.

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

Applies the specified collection of animation settings (an animation preset) to the layer. Predefined animation preset files are installed in the Presets folder, and users can create new animation presets through the user interface.

**Parameters**

==============  =======================================================
``presetName``  An ExtendScript File object for the file containing the
                animation preset.
==============  =======================================================

**Returns**

Nothing.

----

.. _Layer.copyToComp:

Layer.copyToComp()
*********************************************

``app.project.item(index).layer(index).copyToComp(intoComp)``

**Description**

Copies the layer into the specified composition. The original layer remains unchanged. Creates a new Layer object with the same values as this one, and prepends the new object to the :ref:`layercollection` in the target CompItem. Retrieve the copy using into ``Comp.layer(1)``. Copying in a layer changes the index positions of previously existing layers in the target composition. This is the same as copying and pasting a layer through the user interface.

.. note::
   As of After Effects 13.6, this method no longer causes After Effects to crash when the layer has a parent.

.. warning::
   As of After Effects 13.7 (13.6, has not been tested), if the copied layer has an effect on it and the user undoes the action, After Effects will Crash.

.. tip::
   The scripting guide says this method copies the layer to the top of the comp. It actually copies it to above the first selected layer, or to to the top, if nothing is selected. To retrieve the copy you have to check ``CompItem.selectedLayers`` for the layer with the topmost index, and use ``comp.layer( topmost_index_of_selected_layers - 1 )`` to retrieve the layer.

**Parameters**

============  ============================================
``intoComp``  The target composition, and :ref:`CompItem`.
============  ============================================

**Returns**

Nothing.

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

Sets the parent of this layer to the specified layer, without changing the transform values of the child layer. There may be an apparent jump in the rotation, translation, or scale of the child layer, as this layer's transform values are combined with those of its ancestors. If you do not want the child layer to jump, set the :ref:`parent <layer.parent>` attribute directly. In this case, an offset is calculated and set in the child layer's transform fields, to prevent the jump from occurring.

**Parameters**

=============  ========================================================
``newParent``  Optional, a layer object in the same composition. If not
               specified, it sets the parent to None.
=============  ========================================================

**Returns**

Nothing.
