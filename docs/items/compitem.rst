.. highlight:: javascript
.. _CompItem:

CompItem object
################################################

|  ``app.project.item(index)``
|  ``app.project.items[index]``

**Description**

The CompItem object represents a composition, and allows you to manipulate and get information about it. Access the objects by position index number in a project's item collection.

    CompItem is a subclass of :ref:`AVItem`, which is a subclass of :ref:`Item`. All methods and attributes of AVItem and Item, in addition to those listed below, are available when working with CompItem.

**Example**

Given that the first item in the project is a CompItem, the following code displays two alerts. The first shows the number of layers in the CompItem, and the second shows the name of the last layer in the CompItem.

.. code:: javascript

    var firstComp = app.project.item(1);
    alert("number of layers is " + firstComp.numLayers);
    alert("name of last layer is " + firstComp.layer(firstComp.numLayers).name);

----

==========
Attributes
==========

.. _CompItem.activeCamera:

CompItem.activeCamera
*********************************************

``app.project.item(index).activeCamera``

**Description**

The active camera, which is the front-most camera layer that is enabled. The value is null if the composition contains no enabled camera layers.

**Type**

CameraLayer object; read-only.

----

.. _CompItem.bgColor:

CompItem.bgColor
*********************************************

``app.project.item(index).bgColor``

**Description**

The background color of the composition. The three array values specify the red, green, and blue components of the color.

**Type**

An array containing three floating-point values, ``[R, G, B]``, in the range ``[0.0..1.0]``; read/write.

----

.. _CompItem.counters:

CompItem.counters
*********************************************

``app.project.item(index).counters``

.. note::
  This functionality was added in After Effects 13.2 (CC2014).

.. warning::
  This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

**Description**

This attribute works app-wide: if changed on one CompItem, it will change it for every CompItem in the project. The value stays until restarting AE. Once restarted, it will revert to false.

This parameter doesn't do anything.

**Type**

Boolean; read/write.

----

.. _CompItem.displayStartFrame:

CompItem.displayStartFrame
*********************************************

``app.project.item(index).displayStartFrame``

**Description**

The frame value of the beginning of the composition.

This value is an alternative to calculating the start frame using :ref:`CompItem.displayStartTime` and :ref:`CompItem.frameDuration` to compensate for floating-point problems.

.. note::
   This functionality was added in After Effects 17.1.

**Type**

Integer; read/write.

----

.. _CompItem.displayStartTime:

CompItem.displayStartTime
*********************************************

``app.project.item(index).displayStartTime``

**Description**

The time set as the beginning of the composition, in seconds. This is the equivalent of the Start Timecode or Start Frame setting in the Composition Settings dialog box.

.. note::
   As of After Effects 17.1, the minimum value is ``-10800.0``. Before 17.1, the minimum value was 0.0

**Type**

Floating-point value in the range ``[-10800.0...86339.0]`` (-3:00:00:00 to 23:59:00:00); read/write.

----

.. _CompItem.draft3d:

CompItem.draft3d
*********************************************

``app.project.item(index).draft3d``

**Description**

When true, Draft 3D mode is enabled for the Composition panel. This corresponds to the value of the Draft 3D button in the Composition panel.

**Type**

Boolean; read/write.

----

.. _CompItem.dropFrame:

CompItem.dropFrame
*********************************************

``app.project.item(index).dropFrame``

**Description**

When true, indicates that the composition uses drop-frame timecode. When false, indicates non-drop-frame timecode. This corresponds to the setting in the Composition Settings dialog box.

**Type**

Boolean; read/write.

----

.. _CompItem.frameBlending:

CompItem.frameBlending
*********************************************

``app.project.item(index).frameBlending``

**Description**

When true, frame blending is enabled for this Composition. Corresponds to the value of the Frame Blending button in the Composition panel.

**Type**

Boolean; if true, frame blending is enabled; read/write.

----

.. _CompItem.frameDuration:

CompItem.frameDuration
*********************************************

``app.project.item(index).frameDuration``

**Description**

The duration of a frame, in seconds. This is the inverse of the ``frameRate`` value (frames-per-second).

**Type**

Floating-point; read/write.

----

.. _CompItem.hideShyLayers:

CompItem.hideShyLayers
*********************************************

``app.project.item(index).hideShyLayers``

