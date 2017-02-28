.. highlight:: javascript

.. _AVlayer:

AVLayer object
################################################

``app.project.item(index).layer(index)``

**Description**

The AVLayer object provides an interface to those layers that contain AVItem objects (composition layers, footage layers, solid layers, text layers, and sound layers).

    AVLayer is a subclass of :ref:`Layer`. All methods and attributes of Layer, in addition to those listed below, are available when working with AVLayer.

    AVLayer is a base class for :ref:`TextLayer`, so AVLayer attributes and methods are available when working with TextLayer objects.

**AE Properties**

Different types of layers have different AE properties. AVLayer has the following properties and property groups:

-  Marker
-  Time Remap
-  Motion Trackers
-  Masks
-  Effects
-  Transform

   -  Anchor Point
   -  Position
   -  Scale
   -  Orientation
   -  X Rotation
   -  Y Rotation
   -  Rotation
   -  Opacity

-  Layer Styles
-  Geometry Options // Ray-traced 3D
-  Material Options

   -  Casts Shadows
   -  Light Transmission
   -  Accepts Shadows
   -  Accepts Lights
   -  Appears in Reflections // Ray-traced 3D
   -  Ambient
   -  Diffuse
   -  Specular Intensity
   -  Specular Shininess
   -  Metal
   -  Reflection Intensity // Ray-traced 3D
   -  Reflection Sharpness // Ray-traced 3D
   -  Reflection Rolloff // Ray-traced 3D
   -  Transparency // Ray-traced 3D
   -  Transparency Rolloff // Ray-traced 3D
   -  Index of Refraction // Ray-traced 3D

-  Audio

   -  AudioLevels

**Example**

If the first item in the project is a CompItem, and the first layer of that CompItem is an AVLayer, the following sets the layer ``quality``, ``startTime``, and ``inPoint``.

.. code:: javascript

    var firstLayer = app.project.item(1).layer(1);
    firstLayer.quality = LayerQuality.BEST;
    firstLayer.startTime = 1;
    firstLayer.inPoint = 2;

----

==========
Attributes
==========

.. _AVLayer.adjustmentLayer:

AVLayer.adjustmentLayer
*********************************************

``app.project.item(index).layer(index).adjustmentLayer``

**Description**

True if the layer is an adjustment layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.audioActive:

AVLayer.audioActive
*********************************************

``app.project.item(index).layer(index).audioActive``

**Description**

True if the layer's audio is active at the current time. For this value to be true, ``audioEnabled`` must be true, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the ``inPoint``
and ``outPoint`` of this layer.

**Type**

Boolean; read-only.

----

.. _AVLayer.audioEnabled:

AVLayer.audioEnabled
*********************************************

``app.project.item(index).layer(index).audioEnabled``

**Description**

When true, the layer's audio is enabled. This value corresponds to the audio toggle switch in the Timeline panel.

**Type**

Boolean; read/write.

----

.. _AVLayer.autoOrient:

AVLayer.autoOrient
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

.. _AVLayer.blendingMode:

AVLayer.blendingMode
*********************************************

``app.project.item(index).layer(index).blendingMode``

**Description**

The blending mode of the layer.

**Type**

A BlendingMode enumerated value; read/write. One of:

-  ``BlendingMode.ADD``
-  ``BlendingMode.ALPHA_ADD``
-  ``BlendingMode.CLASSIC_COLOR_BURN``
-  ``BlendingMode.CLASSIC_COLOR_DODGE``
-  ``BlendingMode.CLASSIC_DIFFERENCE``
-  ``BlendingMode.COLOR``
-  ``BlendingMode.COLOR_BURN``
-  ``BlendingMode.COLOR_DODGE``
-  ``BlendingMode.DANCING_DISSOLVE``
-  ``BlendingMode.DARKEN``
-  ``BlendingMode.DARKER_COLOR``
-  ``BlendingMode.DIFFERENCE``
-  ``BlendingMode.DISSOLVE``
-  ``BlendingMode.EXCLUSION``
-  ``BlendingMode.HARD_LIGHT``
-  ``BlendingMode.HARD_MIX``
-  ``BlendingMode.HUE``
-  ``BlendingMode.LIGHTEN``
-  ``BlendingMode.LIGHTER_COLOR``
-  ``BlendingMode.LINEAR_BURN``
-  ``BlendingMode.LINEAR_DODGE``
-  ``BlendingMode.LINEAR_LIGHT``
-  ``BlendingMode.LUMINESCENT_PREMUL``
-  ``BlendingMode.LUMINOSITY``
-  ``BlendingMode.MULTIPLY``
-  ``BlendingMode.NORMAL``
-  ``BlendingMode.OVERLAY``
-  ``BlendingMode.PIN_LIGHT``
-  ``BlendingMode.SATURATION``
-  ``BlendingMode.SCREEN``
-  ``BlendingMode.SILHOUETE_ALPHA``
-  ``BlendingMode.SILHOUETTE_LUMA``
-  ``BlendingMode.SOFT_LIGHT``
-  ``BlendingMode.STENCIL_ALPHA``
-  ``BlendingMode.STENCIL_LUMA``
-  ``BlendingMode.VIVID_LIGHT``

