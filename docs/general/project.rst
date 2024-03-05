.. highlight:: javascript
.. _project:

Project object
##############

``app.project``

**Description**

The project object represents an After Effects project. Attributes provide access to specific objects within the project, such as imported files or footage and compositions, and also to project settings such as the timecode base. Methods can import footage, create solids, compositions and folders, and save changes.

----

==========
Attributes
==========

.. _Project.activeItem:

Project.activeItem
*********************************************

``app.project.activeItem``

**Description**

The item that is currently active and is to be acted upon, or a null if no item is currently selected or if multiple items are selected.

**Type**

:ref:`Item` or null; read-only.

----

.. _Project.bitsPerChannel:

Project.bitsPerChannel
*********************************************

``app.project.bitsPerChannel``

**Description**

The color depth of the current project, either 8, 16, or 32 bits.

**Type**

Integer (8, 16, or 32 only); read/write.

----

.. _Project.compensateForSceneReferredProfiles:

Project.compensateForSceneReferredProfiles
*********************************************

``app.project.compensateForSceneReferredProfiles``

.. note::
   This functionality was added in After Effects 16.0 (CC 2019)

**Description**

True if Compensate for Scene-referred Profiles should be enabled for this project; otherwise false.

**Type**

Boolean; read/write.

----

.. _Project.dirty:

Project.dirty
*********************************************

``app.project.dirty``

.. note::
  This functionality was added in After Effects 17.5 (CC2020).

.. warning::
  This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

**Description**

True if the project has been modified from the last save; otherwise false.

"Dirty" projects will have an ``*`` in the project window title.

**Type**

Boolean; read-only.

----

.. _Project.displayStartFrame:

Project.displayStartFrame
*********************************************

``app.project.displayStartFrame``

**Description**

An alternate way of setting the Frame Count menu setting in the Project Settings dialog box to 0 or 1, and is equivalent to using the ``FramesCountType.FC_START_0`` or ``FramesCountType.FC_START_1`` enumerated values for the :ref:`framesCountType <project.framescounttype>`.

**Type**

Integer (0 or 1); read/write.

----

.. _Project.expressionEngine:

Project.expressionEngine
*********************************************

``app.project.expressionEngine``

.. note::
   This functionality was added in After Effects 16.0 (CC 2019)

**Description**

The Expressions Engine setting in the Project Settings dialog box, as a string. One of:

- ``extendscript``
- ``javascript-1.0``

**Type**

String; read/write.

----

.. _Project.feetFramesFilmType:

Project.feetFramesFilmType
*********************************************

``app.project.feetFramesFilmType``

**Description**

The Use Feet + Frames menu setting in the Project Settings dialog box. Use this attribute instead of the old ``timecodeFilmType`` attribute.

**Type**

A ``FeetFramesFilmType`` enumerated value; read/write. One of:

-  ``FeetFramesFilmType.MM16``
-  ``FeetFramesFilmType.MM35``

----

.. _Project.file:

Project.file
*********************************************

``app.project.file``

**Description**

The `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file containing the project that is currently open.

**Type**

`File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object or null if project has not been saved; read-only.

----

.. _Project.footageTimecodeDisplayStartType:

Project.footageTimecodeDisplayStartType
*********************************************

``app.project.footageTimecodeDisplayStartType``

**Description**

The Footage Start Time setting in the Project Settings dialog box, which is enabled when Timecode is selected as the time display style.

**Type**

A ``FootageTimecodeDisplayStartType`` enumerated value; read/write. One of:

-  ``FootageTimecodeDisplayStartType.FTCS_START_0``
-  ``FootageTimecodeDisplayStartType.FTCS_USE_SOURCE_MEDIA``

----

.. _Project.framesCountType:

Project.framesCountType
*********************************************

``app.project.framesCountType``

**Description**

The Frame Count menu setting in the Project Settings dialog box.

**Type**

A ``FramesCountType`` enumerated value; read/write. One of:

-  ``FramesCountType.FC_START_1``
-  ``FramesCountType.FC_START_0``
-  ``FramesCountType.FC_TIMECODE_CONVERSION``

.. WARNING:: Setting this attribute to ``FramesCountType.FC_TIMECODE_CONVERSION`` resets the ``displayStartFrame`` attribute to 0.

----

.. _Project.framesUseFeetFrames:

Project.framesUseFeetFrames
*********************************************

``app.project.framesUseFeetFrames``

**Description**

The Use Feet + Frames setting in the Project Settings dialog box. True if using Feet + Frames; false if using Frames.

**Type**

Boolean; read/write.

----

.. _Project.gpuAccelType:

Project.gpuAccelType
*********************************************

``app.project.gpuAccelType``

.. note::
   This functionality was added in After Effects 13.8 (CC 2015.3)

**Description**

Get or set the current projects GPU Acceleration option.
see :ref:`app.availableGPUAccelTypes`

**Type**

A ``GpuAccelType`` enumerated value; read/write. One of:

- ``GpuAccelType.CUDA``
- ``GpuAccelType.Metal``
- ``GpuAccelType.OPENCL``
- ``GpuAccelType.SOFTWARE``

**Example**

.. code:: javascript

    // access via scripting to Project Settings -> Video Rendering and Effects -> Use

    var currentGPUSettings = app.project.gpuAccelType; // returns the current value
    var type_str = "";

    // check the current value and alert the user

    switch (currentGPUSettings) {
        case GpuAccelType.CUDA:
            type_str = "CUDA";
            break;
        case GpuAccelType.METAL:
            type_str = "Metal";
            break;
        case GpuAccelType.OPENCL:
            type_str = "OpenCL";
            break;
        case GpuAccelType.SOFTWARE:
            type_str = "Software";
            break;
        default:
            type_str = "UNKNOWN";
    }

    alert("Your current setting is " + type_str);

    // set the value to Metal
    app.project.gpuAccelType = GpuAccelType.METAL;

----

.. _Project.items:

Project.items
*********************************************

``app.project.items``

**Description**

All of the items in the project.

**Type**

:ref:`ItemCollection`; read-only.

----

.. _Project.linearBlending:

Project.linearBlending
*********************************************

``app.project.linearBlending``

**Description**

True if linear blending should be used for this project; otherwise false.

**Type**

Boolean; read/write.

----

.. _Project.linearizeWorkingSpace:

Project.linearizeWorkingSpace
*********************************************

``app.project.linearizeWorkingSpace``

.. note::
   This functionality was added in After Effects 16.0 (CC 2019)

**Description**

True if Linearize Working Space should be enabled for this project; otherwise false.

**Type**

Boolean; read/write.

----

.. _Project.numItems:

Project.numItems
*********************************************

``app.project.numItems``

**Description**

The total number of items contained in the project, including folders and all types of footage.

**Type**

Integer; read-only.

**Example**

.. code:: javascript

    var numItems = app.project.numItems;
    alert("There are " + numItems + " items in this project.")

----

.. _Project.renderQueue:

Project.renderQueue
*********************************************

``app.project.renderQueue``

**Description**

The renderqueue of the project.

**Type**

:ref:`RenderQueue`; read-only.

----

.. _Project.revision:

Project.revision
*********************************************

``app.project.revision``

**Description**

The current revision of the project. Every user action increases the revision number. New project starts at revision 1.

**Type**

Integer; the current revision version of the project; read-only.

----

.. _Project.rootFolder:

Project.rootFolder
*********************************************

``app.project.rootFolder``

**Description**

The root folder containing the contents of the project; this is a virtual folder that contains all items in the Project panel, but not items contained inside other folders in the Project panel.

**Type**

:ref:`FolderItem`; read-only.

----

.. _Project.selection:

Project.selection
*********************************************

``app.project.selection``

**Description**

All items selected in the Project panel, in the sort order shown in the Project panel.

**Type**

Array of :ref:`Item objects <item>`; read-only.

----

.. _Project.timeDisplayType:

Project.timeDisplayType
*********************************************