**Description**

When true, only layers with shy set to false are shown in the Timeline panel. When false, all layers are visible, including those whose shy value is true. Corresponds to the value of the Hide All Shy Layers button in the Composition panel.

**Type**

Boolean; read/write.

----

.. _CompItem.layers:

CompItem.layers
*********************************************

``app.project.item(index).layers``

**Description**

A :ref:`LayerCollection` that contains all the Layer objects for layers in this composition.

**Type**

LayerCollection object; read-only.

----

.. _CompItem.markerProperty:

CompItem.markerProperty
*********************************************

``app.project.item(index).markerProperty``

.. note::
   This functionality was added in After Effects 14.0 (CC 2017)

**Description**

A :ref:`PropertyGroup` that contains all a composition's markers. Composition marker scripting has the same functionality as :ref:`Layer markers <Layer.marker>`.

See :ref:`MarkerValue`.

**Type**

PropertyGroup object or null; read-only.

**Example**

The following sample code creates a project and composition, then creates two composition markers with different properties

.. code:: javascript

    // comp.markerProperty allows you to add markers to a comp.
    // It has the same functionality as layer.property("Marker")
    var currentProj = app.newProject();
    var comp = currentProj.items.addComp("mycomp", 1920, 1080, 1.0, 5, 29.97);
    var solidLayer = comp.layers.addSolid([1, 1, 1], "mylayer", 1920, 1080, 1.0);

    var compMarker = new MarkerValue("This is a comp marker!");
    compMarker.duration = 1;

    var compMarker2 = new MarkerValue("Another comp marker!");
    compMarker2.duration = 1;

    comp.markerProperty.setValueAtTime(1, compMarker);
    comp.markerProperty.setValueAtTime(3, compMarker2);

----

.. _CompItem.motionBlur:

CompItem.motionBlur
*********************************************

``app.project.item(index).motionBlur``

**Description**

When true, motion blur is enabled for the composition. Corresponds to the value of the Motion Blur button in the Composition panel.

**Type**

Boolean; read/write.

----

.. _CompItem.motionBlurAdaptiveSampleLimit:

CompItem.motionBlurAdaptiveSampleLimit
*********************************************

``app.project.item(index).motionBlurAdaptiveSampleLimit``

**Description**

The maximum number of motion blur samples of 2D layer motion. This corresponds to the Adaptive Sample Limit setting in the Advanced tab of the Composition Settings dialog box.

**Type**

Integer (between 16 and 256); read/write.

----

.. _CompItem.motionBlurSamplesPerFrame:

CompItem.motionBlurSamplesPerFrame
*********************************************

``app.project.item(index).motionBlurSamplesPerFrame``

**Description**

The minimum number of motion blur samples per frame for Classic 3D layers, shape layers, and certain effects. This corresponds to the Samples Per Frame setting in the Advanced tab of the Composition Settings dialog box.

**Type**

Integer (between 2 and 64); read/write.

----

.. _CompItem.motionGraphicsTemplateControllerCount:

CompItem.motionGraphicsTemplateControllerCount
**********************************************

``app.project.item(index).motionGraphicsTemplateControllerCount``

.. note::
   This functionality was added in After Effects 16.1 (CC 2019)

**Description**

The number of properties in the Essential Graphics panel for the composition.

**Type**

Integer; read-only.

----

.. _CompItem.motionGraphicsTemplateName:

CompItem.motionGraphicsTemplateName
*********************************************

``app.project.item(index).motionGraphicsTemplateName``

.. note::
   This functionality was added in After Effects 15.0 (CC 2018)

**Description**

Read or write the name property in the Essential Graphics panel for the composition.

The name in the Essential Graphics panel is used for the file name of an exported Motion Graphics template (ex., "My Template.mogrt").

The following example will set the name for the active composition and then return it as an alert

.. code:: javascript

    app.project.activeItem.motionGraphicsTemplateName = "My Template";
    alert(app.project.activeItem.motionGraphicsTemplateName);

**Type**

String; read/write.

----

.. _CompItem.numLayers:

CompItem.numLayers
*********************************************

``app.project.item(index).numLayers``

**Description**

The number of layers in the composition.

**Type**

Integer; read-only.

----

.. _CompItem.preserveNestedFrameRate:

CompItem.preserveNestedFrameRate
*********************************************