----

.. _AVLayer.canSetCollapseTransformation:

AVLayer.canSetCollapseTransformation
*********************************************

``app.project.item(index).layer(index).canSetCollapseTransformation``

**Description**

True if it is legal to change the value of the ``collapseTransformation`` attribute on this layer.

**Type**

Boolean; read-only.

----

.. _AVLayer.canSetTimeRemapEnabled:

AVLayer.canSetTimeRemapEnabled
*********************************************

``app.project.item(index).layer(index).canSetTimeRemapEnabled``

**Description**

True if it is legal to change the value of the ``timeRemapEnabled`` attribute on this layer.

**Type**

Boolean; read-only.

----

.. _AVLayer.collapseTransformation:

AVLayer.collapseTransformation
*********************************************

``app.project.item(index).layer(index).collapseTransformation``

**Description**

True if collapse transformation is on for this layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.effectsActive:

AVLayer.effectsActive
*********************************************

``app.project.item(index).layer(index).effectsActive``

**Description**

True if the layer's effects are active, as indicated by the ``<f>`` icon next to it in the user interface.

**Type**

Boolean; read/write.

----

.. _AVLayer.environmentLayer:

AVLayer.environmentLayer
*********************************************

``app.project.item(index).layer(index).environmentLayer``

**Description**

True if this is an environment layer in a Ray-traced 3D composition. Setting this attribute to true automaticallymakes the layer 3D (``threeDLayer`` becomes true).

**Type**

Boolean; read/write.

----

.. _AVLayer.frameBlending:

AVLayer.frameBlending
*********************************************

``app.project.item(index).layer(index).frameBlending``

**Description**

True if frame blending is enabled for the layer.

**Type**

Boolean; read-only.

----

.. _AVLayer.frameBlendingType:

AVLayer.frameBlendingType
*********************************************

``app.project.item(index).layer(index).frameBlendingType``

**Description**

The type of frame blending to perform when frame blending is enabled for the layer.

**Type**

A FrameBlendingType enumerated value; read/write. One of:

-  ``FrameBlendingType.FRAME_MIX``
-  ``FrameBlendingType.NO_FRAME_BLEND``
-  ``FrameBlendingType.PIXEL_MOTION``

----

.. _AVLayer.guideLayer:

AVLayer.guideLayer
*********************************************

``app.project.item(index).layer(index).guideLayer``

**Description**

True if the layer is a guide layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.hasAudio:

AVLayer.hasAudio
*********************************************

``app.project.item(index).layer(index).hasAudio``

**Description**

True if the layer contains an audio component, regardless of whether it is audio-enabled or soloed.

**Type**

Boolean; read-only.

----

.. _AVLayer.hasTrackMatte:

AVLayer.hasTrackMatte
*********************************************

``app.project.item(index).layer(index).hasTrackMatte``

**Description**

True if the layer in front of this layer is being used as a track matte on this layer. When true, this layer's ``trackMatteType`` value controls how the matte is applied.

**Type**

Boolean; read-only.

----

.. _AVLayer.height:

AVLayer.height
*********************************************

``app.project.item(index).layer(index).height``

**Description**

The height of the layer in pixels.

**Type**

Floating-point; read-only.

----

.. _AVLayer.isNameFromSource:

AVLayer.isNameFromSource
*********************************************

``app.project.item(index).layer(index).isNameFromSource``

**Description**

True if the layer has no expressly set name, but contains a named source. In this case, ``layer.name`` has the same value as ``layer.source.name``. False if the layer has an expressly set name, or if the layer does not have a source.

**Type**

Boolean; read-only.

----

.. _AVLayer.isTrackMatte:

AVLayer.isTrackMatte
*********************************************

``app.project.item(index)layer(index).isTrackMatte``

**Description**

True if this layer is being used as a track matte for the layer behind it.

**Type**

Boolean; read-only.

----

.. _AVLayer.motionBlur:

AVLayer.motionBlur
*********************************************

``app.project.item(index).layer(index).motionBlur``

**Description**

True if motion blur is enabled for the layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.preserveTransparency:

AVLayer.preserveTransparency
*********************************************

``app.project.item(index).layer(index).preserveTransparency``

**Description**

True if preserve transparency is enabled for the layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.quality:

AVLayer.quality
*********************************************

``app.project.item(index).layer(index).quality``

**Description**

The quality with which this layer is displayed.

**Type**

A ``LayerQuality`` enumerated value; read/write. One of:

-  ``LayerQuality.BEST``
-  ``LayerQuality.DRAFT``
-  ``LayerQuality.WIREFRAME``

----

.. _AVLayer.source:

AVLayer.source
*********************************************

``app.project.item(index).layer(index).source``

**Description**

The source AVItem for this layer. The value is null in a Text layer. Use ``AVLayer.replaceSource()`` to change the value.

**Type**

AVItem object; read-only.

----

.. _AVLayer.threeDLayer:

AVLayer.threeDLayer
*********************************************

``app.project.item(index).layer(index).threeDLayer``

**Description**

True if this is a 3D layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.threeDPerChar:

AVLayer.threeDPerChar
*********************************************

``app.project.item(index).layer(index).threeDPerChar``

**Description**

``True`` if this layer has the Enable Per-character 3D switch set, allowing its characters to be animated off the plane of the text layer. Applies only to text layers.

**Type**

Boolean; read/write.

----

.. _AVLayer.timeRemapEnabled:

AVLayer.timeRemapEnabled
*********************************************

``app.project.item(index).layer(index).timeRemapEnabled``

**Description**

True if time remapping is enabled for this layer.

**Type**

Boolean; read/write.

----

.. _AVLayer.trackMatteType:

AVLayer.trackMatteType
*********************************************

``app.project.item(index).layer(index).trackMatteType``

**Description**

If this layer has a track matte, specifies the way the track matte is applied.

**Type**

A ``TrackMatteType`` enumerated value; read/write. One of:

-  ``TrackMatteType.ALPHA``
-  ``TrackMatteType.ALPHA_INVERTED``
-  ``TrackMatteType.LUMA``
-  ``TrackMatteType.LUMA_INVERTED``
-  ``TrackMatteType.NO_TRACK_MATTE``

----

.. _AVLayer.width:

AVLayer.width
*********************************************

``app.project.item(index).layer(index).width``

**Description**

The width of the layer in pixels.

**Type**

Floating-point; read-only.

----

=======
Methods
=======

.. _AVLayer.audioActiveAtTime:

AVLayer.audioActiveAtTime()
*********************************************

``app.project.item(index).layer(index).audioActiveAtTime(time)``

**Description**

Returns true if this layer's audio will be active at the specified time. For this method to return true, ``audioEnabled`` must be true, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the ``inPoint`` and ``outPoint`` of this layer.

**Parameters**

========  =============================================
``time``  The time, in seconds. A floating-point value.
========  =============================================

**Returns**

Boolean.

----

.. _AVLayer.calculateTransformFromPoints:

AVLayer.calculateTransformFromPoints()
*********************************************

``app.project.item(index).layer(index).calculateTransformFromPoints(pointTopLeft, pointTopRight, pointBottomRight)``

**Description**

Calculates a transformation from a set of points in this layer.

**Parameters**

====================  ========================================================
``pointTopLeft``      The top left point coordinates in the form of an array,
                      [x , y, z] .
``pointTopRight``     The top right point coordinates in the form of an array,
                      [ x, y, z ] .
``pointBottomRight``  The bottom right point coordinates in the form of an
                      array, [ x, y, z ] .
====================  ========================================================

**Returns**

An Object with the transformation properties set.

**Example**

.. code:: javascript

    var newLayer = comp.layers.add(newFootage);
    newLayer.threeDLayer = true;
    newLayer.blendingMode = BlendingMode.ALPHA_ADD;
    var transform = newLayer.calculateTransformFromPoints(tl, tr, bl);
    for(var sel in transform) {
        newLayer.transform[sel].setValue(transform[sel]);
    }

----

.. _AVLayer.openInViewer:

AVLayer.openInViewer()
*********************************************

``app.project.item(index).layer(index).openInViewer()``

**Description**

Opens the layer in a Layer panel, and moves the Layer panel to front and gives it focus.

**Parameters**

None.

**Returns**

Viewer object for the Layer panel, or null if the layer could not be opened (e.g., for text or shape layers, which cannot be opened in the Layer panel).

----

.. _AVLayer.replaceSource:

AVLayer.replaceSource()
*********************************************

``app.project.item(index).layer(index).replaceSource(newSource, fixExpressions)``

**Description**

Replaces the source for this layer.

**Parameters**

==================  =========================================================
``newSource``       The new source AVItem object.
``fixExpressions``  ``True`` to adjust expressions for the new source,
                    ``false`` otherwise. Note that this feature can be
                    resource-intensive; if replacing a large amount of
                    footage, do this only at the end of the operation. See
                    also :ref:`Project.autoFixExpressions`.
==================  =========================================================

**Returns**

Nothing.

.. warning::
  If this method is performed on a null layer, the layers ``isNull`` attribute is not changed from ``true``. This causes the layer not to be visible in comp viewer and renders.

----

.. _AVLayer.sourceRectAtTime:

AVLayer.sourceRectAtTime()
*********************************************

``app.project.item(index).layer(index).sourceRectAtTime(timeT, extents)``

**Description**

Retrieves the rectangle bounds of the layer at the specified time index, corrected for text or shape layer content. Use, for example, to write text that is properly aligned to the baseline.

**Parameters**

===========  ================================================================
``timeT``    The time index, in seconds. A floating-point value.
``extents``  ``True`` to include the extents, ``false`` otherwise. Extents
             apply to shape layers, increasing the size of the layer bounds
             as necessary.
===========  ================================================================

**Returns**

A JavaScript object with four attributes, [``top``, ``left``, ``width``, ``height``].
