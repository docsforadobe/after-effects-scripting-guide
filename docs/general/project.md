# Project object

`app.project`

#### Description

The project object represents an After Effects project. Attributes provide access to specific objects within the project, such as imported files or footage and compositions, and also to project settings such as the timecode base. Methods can import footage, create solids, compositions and folders, and save changes.

---

## Attributes

### Project.activeItem

`app.project.activeItem`

#### Description

The item that is currently active and is to be acted upon, or `null` if no item is currently selected or if multiple items are selected.

#### Type

[Item object](../item/item.md) or `null`; read-only.

---

### Project.bitsPerChannel

`app.project.bitsPerChannel`

#### Description

The color depth of the current project, either 8, 16, or 32 bits.

#### Type

Integer (8, 16, or 32 only); read/write.

---

### Project.compensateForSceneReferredProfiles

`app.project.compensateForSceneReferredProfiles`

!!! note
    This functionality was added in After Effects 16.0 (CC 2019)

#### Description

`true` if Compensate for Scene-referred Profiles should be enabled for this project; otherwise `false`.

#### Type

Boolean; read/write.

---

### Project.dirty

`app.project.dirty`

!!! note
    This functionality was added in After Effects 17.5 (CC2020).

!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

#### Description

`true` if the project has been modified from the last save; otherwise `false`.

"Dirty" projects will have an `*` in the project window title.

#### Type

Boolean; read-only.

---

### Project.displayStartFrame

`app.project.displayStartFrame`

#### Description