``app.project.item(index).preserveNestedFrameRate``

**Description**

When true, the frame rate of nested compositions is preserved in the current composition. Corresponds to the value of the "Preserve frame rate when nested or in render queue" option in the Advanced tab of the Composition Settings dialog box.

**Type**

Boolean; read/write.

----

.. _CompItem.preserveNestedResolution:

CompItem.preserveNestedResolution
*********************************************

``app.project.item(index).preserveNestedResolution``

**Description**

When true, the resolution of nested compositions is preserved in the current composition. Corresponds to the value of the "Preserve Resolution When Nested" option in the Advanced tab of the Composition Settings dialog box.

**Type**

Boolean; read/write.

----

.. _CompItem.renderer:

CompItem.renderer
*********************************************

``app.project.item(index).renderer``

**Description**

The current rendering plug-in module to be used to render this composition, as set in the Advanced tab of the Composition Settings dialog box. Allowed values are the members of :ref:`compItem.renderers`.

**Type**

String; read/write.

----

.. _CompItem.renderers:

CompItem.renderers
*********************************************

``app.project.item(index).renderers``

**Description**

The available rendering plug-in modules. Member strings reflect installed modules, as seen in the Advanced tab of the Composition Settings dialog box.

**Type**

Array of strings; read-only.

----

.. _CompItem.resolutionFactor:

CompItem.resolutionFactor
*********************************************

``app.project.item(index).resolutionFactor``

**Description**

The x and y downsample resolution factors for rendering the composition. The two values in the array specify how many pixels to skip when sampling; the first number controls horizontal sampling, the second controls vertical sampling. Full resolution is ``[1, 1]``, half resolution is ``[2, 2]``, and quarter resolution is ``[4, 4]``. The default is ``[1, 1]``.

**Type**

Array of two integers in the range ``[1..99]``; read/write.

----

.. _CompItem.selectedLayers:

CompItem.selectedLayers
*********************************************

``app.project.item(index).selectedLayers``

**Description**

All of the selected layers in this composition. This is a 0-based array (the first object is at index 0).

**Type**

Array of :ref:`Layer <Layer>` objects; read-only.

----

.. _CompItem.selectedProperties:

CompItem.selectedProperties
*********************************************

``app.project.item(index).selectedProperties``

**Description**

All of the selected properties (Property and PropertyGroup objects) in this composition. The first property is at index position 0.

**Type**

Array of :ref:`Property <Property>` and :ref:`PropertyGroup <PropertyGroup>` objects; read-only.

----

.. _CompItem.shutterAngle:

CompItem.shutterAngle
*********************************************

``app.project.item(index).shutterAngle``

**Description**

The shutter angle setting for the composition. This corresponds to the Shutter Angle setting in the Advanced tab of the Composition Settings dialog box.

**Type**

Integer in the range ``[0...720]``; read/write.

----

.. _CompItem.shutterPhase:

CompItem.shutterPhase
*********************************************

``app.project.item(index).shutterPhase``

**Description**

The shutter phase setting for the composition. This corresponds to the Shutter Phase setting in the Advanced tab of the Composition Settings dialog box.

**Type**

Integer in the range ``[–360...360]``; read/write.

----

.. _CompItem.workAreaDuration:

CompItem.workAreaDuration
*********************************************

``app.project.item(index).workAreaDuration``

**Description**

The duration of the work area in seconds. This is the difference of the start-point and end-point times of the Composition work area.

**Type**

Floating-point; read/write.

----

.. _CompItem.workAreaStart:

CompItem.workAreaStart
*********************************************

``app.project.item(index).workAreaStart``

**Description**

The time when the Composition work area begins, in seconds.

**Type**

Floating-point; read/write.

----

=======
Methods
=======

.. _CompItem.duplicate:

CompItem.duplicate()
*********************************************

``app.project.item(index).duplicate()``

**Description**

Creates and returns a duplicate of this composition, which contains the same layers as the original.

**Parameters**

None.

**Returns**

CompItem object.

----

.. _CompItem.exportAsMotionGraphicsTemplate:

CompItem.exportAsMotionGraphicsTemplate()
*********************************************

``app.project.item(index).exportAsMotionGraphicsTemplate(doOverWriteFileIfExisting, file_path)``