``app.project.timeDisplayType``

**Description**

The time display style, corresponding to the Time Display Style section in the Project Settings dialog box.

**Type**

A ``TimeDisplayType`` enumerated value; read/write. One of:

-  ``TimeDisplayType.FRAMES``
-  ``TimeDisplayType.TIMECODE``

----

.. _Project.toolType:

Project.toolType
*********************************************

``app.project.toolType``

.. note::
    This functionality was added in After Effects 14.0 (CC 2017)

**Description**

Get and sets the active tool in the Tools panel.

**Type**

A ``ToolType`` enumerated value; read/write. One of:

- ``ToolType.Tool_Arrow``: Selection Tool
- ``ToolType.Tool_Rotate``: Rotation Tool
- ``ToolType.Tool_CameraMaya``: Unified Camera Tool
- ``ToolType.Tool_CameraOrbit``: Orbit Camera Tool
- ``ToolType.Tool_CameraTrackXY``: Track XY Camera Tool
- ``ToolType.Tool_CameraTrackZ``: Track Z Camera Tool
- ``ToolType.Tool_Paintbrush``: Brush Tool
- ``ToolType.Tool_CloneStamp``: Clone Stamp Tool
- ``ToolType.Tool_Eraser``: Eraser Tool
- ``ToolType.Tool_Hand``: Hand Tool
- ``ToolType.Tool_Magnify``: Zoom Tool
- ``ToolType.Tool_PanBehind``: Pan Behind (Anchor Point) Tool
- ``ToolType.Tool_Rect``: Rectangle Tool
- ``ToolType.Tool_RoundedRect``: Rounded Rectangle Tool
- ``ToolType.Tool_Oval``: Ellipse Tool
- ``ToolType.Tool_Polygon``: Polygon Tool
- ``ToolType.Tool_Star``: Star Tool
- ``ToolType.Tool_TextH``: Horizontal Type Tool
- ``ToolType.Tool_TextV``: Vertical Type Tool
- ``ToolType.Tool_Pen``: Pen Tool
- ``ToolType.Tool_Feather``: Mask Feather Tool
- ``ToolType.Tool_PenPlus``: Add Vertex Tool
- ``ToolType.Tool_PenMinus``: Delete Vertex Tool
- ``ToolType.Tool_PenConvert``: Convert Vertex Tool
- ``ToolType.Tool_Pin``: Puppet Pin Tool
- ``ToolType.Tool_PinStarch``: Puppet Starch Tool
- ``ToolType.Tool_PinDepth``: Puppet Overlap Tool
- ``ToolType.Tool_Quickselect``: Roto Brush Tool
- ``ToolType.Tool_Hairbrush``: Refine Edge Tool

**Examples**

The following sample code checks the current tool, and if it is not the Unified Camera Tool, sets the current tool to that:

.. code:: javascript

    // Check the current tool, then set it to Unified Camera Tool (UCT).
    // Assume a composition is selected in the project.
    var comp = app.project.activeItem;
    if (comp instanceof CompItem) {
        // Add a camera to the current comp. (Requirement for UCT)
        var cameraLayer = comp.layers.addCamera("Test Camera", [comp.width / 2, comp.height / 2]);
        comp.openInViewer();

        // If the currently selected tool is not one of the camera tools, set it to UCT.
        if (( app.project.toolType !== ToolType.Tool_CameraMaya) &&
            ( app.project.toolType !== ToolType.Tool_CameraOrbit ) &&
            ( app.project.toolType !== ToolType.Tool_CameraTrackXY) &&
            ( app.project.toolType !== ToolType.Tool_CameraTrackZ)) {
                app.project.toolType = ToolType.Tool_CameraMaya;
            }
    }

The following sample code uses the new app.project.toolType attribute to create a 360-degrees composition (environment layer and camera) from a selected footage item or composition selected in the Project panel. This script a good starting point for building VR compositions from equirectangular footage:

.. code:: javascript

    // Create a 360 VR comp from a footage item or comp selected in the Project panel.

    var item = app.project.activeItem;
    if (item !== null && (item.typeName === "Footage" || item.typeName === "Composition")) {
        // Create a comp with the footage.
        var comp = app.project.items.addComp(item.name, item.width, item.height, item.pixelAspect, item.duration, item.frameRate);
        var layers = comp.layers;
        var footageLayer = layers.add(item);

        // Apply the CC Environment effect and create a camera.
        var effect = footageLayer.Effects.addProperty("CC Environment");
        var camera = layers.addCamera("360 Camera", [item.width / 2, item.height / 2]);
        comp.openInViewer();
        app.project.toolType = ToolType.Tool_CameraMaya;
    } else {
        alert("Select a single footage item or composition in the Project panel.");
    }

----

.. _Project.transparencyGridThumbnails:

Project.transparencyGridThumbnails
*********************************************

``app.project.transparencyGridThumbnails``

**Description**

When true, thumbnail views use the transparency checkerboard pattern.

**Type**

Boolean; read/write.

----

.. _Project.usedFonts:

Project.usedFonts
*********************************************

``app.project.usedFonts``

.. note::
   This functionality was added in After Effects (Beta) 24.0 and subject to change while it remains in Beta.

**Description**

Returns an Array of Objects containing references to used fonts and the Text Layers and times on which they appear in the current :ref:`Project<Project>`. Each object is composed of ``font`` which is a :ref:`Font object<fontobject>`, and ``usedAt`` which is an Array of Objects, each composed of ``layerID``, a :ref:`Layer.id`, and ``timeD`` for when. See :ref:`Project.layerByID` to retrieve the layers.

.. code:: javascript

   var usedList = app.project.usedFonts;
   if (usedList.length) {
       var font = usedList[0].font;
       var usedAt = usedList[0].usedAt;
   
       var str = "[0]:" + font.postScriptName + "\n";
       for (var i = 0; i < usedAt.length; i++) {
            var layerID = usedAt[i].layerID;
            var timeD  = usedAt[i].timeD;

            var layer = app.project.layerByID(layerID);
            str += "   Layer:'" + String(layer.property("Source Text").valueAtTime(timeD, false)) + "'\n";
       }
       alert(str);
   }

**Type**

Array of Objects; read-only.

----

.. _Project.workingGamma:

Project.workingGamma
********************

``app.project.workingGamma``

**Description**

The current project's working gamma value, either 2.2 or 2.4. Setting values other than 2.2 or 2.4 will cause a scripting error. Note that when the project's color working space is set, the working gamma value is ignored by After Effects.

**Type**

Number; read/write.

**Examples**

* To set the working gamma to 2.4 (Rec. 709): ``app.project.workingGamma = 2.4;``
* To get the current working gamma: ``var currentGamma = app.project.workingGamma;``

----

.. _Project.workingSpace:

Project.workingSpace
********************

``app.project.workingSpace``

**Description**

A string which is the color profile description for the project's color working space. To set the working space to None, set ``workingSpace`` to an empty string.

Use ``app.project.listColorProfiles()`` to return an array of available color profile descriptions that can be used to set the color working space.

**Type**

String; read/write.

**Examples**

* To set the working space to Rec.709 Gamma 2.4: ``app.project.workingSpace = "Rec.709 Gamma 2.4";``
* To set the working space to None: ``app.project.workingSpace = "";``
* To get the current working space: ``var currentSpace = app.project.workingSpace;``

----

.. _Project.xmpPacket:

Project.xmpPacket
*********************************************

``app.project.xmpPacket``

**Description**

The project's XMP metadata, stored as RDF (XML-based). For more information on XMP, see the `JavaScript Tools Guide <https://extendscript.docsforadobe.dev/>`_.

**Type**

String; read/write.

**Example**

The following example code accesses the XMP metadata of the current project, and modifies the Label project metadata field.