An alternate way of setting the Frame Count menu setting in the Project Settings dialog box to 0 or 1, and is equivalent to using the `FramesCountType.FC_START_0` or `FramesCountType.FC_START_1` enumerated values for the [framesCountType](#projectframescounttype).

#### Type

Integer (0 or 1); read/write.

---

### Project.expressionEngine

`app.project.expressionEngine`

!!! note
    This functionality was added in After Effects 16.0 (CC 2019)

#### Description

The Expressions Engine setting in the Project Settings dialog box, as a string. One of:

- `extendscript`
- `javascript-1.0`

#### Type

String; read/write.

---

### Project.feetFramesFilmType

`app.project.feetFramesFilmType`

#### Description

The Use Feet + Frames menu setting in the Project Settings dialog box. Use this attribute instead of the old `timecodeFilmType` attribute.

#### Type

A `FeetFramesFilmType` enumerated value; read/write. One of:

- `FeetFramesFilmType.MM16`
- `FeetFramesFilmType.MM35`

---

### Project.file

`app.project.file`

#### Description

The [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the file containing the project that is currently open.

#### Type

[File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object or `null` if project has not been saved; read-only.

---

### Project.footageTimecodeDisplayStartType

`app.project.footageTimecodeDisplayStartType`

#### Description

The Footage Start Time setting in the Project Settings dialog box, which is enabled when Timecode is selected as the time display style.

#### Type

A `FootageTimecodeDisplayStartType` enumerated value; read/write. One of:

- `FootageTimecodeDisplayStartType.FTCS_START_0`
- `FootageTimecodeDisplayStartType.FTCS_USE_SOURCE_MEDIA`

---

### Project.framesCountType

`app.project.framesCountType`

#### Description

The Frame Count menu setting in the Project Settings dialog box.

#### Type

A `FramesCountType` enumerated value; read/write. One of:

- `FramesCountType.FC_START_1`
- `FramesCountType.FC_START_0`
- `FramesCountType.FC_TIMECODE_CONVERSION`

!!! warning
    Setting this attribute to `FramesCountType.FC_TIMECODE_CONVERSION` resets the `displayStartFrame` attribute to 0.

---

### Project.framesUseFeetFrames

`app.project.framesUseFeetFrames`

#### Description

The "Use Feet + Frames" setting in the Project Settings dialog box.

`true` if using Feet + Frames; `false` if using Frames.

#### Type

Boolean; read/write.

---

### Project.gpuAccelType

`app.project.gpuAccelType`

!!! note
    This functionality was added in After Effects 13.8 (CC 2015.3)

#### Description

Get or set the current projects GPU Acceleration option.
see [app.availableGPUAccelTypes](application.md#appavailablegpuacceltypes)

#### Type

A `GpuAccelType` enumerated value; read/write. One of:

- `GpuAccelType.CUDA`
- `GpuAccelType.Metal`
- `GpuAccelType.OPENCL`
- `GpuAccelType.SOFTWARE`

#### Example

```javascript
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
```

---

### Project.items

`app.project.items`

#### Description

All of the items in the project.

#### Type

[ItemCollection object](../item/itemcollection.md); read-only.

---

### Project.linearBlending

`app.project.linearBlending`

#### Description

`true` if linear blending should be used for this project; otherwise `false`.

#### Type

Boolean; read/write.

---

### Project.linearizeWorkingSpace

`app.project.linearizeWorkingSpace`

!!! note
    This functionality was added in After Effects 16.0 (CC 2019)

#### Description

`true` if Linearize Working Space should be enabled for this project; otherwise `false`.

#### Type

Boolean; read/write.

---

### Project.numItems

`app.project.numItems`

#### Description

The total number of items contained in the project, including folders and all types of footage.

#### Type

Integer; read-only.

#### Example

```javascript
var numItems = app.project.numItems;
alert("There are " + numItems + " items in this project.")
```

---

### Project.renderQueue

`app.project.renderQueue`

#### Description

The [Render Queue](../renderqueue/renderqueue.md) of the project.


#### Type

[RenderQueue object](../renderqueue/renderqueue.md); read-only.

---

### Project.revision

`app.project.revision`

#### Description

The current revision of the project. Every user action increases the revision number. New project starts at revision 1.

#### Type

Integer; the current revision version of the project; read-only.

---

### Project.rootFolder

`app.project.rootFolder`

#### Description

The root folder containing the contents of the project; this is a virtual folder that contains all items in the Project panel, but not items contained inside other folders in the Project panel.

#### Type

[FolderItem object](../item/folderitem.md); read-only.

---

### Project.selection

`app.project.selection`

#### Description

All items selected in the Project panel, in the sort order shown in the Project panel.

#### Type

Array of [Item objects](../item/item.md); read-only.

---

### Project.timeDisplayType

`app.project.timeDisplayType`

#### Description

The time display style, corresponding to the Time Display Style section in the Project Settings dialog box.

#### Type

A `TimeDisplayType` enumerated value; read/write. One of:

- `TimeDisplayType.FRAMES`
- `TimeDisplayType.TIMECODE`

---

### Project.toolType

`app.project.toolType`

!!! note
    This functionality was added in After Effects 14.0 (CC 2017)

#### Description

Get and sets the active tool in the Tools panel.

#### Type

A `ToolType` enumerated value; read/write. One of:

- `ToolType.Tool_Arrow`: Selection Tool
- `ToolType.Tool_Rotate`: Rotation Tool
- `ToolType.Tool_CameraMaya`: Unified Camera Tool
- `ToolType.Tool_CameraOrbit`: Orbit Camera Tool
- `ToolType.Tool_CameraTrackXY`: Track XY Camera Tool
- `ToolType.Tool_CameraTrackZ`: Track Z Camera Tool
- `ToolType.Tool_Paintbrush`: Brush Tool
- `ToolType.Tool_CloneStamp`: Clone Stamp Tool
- `ToolType.Tool_Eraser`: Eraser Tool
- `ToolType.Tool_Hand`: Hand Tool
- `ToolType.Tool_Magnify`: Zoom Tool
- `ToolType.Tool_PanBehind`: Pan Behind (Anchor Point) Tool
- `ToolType.Tool_Rect`: Rectangle Tool
- `ToolType.Tool_RoundedRect`: Rounded Rectangle Tool
- `ToolType.Tool_Oval`: Ellipse Tool
- `ToolType.Tool_Polygon`: Polygon Tool
- `ToolType.Tool_Star`: Star Tool
- `ToolType.Tool_TextH`: Horizontal Type Tool
- `ToolType.Tool_TextV`: Vertical Type Tool
- `ToolType.Tool_Pen`: Pen Tool
- `ToolType.Tool_Feather`: Mask Feather Tool
- `ToolType.Tool_PenPlus`: Add Vertex Tool
- `ToolType.Tool_PenMinus`: Delete Vertex Tool
- `ToolType.Tool_PenConvert`: Convert Vertex Tool
- `ToolType.Tool_Pin`: Puppet Pin Tool
- `ToolType.Tool_PinStarch`: Puppet Starch Tool
- `ToolType.Tool_PinDepth`: Puppet Overlap Tool
- `ToolType.Tool_Quickselect`: Roto Brush Tool
- `ToolType.Tool_Hairbrush`: Refine Edge Tool

#### Examples

The following sample code checks the current tool, and if it is not the Unified Camera Tool, sets the current tool to that:

```javascript
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
```

The following sample code uses the new app.project.toolType attribute to create a 360-degrees composition (environment layer and camera) from a selected footage item or composition selected in the Project panel. This script a good starting point for building VR compositions from equirectangular footage:

```javascript
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
```

---

### Project.transparencyGridThumbnails

`app.project.transparencyGridThumbnails`

#### Description

When `true`, thumbnail views use the transparency checkerboard pattern.

#### Type

Boolean; read/write.

---

### Project.usedFonts

`app.project.usedFonts`

!!! note
    This functionality was added in After Effects 24.5

#### Description

Returns an Array of Objects containing references to used fonts and the Text Layers and times on which they appear in the current [Project](#project-object).

Each object is composed of `font` which is a [Font object](../text/fontobject.md), and `usedAt` which is an Array of Objects, each composed of `layerID`, a [Layer.id](../layer/layer.md#layerid), and `layerTimeD` for when. See [Project.layerByID()](#projectlayerbyid) to retrieve the layers.

```javascript
var usedList = app.project.usedFonts;
if (usedList.length) {
    var font = usedList[0].font;
    var usedAt = usedList[0].usedAt;

    var str = "[0]:" + font.postScriptName + "\n";
    for (var i = 0; i < usedAt.length; i++) {
        var layerID = usedAt[i].layerID;
        // valueAtTime() for Source Text property is expecting timed
        // to be in Layer Time instead of Comp Time, unlike any of
        // the other properties. So we have adjusted the name returned
        // by usedFonts to make this clear as we expect that is where
        // it will be used next.
        var layerTimeD = usedAt[i].layerTimeD;

        var layer = app.project.layerByID(layerID);
        str += "    Layer:'" + String(layer.property("Source Text").valueAtTime(layerTimeD, false)) + "'\n";
    }
    alert(str);
}
```

#### Type

Array of Objects; read-only.

---

### Project.workingGamma

`app.project.workingGamma`

#### Description

The current project's working gamma value, either 2.2 or 2.4.

Setting values other than 2.2 or 2.4 will cause a scripting error.

!!! tip
    When the project's color working space is set, the working gamma value is ignored by After Effects.

#### Type

`2.2` or `2.4`; read/write.

#### Examples

* To set the working gamma to 2.4 (Rec. 709): `app.project.workingGamma = 2.4;`
* To get the current working gamma: `var currentGamma = app.project.workingGamma;`

---

### Project.workingSpace

`app.project.workingSpace`

#### Description

A string which is the color profile description for the project's color working space. To set the working space to None, set `workingSpace` to an empty string.

Use `app.project.listColorProfiles()` to return an array of available color profile descriptions that can be used to set the color working space.

#### Type

String; read/write.

#### Examples

* To set the working space to Rec.709 Gamma 2.4: `app.project.workingSpace = "Rec.709 Gamma 2.4";`
* To set the working space to None: `app.project.workingSpace = "";`
* To get the current working space: `var currentSpace = app.project.workingSpace;`

---

### Project.xmpPacket

`app.project.xmpPacket`

#### Description

The project's XMP metadata, stored as RDF (XML-based). For more information on XMP, see the [JavaScript Tools Guide](https://extendscript.docsforadobe.dev/).

#### Type

String; read/write.

#### Example

The following example code accesses the XMP metadata of the current project, and modifies the Label project metadata field.

```javascript
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
```

---

## Methods

### Project.autoFixExpressions()

`app.project.autoFixExpressions(oldText, newText)`

#### Description

Automatically replaces text found in broken expressions in the project, if the new text causes the expression to evaluate without errors.

#### Parameters

| Parameter |  Type  |     Description      |
| --------- | ------ | -------------------- |
| `oldText` | String | The text to replace. |
| `newText` | String | The new text.        |

#### Returns

Nothing.

---

### Project.close()

`app.project.close(closeOptions)`

#### Description

Closes the project with the option of saving changes automatically, prompting the user to save changes or closing without saving changes.

#### Parameters

+----------------+---------------------+-------------------------------------------------------------------------------------------+
|   Parameter    |        Type         |                                        Description                                        |
+================+=====================+===========================================================================================+
| `closeOptions` | `CloseOptions` enum | Action to be performed on close. One of:                                                  |
|                |                     |                                                                                           |
|                |                     | - `CloseOptions.DO_NOT_SAVE_CHANGES`: Close without saving.                               |
|                |                     | - `CloseOptions.PROMPT_TO_SAVE_CHANGES`: Prompt for whether to save changes before close. |
|                |                     | - `CloseOptions.SAVE_CHANGES`: Save automatically on close.                               |
+----------------+---------------------+-------------------------------------------------------------------------------------------+

#### Returns

Boolean. `true` on success. `false` if the file has not been previously saved, the user is prompted, and the user cancels the save.

---

### Project.consolidateFootage()

`app.project.consolidateFootage()`

#### Description

Consolidates all footage in the project. Same as the File > Consolidate All Footage command.

#### Parameters

None.

#### Returns

Integer; the total number of footage items removed.

---

### Project.importFile()

`app.project.importFile(importOptions)`

#### Description

Imports the file specified in the specified ImportOptions object, using the specified options. Same as the File > Import File command.

Creates and returns a new FootageItem object from the file, and adds it to the project's items array.

#### Parameters

|    Parameter    |                    Type                    |                               Description                                |
| --------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| `importOptions` | [ImportOptions](../other/importoptions.md) | Options specifying the file to import and the options for the operation. |

#### Returns

[FootageItem object](../item/footageitem.md).

#### Example

```javascript
app.project.importFile(new ImportOptions(new File("sample.psd"));
```

---

### Project.importFileWithDialog()

`app.project.importFileWithDialog()`

#### Description

Shows an Import File dialog box. Same as the File > Import > File command.

#### Returns

Array of [Item objects](../item/item.md) created during import; or `null` if the user cancels the dialog box.

---

### Project.importPlaceholder()

`app.project.importPlaceholder(name, width, height, frameRate, duration)`

#### Description

Creates and returns a new PlaceholderItem and adds it to the project's items array. Same as the File > Import > Placeholder command.

#### Parameters

|  Parameter  |                        Type                         |                 Description                 |
| ----------- | --------------------------------------------------- | ------------------------------------------- |
| `name`      | String                                              | The name of the placeholder.                |
| `width`     | Integer, in the range `[4..30000]`                  | The width of the placeholder in pixels.     |
| `height`    | Integer, in the range `[4..30000]`                  | The height of the placeholder in pixels.    |
| `frameRate` | Floating-point value, in the range `[1.0..99.0]`    | The frame rate of the placeholder.          |
| `duration`  | Floating-point value, in the range `[0.0..10800.0]` | The duration of the placeholder in seconds. |

#### Returns

PlaceholderItem object.

---

### Project.item()

`app.project.item(index)`

#### Description

Retrieves an item at a specified index position.

#### Parameters

| Parameter |  Type   |                          Description                          |
| --------- | ------- | ------------------------------------------------------------- |
| `index`   | Integer | The index position of the item. The first item is at index 1. |

#### Returns

[Item object](../item/item.md).

---

### Project.itemByID()

`app.project.itemByID(id)`

!!! note
    This functionality was added in After Effects 13.0 (CC 2014)

#### Description

Retrieves an item by its [Item ID](../item/item.md#itemid)

#### Parameters

| Parameter |  Type   |    Description    |
| --------- | ------- | ----------------- |
| `id`      | Integer | The ID of an item |

#### Returns

[Item object](../item/item.md).

---

### Project.layerByID()

`app.project.layerByID(id)`

!!! note
    This functionality was added in After Effects 22.0 (2022)

#### Description

Instance method on Project which, when given a valid ID value, returns the Layer object in the Project with that given ID.

#### Parameters

| Parameter |          Type          |                      Description                      |
| --------- | ---------------------- | ----------------------------------------------------- |
| `id`      | Integer (non-negative) | The ID of the Layer to be retrieved from the Project. |

#### Returns

[Layer object](../layer/layer.md) with the given ID if it exists on the project; otherwise null. Non-valid IDs will throw an exception stating that the input parameter is not an unsigned integer.

#### Example

```javascript
var firstComp = app.project.item(1);
var firstLayer = firstComp.layer(1);
var layerID = firstLayer.id;

if (app.project.layerByID(layerID) === firstLayer) {
    alert("You can get the Layer from the ID!");
}
```

---

### Project.listColorProfiles()

`app.project.listColorProfiles()`

#### Description

Returns an array of color profile descriptions that can be set as the project's color working space.

#### Parameters

None.

#### Returns

Array of strings.

---

### Project.reduceProject()

`app.project.reduceProject(array_of_items)`

#### Description

Removes all items from the project except those specified. Same as the File > Reduce Project command.

#### Parameters

|    Parameter     |                   Type                   |      Description      |
| ---------------- | ---------------------------------------- | --------------------- |
| `array_of_items` | Array of [Item objects](../item/item.md) | The items to be kept. |

#### Returns

Integer; the total number of items removed.

#### Example

```javascript
var items = [];
items[items.length] = app.project.item(1);
items[items.length] = app.project.item(3);
app.project.reduceProject(items);
```

---

### Project.removeUnusedFootage()

`app.project.removeUnusedFootage()`

#### Description

Removes unused footage from the project. Same as the File > Remove Unused Footage command.

#### Parameters

None.

#### Returns

Integer; the total number of FootageItem objects removed.

---

### Project.replaceFont()

`app.project.replaceFont(fromFont, toFont, [noFontLocking = false])`

!!! note
    This functionality was added in After Effects 24.5

#### Description

This function will replace all the usages of [Font object](../text/fontobject.md) `fromFont` with [Font object](../text/fontobject.md) `toFont`.

This operation exposes the same mechanism and policy used for automatic font replacement of missing or substituted fonts and is therefore a complete and precise replacement, even on [TextDocuments](../text/textdocument.md) which have mixed styling, preserving the character range the `fromFont` was applied to.

This operation is not undoable.

The optional parameter `noFontLocking` controls what happens when the `toFont` has no glyphs for the text it is applied to. By default a fallback font will be selected which will have the necessary glyphs, but if this parameter is set to `true` then this fallback will not take place and missing glyphs will result. There is no way at the current time to detect or report this.

Note that when `fromFont` is a substituted font and the `toFont` has the same font properties no fallback can occur and the parameter is ignored and treated as `true`.

```javascript
var fromFont = app.project.usedFonts[0].font;
var fontList = app.fonts.getFontsByPostScriptName("TimesNewRomanPSMT");
var toFont = fontList[0];
var layerChanged = app.project.replaceFont(fromFont, toFont);
```

#### Parameters

|    Parameter    |                 Type                 |          Description          |
| --------------- | ------------------------------------ | ----------------------------- |
| `fromFont`      | [Font object](../text/fontobject.md) | Font to be replaced.          |
| `toFont`        | [Font object](../text/fontobject.md) | Font to replace it with.      |
| `noFontLocking` | Boolean                              | Optional. Defaults to `false` |

#### Returns

Boolean. `true` if at least one Layer was changed.

---

### Project.save()

`app.project.save([file])`

#### Description

Saves the project. The same as the File > Save or File > Save As command. If the project has never previously been saved and no file is specified, prompts the user for a location and file name.

Pass a [File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object to save a project to a new file without prompting.

#### Parameters

| Parameter |                                              Type                                              |         Description         |
| --------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| `file`    | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) | Optional. The file to save. |

#### Returns

None.

---

### Project.saveWithDialog()

`app.project.saveWithDialog()`

#### Description

Shows the Save dialog box. The user can name a file with a location and save the project, or click Cancel to exit the dialog box.

#### Parameters

None.

#### Returns

Boolean; `true` if the project was saved.

---

### Project.setDefaultImportFolder()

`app.project.setDefaultImportFolder(folder)`

#### Description

Sets the folder that will be shown in the file import dialog. This location will be used as an override until setDefaultImportFolder() is called with no parameters, or until After Effects is quit.

#### Parameters

| Parameter |                                                Type                                                |       Description        |
| --------- | -------------------------------------------------------------------------------------------------- | ------------------------ |
| `folder`  | [Extendscript Folder](https://extendscript.docsforadobe.dev/file-system-access/folder-object.html) | Folder to set as default |

#### Returns

Boolean; indicates if the operation was successful.

#### Examples

Any of the following will set the default import folder to C:/My Folder:

* `var myFolder = new Folder("C:/My Folder"); app.project.setDefaultImportFolder(myFolder);`
* `app.project.setDefaultImportFolder(new Folder("C:/My Folder"));`
* `app.project.setDefaultImportFolder(Folder("C:/My Folder"));`

Note: if the path refers to an existing file and not a folder, the Folder function returns a File object instead of a Folder object, which will cause `setDefaultImportFolder()` to return `false`.

To set the default import folder to the current user's desktop folder: `app.project.setDefaultImportFolder(Folder.desktop);`

To disable the default folder, call `setDefaultImportFolder()` with no parameters: `app.project.setDefaultImportFolder();`

---

### Project.showWindow()

`app.project.showWindow(doShow)`

#### Description

Shows or hides the Project panel.

#### Parameters

| Parameter |  Type   |                                Description                                 |
| --------- | ------- | -------------------------------------------------------------------------- |
| `doShow`  | Boolean | When `true`, show the Project panel. When `false`, hide the Project panel. |

#### Returns

Nothing.

---

## Team Projects

### Project.newTeamProject()

`app.project.newTeamProject(teamProjectName, description)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Creates a new team project.

#### Parameters

|     Parameter     |  Type  |          Description          |
| ----------------- | ------ | ----------------------------- |
| `teamProjectName` | String | Team project name             |
| `description`     | String | Optional. Project description |

#### Returns

Boolean. `true` if the team project is successfully created, otherwise `false`.

---

### Project.openTeamProject()

`app.project.openTeamProject(teamProjectName)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Opens a team project.

#### Parameters

|     Parameter     |  Type  |    Description    |
| ----------------- | ------ | ----------------- |
| `teamProjectName` | String | Team project name |

#### Returns

Boolean. `true` if the team project is successfully opened, otherwise `false`.

---

### Project.shareTeamProject()

`app.project.shareTeamProject(comment)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Shares the currently open team project.

#### Parameters

| Parameter |  Type  |    Description     |
| --------- | ------ | ------------------ |
| `comment` | String | Optional. Comment. |

#### Returns

Boolean. `true` if the team project is successfully shared, otherwise `false`.

---

### Project.syncTeamProject()

`app.project.syncTeamProject()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Syncs the currently open team project.

#### Returns

Boolean. `true` if the team project is successfully synced, otherwise `false`.

---

### Project.closeTeamProject()

`app.project.closeTeamProject()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Closes a currently open team project.

#### Returns

Boolean. `true` if the team project is successfully closed, otherwise `false`.

---

### Project.convertTeamProjectToProject()

`app.project.convertTeamProjectToProject(project_file)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Converts a team project to an After Effects project on a local disk.

#### Parameters

|   Parameter    |                                              Type                                              |                                               Description                                               |
| -------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `project_file` | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) | The local After Effects project. File extension should be either .aep or .aet (.aepx is not supported). |

#### Returns

Boolean. `true` if the team project is successfully converted, otherwise `false`.

---

### Project.listTeamProjects()

`app.project.listTeamProjects()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Returns an array containing the name strings for all team projects available for the current user.
Archived Team Projects are not included.

#### Returns

Array of strings.

---

### Project.isTeamProjectOpen()

`app.project.isTeamProjectOpen(teamProjectName)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether specified team project is currently open.

#### Parameters

|     Parameter     |  Type  |    Description    |
| ----------------- | ------ | ----------------- |
| `teamProjectName` | String | Team project name |

#### Returns

Boolean. `true` if the specified team project is currently open, otherwise `false`.

---

### Project.isAnyTeamProjectOpen()

`app.project.isAnyTeamProjectOpen()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether any team project is currently open.

#### Returns

Boolean. `true` if any team project is currently open, otherwise `false`.

---

### Project.isTeamProjectEnabled()

`app.project.isTeamProjectEnabled()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether or not team project is enabled for After Effects. (This will almost always return `true`.)

#### Returns

Boolean. `true` if team project is currently enabled, otherwise `false`.

---

### Project.isLoggedInToTeamProject()

`app.project.isLoggedInToTeamProject()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether or not the client (After Effects) is currently logged into the team project server.

#### Returns

Boolean. `true` if the client (After Effects) is currently logged into the team projects server, otherwise `false`.

---

### Project.isSyncCommandEnabled()

`app.project.isSyncCommandEnabled()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether or not the Sync command is enabled.

#### Returns

Boolean. `true` if the team projects Sync command is enabled, otherwise `false`.

---

### Project.isShareCommandEnabled()

`app.project.isShareCommandEnabled()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether or not the Share command is enabled.

#### Returns

Boolean. `true` if the team projects Share command is enabled, otherwise `false`.

---

### Project.isResolveCommandEnabled()

`app.project.isResolveCommandEnabled()`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Checks whether or not the Resolve command is enabled.

#### Returns

Boolean. `true` if the team projects Resolve command is enabled, otherwise `false`.

---

### Project.resolveConflict()

`app.project.resolveConflict(ResolveType)`

!!! note
    This functionality was added in After Effects 14.2 (CC 2017.1)

#### Description

Resolves a conflict between the open team project and the version on the team projects server, using the specified resolution method.

#### Parameters

+---------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |        Type        |                                                                      Description                                                                       |
+===============+====================+========================================================================================================================================================+
| `ResolveType` | `ResolveType` enum | The type of conflict resolution to use. One of:                                                                                                        |
|               |                    |                                                                                                                                                        |
|               |                    | - `ResolveType.ACCEPT_THEIRS`: Take the shared version. The shared version replaces your version.                                                      |
|               |                    | - `ResolveType.ACCEPT_YOURS`: Keep your version of the project. The shared version is not taken.                                                       |
|               |                    | - `ResolveType.ACCEPT_THEIRS_AND_COPY`: Copy and rename your version, then take the shared version. The shared version replaces your original version. |
+---------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Boolean. `true` if the resolution of the specified type was successful, otherwise `false`.