.. note::
   This functionality was added in After Effects 15.0 (CC 2018)

**Description**

Exports the composition as a Motion Graphics template. Returns true if the Motion Graphics template is successfully exported, false otherwise.

The name in the Essential Graphics panel is used for the file name of the Motion Graphics template (ex., "My Template.mogrt").
Use the ``motionGraphicsTemplateName`` attribute to set the name.

Optionally specify the path to the folder where the Motion Graphics template file is saved. If not specified, the file will be saved in the current
user's Motion Graphics Templates folder:

.. code-block:: text

   macOS: /Users/<name>/Library/Application Support/Adobe/Common/Motion Graphics Templates/
   Windows: C:\Users\<name>\AppData\Roaming\Adobe\Common\Motion Graphics Templates\

If the project has been changed since the last time it was saved, After Effects will prompt the user to save the project. To avoid this, use the
project ``save()`` method before exporting the Motion Graphics template.

**Parameters**

=============================  =================================================================
``doOverWriteFileIfExisting``  Whether to overwrite an existing file of the same name, boolean.
                               Required.
``file_path``                  Path to the folder where the file will be saved. Optional.
=============================  =================================================================

**Returns**

Boolean.

----

.. _CompItem.getMotionGraphicsTemplateControllerName:

CompItem.getMotionGraphicsTemplateControllerName()
**************************************************

``app.project.item(index).getMotionGraphicsTemplateControllerName(index)``

.. note::
   This functionality was added in After Effects 16.1 (CC 2019)

**Description**

Gets the name of a single property in the Essential Graphics panel.

**Parameters**

=========  ===================================================================
``index``  Integer; the index of the EGP property whose name will be returned.
=========  ===================================================================

**Returns**

String; read-only.

----

.. _CompItem.setMotionGraphicsControllerName:

CompItem.setMotionGraphicsControllerName()
*********************************************

``app.project.item(index).setMotionGraphicsControllerName(index,newName)``

.. note::
   This functionality was added in After Effects 16.1 (CC 2019)

**Description**

Sets the name of a single property in the Essential Graphics panel.

.. note::
   To rename a property as it is added to the EGP, see :ref:`Property.addToMotionGraphicsTemplateAs`.

**Parameters**

===========  =================================================================
``index``    Integer; the index of the EGP property to be renamed.
``newName``  String; the new name for the EGP property.
===========  =================================================================

**Returns**

String; read-only.

----

.. _CompItem.layer:

CompItem.layer()
*********************************************

|  ``app.project.item(index).layer(index)``
|  ``app.project.item(index).layer(otherLayer, relIndex)``
|  ``app.project.item(index).layer(name)``

**Description**

Returns a Layer object, which can be specified by name, an index position in this layer, or an index position relative to another layer.

**Parameters**

=========  =================================================================
``index``  The index number of the desired layer in this composition. An
           integer in the range ``[1...numLayers]``, where ``numLayers`` is
           the number of layers in the composition.
=========  =================================================================

or:

==============  =============================================================
``otherLayer``  A Layer object in this composition. The ``relIndex`` value is
                added to the index value of thislayer to find the position of
                the desired layer.
``relIndex``    The position of the desired layer, relative to ``otherLayer``.
                An integer in the range ``[1 – otherLayer.index...numLayers –
                otherLayer.index]``, where ``numLayers`` is the number of
                layers in the composition. This value is added to the
                ``otherLayer`` value to derive the absolute index of the
                layer to return.
==============  =============================================================

—or—

========  ====================================================
``name``  The string containing the name of the desired layer.
========  ====================================================

**Returns**

:ref:`Layer`.

----

.. _CompItem.openInEssentialGraphics:

CompItem.openInEssentialGraphics()
*********************************************

``app.project.item(index).openInEssentialGraphics()``

.. note::
   This functionality was added in After Effects 15.0 (CC 2018)

**Description**

Opens the composition in the Essential Graphics panel.

**Parameters**

None.

**Returns**

Nothing.

----

.. _CompItem.openInViewer:

CompItem.openInViewer()
*********************************************

``app.project.item(index).openInViewer()``

**Description**

Opens the composition in a Composition panel, and moves the Composition panel to front and gives it focus.

**Parameters**

None.

**Returns**

:ref:`Viewer` object for the Composition panel, or null if the composition could not be opened.