.. code:: javascript

    var proj = app.project;

    // load the XMPlibrary as an ExtendScript ExternalObject
    if (ExternalObject.AdobeXMPScript === undefined){
        ExternalObject.AdobeXMPScript = new ExternalObject('lib:AdobeXMPScript');
    }
    var mdata = new XMPMeta(app.project.xmpPacket); //get the project's XMPmetadata
    // update the Label project metadata's value
    var schemaNS = XMPMeta.getNamespaceURI("xmp");
    var propName = "xmp:Label";
    try{
        mdata.setProperty(schemaNS, propName, "finalversion...no, really!");
    } catch (e) {
        alert(e);
    }

    app.project.xmpPacket = mdata.serialize();

----

=======
Methods
=======

.. _Project.autoFixExpressions:

Project.autoFixExpressions()
*********************************************

``app.project.autoFixExpressions(oldText, newText)``

**Description**

Automatically replaces text found in broken expressions in the project, if the new text causes the expression to evaluate without errors.

**Parameters**

===========  ======================
``oldText``  The text to replace.
``newText``  The new text.
===========  ======================

**Returns**

Nothing.

----

.. _Project.close:

Project.close()
*********************************************

``app.project.close(closeOptions)``

**Description**

Closes the project with the option of saving changes automatically, prompting the user to save changes or closing without saving changes.

**Parameters**

================  ============================================================
``closeOptions``  Action to be performed on close. A ``CloseOptions``
                  enumerated value, one of:

                  -  ``CloseOptions.DO_NOT_SAVE_CHANGES``: Close without
                     saving.
                  -  ``CloseOptions.PROMPT_TO_SAVE_CHANGES``:Prompt for
                     whether to save changes before close.
                  -  ``CloseOptions.SAVE_CHANGES``: Save automatically on
                     close.
================  ============================================================

**Returns**

Boolean. True on success. False if the file has not been previously saved, the user is prompted, and the user cancels the save.

----

.. _Project.consolidateFootage:

Project.consolidateFootage()
*********************************************

``app.project.consolidateFootage()``

**Description**

Consolidates all footage in the project. Same as the File > Consolidate All Footage command.

**Parameters**

None.

**Returns**

Integer; the total number of footage items removed.

----

.. _Project.importFile:

Project.importFile()
*********************************************

``app.project.importFile(importOptions)``

**Description**

Imports the file specified in the specified ImportOptions object, using the specified options. Same as the File > Import File command.

Creates and returns a new FootageItem object from the file, and adds it to the project's items array.

**Parameters**

=================   =====================================================
``importOptions``   An :ref:`ImportOptions` specifying the file to
                    import and the options for the operation.
=================   =====================================================

**Returns**

:ref:`FootageItem`.

**Example**

.. code:: javascript

    app.project.importFile(new ImportOptions(new File("sample.psd"));

----

.. _Project.importFileWithDialog:

Project.importFileWithDialog()
*********************************************

``app.project.importFileWithDialog()``

**Description**

Shows an Import File dialog box. Same as the File > Import > File command.

**Returns**

Array of :ref:`Item objects <item>` created during import; or null if the user cancels the dialog box.

----

.. _Project.importPlaceholder:

Project.importPlaceholder()
*********************************************

``app.project.importPlaceholder(name, width, height, frameRate, duration)``

**Description**

Creates and returns a new PlaceholderItem and adds it to the project's items array. Same as the File > Import > Placeholder command.

**Parameters**

==============  ===============================================================
``name``        A string containing the name of the placeholder.
``width``       The width of the placeholder in pixels, an integer in the range
                ``[4..30000]``.
``height``      The height of the placeholder in pixels, an integer in the
                range ``[4..30000]``.
``frameRate``   The frame rate of the placeholder, a floating-point value in
                the range ``[1.0..99.0]``.
``duration``    The duration of the placeholder in seconds, a floating-point
                value in the range ``[0.0..10800.0]``.
==============  ===============================================================

**Returns**

PlaceholderItem object.

----

.. _Project.item:

Project.item()
*********************************************

``app.project.item(index)``

**Description**

Retrieves an item at a specified index position.

**Parameters**

=========  ====================================================================
``index``  The index position of the item, an integer. The first item is at
           index 1.
=========  ====================================================================

**Returns**

:ref:`Item`.

----

.. _Project.itemByID:

Project.itemByID()
*********************************************

``app.project.itemByID(id)``

.. note::
   This functionality was added in After Effects 13.0 (CC 2014)

**Description**

Retrieves an item by its :ref:`Item ID <Item.id>`

**Parameters**

======  ====================================================================
``id``  The ID of an item, an integer.
======  ====================================================================

**Returns**

:ref:`Item`.

----

.. _Project.layerByID:

Project.layerByID()
*********************************************

``app.project.layerByID(id)``

.. note::
   This functionality was added in After Effects 22.0 (2022)

**Description**

Instance method on Project which, when given a valid ID value, returns the Layer object in the Project with that given ID.

**Parameters**

===========     ======================
``id``          A non-negative integer representing the ID of the Layer to be retrieved from the Project.
===========     ======================

**Returns**

:ref:`Layer` with the given ID if it exists on the project; otherwise null. Non-valid IDs will throw an exception stating that the input parameter is not an unsigned integer.

**Example**

.. code:: javascript

   var firstComp = app.project.item(1);
   var firstLayer = firstComp.layer(1);
   var layerID = firstLayer.id;

   if (app.project.layerByID(layerID) === firstLayer) {
      alert("You can get the Layer from the ID!");
   }

----

.. _Project.listColorProfiles:

Project.listColorProfiles()
***************************

``app.project.listColorProfiles()``

**Description**

Returns an array of color profile descriptions that can be set as the project's color working space.

**Parameters**

None.

**Returns**

Array of strings.

----

.. _Project.reduceProject:

Project.reduceProject()
*********************************************

``app.project.reduceProject(array_of_items)``

**Description**

Removes all items from the project except those specified. Same as the File > Reduce Project command.

**Parameters**

==================  ===========================================================
``array_of_items``  An array containing the :ref:`Item objects <item>` that are
                    to be kept.
==================  ===========================================================

**Returns**

Integer; the total number of items removed.

**Example**

.. code:: javascript

    var items = [];
    items[items.length] = app.project.item(1);
    items[items.length] = app.project.item(3);
    app.project.reduceProject(items);

----

.. _Project.removeUnusedFootage:

Project.removeUnusedFootage()
*********************************************

``app.project.removeUnusedFootage()``

**Description**

Removes unused footage from the project. Same as the File > Remove Unused Footage command.

**Parameters**

None.

**Returns**

Integer; the total number of FootageItem objects removed.

----

.. _Project.replaceFont:

Project.replaceFont()
**************************************

``app.project.replaceFont(fromFont, toFont, [noFontLocking = false])``

.. note::
   This functionality was added in After Effects (Beta) 24.0 and subject to change while it remains in Beta.

**Description**

This function will replace all the usages of :ref:`fontobject` ``fromFont`` with :ref:`fontobject` ``toFont``.

This operation exposes the same mechanism and policy used for automatic font replacement of missing or substituted fonts and is therefore a complete and precise replacement, even on :ref:`TextDocuments<TextDocument>` which have mixed styling, preserving the character range the ``fromFont`` was applied to.

This operation is not undoable.

The optional parameter ``noFontLocking`` controls what happens when the ``toFont`` has no glyphs for the text it is applied to. By default a fallback font will be selected which will have the necessary glyphs, but if this parameter is set to true then this fallback will not take place and missing glyphs will result. There is no way at the current time to detect or report this.

Note that when ``fromFont`` is a substituted font and the ``toFont`` has the same font properties no fallback can occur and the parameter is ignored and treated as true.


.. code:: javascript

   var fromFont = app.project.usedFonts[0].font;
   var fontList = app.fonts.getFontsByPostScriptName("TimesNewRomanPSMT");
   var toFont = fontList[0];
   var layerChanged = app.project.replaceFont(fromFont, toFont);

**Parameters**

====================  ========================================================
``fromFont``          A :ref:`fontobject` to be replaced.
``toFont``            A :ref:`fontobject` to replace it with.
``noFontLocking``     An optional Boolean, defaults to false
====================  ========================================================

**Returns**

Boolean. True if at least one Layer was changed.

----

.. _Project.save:

Project.save()
*********************************************

``app.project.save([file])``

**Description**

Saves the project. The same as the File > Save or File > Save As command. If the project has never previously been saved and no file is specified, prompts the user for a location and file name.

Pass a `File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object to save a project to a new file without prompting.

**Parameters**

========  ============================================================
``file``  Optional. An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file to save.
========  ============================================================

**Returns**

None.

----

.. _Project.saveWithDialog:

Project.saveWithDialog()
*********************************************

``app.project.saveWithDialog()``

**Description**

Shows the Save dialog box. The user can name a file with a location and save the project, or click Cancel to exit the dialog box.

**Parameters**

None.

**Returns**

Boolean; true if the project was saved.

----

.. _Project.setDefaultImportFolder:

Project.setDefaultImportFolder()
********************************

``app.project.setDefaultImportFolder(folder)``

**Description**

Sets the folder that will be shown in the file import dialog. This location will be used as an override until setDefaultImportFolder() is called with no parameters, or until After Effects is quit.

**Parameters**

==========   ===========================
``folder``   `Extendscript Folder <https://extendscript.docsforadobe.dev/file-system-access/folder-object.html>`_ object.
==========   ===========================

**Returns**

Boolean; indicates if the operation was successful.

**Examples**

Any of the following will set the default import folder to C:/My Folder:

* ``var myFolder = new Folder("C:/My Folder"); app.project.setDefaultImportFolder(myFolder);``
* ``app.project.setDefaultImportFolder(new Folder("C:/My Folder"));``
* ``app.project.setDefaultImportFolder(Folder("C:/My Folder"));``

Note: if the path refers to an existing file and not a folder, the Folder function returns a File object instead of a Folder object, which will cause ``setDefaultImportFolder()`` to return false.

To set the default import folder to the current user's desktop folder: ``app.project.setDefaultImportFolder(Folder.desktop);``

To disable the default folder, call ``setDefaultImportFolder()`` with no parameters: ``app.project.setDefaultImportFolder();``

----

.. _Project.showWindow:

Project.showWindow()
*********************************************

``app.project.showWindow(doShow)``

**Description**

Shows or hides the Project panel.

**Parameters**

==========  ===================================================================
``doShow``  When true, show the Project panel. When false, hide the Project
            panel.
==========  ===================================================================

**Returns**

Nothing.

----

=============
Team Projects
=============

.. _Project.newTeamProject:

Project.newTeamProject()
*********************************************

``app.project.newTeamProject(teamProjectName, description)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Creates a new team project.

**Parameters**

===================  =================================================
``teamProjectName``  Team project name, string value.
``description``      Optional. Team project description, string value.
===================  =================================================

**Returns**

Boolean. ``True`` if the team project is successfully created, ``false`` otherwise.

----

.. _Project.openTeamProject:

Project.openTeamProject()
*********************************************

``app.project.openTeamProject(teamProjectName)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Opens a team project.

**Parameters**

===================  ================================
``teamProjectName``  Team project name, string value.
===================  ================================

**Returns**

Boolean. ``True`` if the team project is successfully opened, ``false`` otherwise.

----

.. _Project.shareTeamProject:

Project.shareTeamProject()
*********************************************

``app.project.shareTeamProject(comment)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Shares the currently open team project.

**Parameters**

===========  ================================
``comment``  Comment, string value. Optional.
===========  ================================

**Returns**

Boolean. ``True`` if the team project is successfully shared, ``false`` otherwise.

----

.. _Project.syncTeamProject:

Project.syncTeamProject()
*********************************************

``app.project.syncTeamProject()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Syncs the currently open team project.

**Returns**

Boolean. ``True`` if the team project is successfully synced, ``false`` otherwise.

----

.. _Project.closeTeamProject:

Project.closeTeamProject()
*********************************************

``app.project.closeTeamProject()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Closes a currently open team project.

**Returns**

Boolean. ``True`` if the team project is successfully closed, ``false`` otherwise.

----

.. _Project.convertTeamProjectToProject:

Project.convertTeamProjectToProject()
*********************************************

``app.project.convertTeamProjectToProject(project_file)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Converts a team project to an After Effects project on a local disk.

**Parameters**

================  ======================================================================
``project_file``  File object for the local After Effects project.
                  File extension should be either .aep or .aet (.aepx is not supported).
================  ======================================================================

**Returns**

Boolean. ``True`` if the team project is successfully converted, ``false`` otherwise.

----

.. _Project.listTeamProjects:

Project.listTeamProjects()
*********************************************

``app.project.listTeamProjects()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Returns an array containing the name strings for all team projects available for the current user.
Archived Team Projects are not included.

**Returns**

Array of strings.

----

.. _Project.isTeamProjectOpen:

Project.isTeamProjectOpen()
*********************************************

``app.project.isTeamProjectOpen(teamProjectName)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether specified team project is currently open.

**Parameters**

===================  ================================
``teamProjectName``  Team project name, string value.
===================  ================================

**Returns**

Boolean. ``True`` if the specified team project is currently open, ``false`` otherwise.

----

.. _Project.isAnyTeamProjectOpen:

Project.isAnyTeamProjectOpen()
*********************************************

``app.project.isAnyTeamProjectOpen()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether any team project is currently open.

**Returns**

Boolean. ``True`` if any team project is currently open, ``false`` otherwise.

----

.. _Project.isTeamProjectEnabled:

Project.isTeamProjectEnabled()
*********************************************

``app.project.isTeamProjectEnabled()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether or not team project is enabled for After Effects. (This will almost always return true.)

**Returns**

Boolean. ``True`` if team project is currently enabled, ``false`` otherwise.

----

.. _Project.isLoggedInToTeamProject:

Project.isLoggedInToTeamProject()
*********************************************

``app.project.isLoggedInToTeamProject()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether or not the client (After Effects) is currently logged into the team project server.

**Returns**

Boolean. ``True`` if the client (After Effects) is currently logged into the team projects server, ``false`` otherwise.

----

.. _Project.isSyncCommandEnabled:

Project.isSyncCommandEnabled()
*********************************************

``app.project.isSyncCommandEnabled()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether or not the Sync command is enabled.

**Returns**

Boolean. ``True`` if the team projects Sync command is enabled, ``false`` otherwise.

----

.. _Project.isShareCommandEnabled:

Project.isShareCommandEnabled()
*********************************************

``app.project.isShareCommandEnabled()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether or not the Share command is enabled.

**Returns**

Boolean. ``True`` if the team projects Share command is enabled, ``false`` otherwise.

----

.. _Project.isResolveCommandEnabled:

Project.isResolveCommandEnabled()
*********************************************

``app.project.isResolveCommandEnabled()``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Checks whether or not the Resolve command is enabled.

**Returns**

Boolean. ``True`` if the team projects Resolve command is enabled, ``false`` otherwise.

----

.. _Project.resolveConflict:

Project.resolveConflict()
*********************************************

``app.project.resolveConflict(ResolveType)``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

Resolves a conflict between the open team project and the version on the team projects server, using the specified resolution method.

**Parameters**

===============  ===================================================================================
``ResolveType``  The type of conflict resolution to use. A ``ResolveType`` enumerated value, one of:

                  -  ``ResolveType.ACCEPT_THEIRS``: Take the shared version.
                     The shared version replaces your version.
                  -  ``ResolveType.ACCEPT_YOURS``: Keep your version of the project.
                     The shared version is not taken.
                  -  ``ResolveType.ACCEPT_THEIRS_AND_COPY``: Copy and rename your version,
                     then take the shared version. The shared version replaces your original version
===============  ===================================================================================

**Returns**

Boolean. ``True`` if the resolution of the specified type was successful, ``false`` otherwise.
