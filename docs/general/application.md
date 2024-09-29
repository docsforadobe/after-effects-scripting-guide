# Application object

`app`

**Description**

Provides access to objects and application settings within the After Effects application. The single global object is always available by its name, app.

Attributes of the Application object provide access to specific objects within After Effects. Methods of the Application object can create a project, open an existing project, control Watch Folder mode, purge memory, and quit the After Effects application. When the After Effects application quits, it closes the open project, prompting the user to save or discard changes as necessary, and creates a project file as necessary.

---

## Attributes

### app.activeViewer

`app.activeViewer`

**Description**

The Viewer object for the currently focused or active-focused viewer (Composition, Layer, or Footage) panel. Returns null if no viewers are open.

**Type**

[Viewer object](../other/viewer.md#viewer) object; read-only.

---

### app.availableGPUAccelTypes

`app.availableGPUAccelTypes`

#### NOTE
This functionality was added in After Effects 14.0 (CC 2017)

**Description**

Use this in conjunction with `app.project.gpuAccelType` to set the value for Project Settings > Video Rendering and Effects > Use.

**Type**

Array of `GpuAccelType` enums, or null if no viewers are open; read-only. One of:

- `CUDA`
- `Metal`
- `OPENCL`
- `SOFTWARE`

**Example**
The following sample code checks the current computer’s available GPU acceleration types, and sets it to Metal if available.

```javascript
// app.availableGPUAccelTypes returns GPU acceleration types available on the current system.
// You can use this to check before setting the GPU acceleration type.
var newType = GpuAccelType.METAL;

// Before trying to set, check which GPU acceleration types are available on the current system.
var canSet = false;
var currentOptions = app.availableGPUAccelTypes;
for (var op in currentOptions) {
    if (currentOptions[op] === newType) {
        canSet = true;
    }
}

if (canSet) {
    // Set the GPU acceleration type.
    app.project.gpuAccelType = newType;
} else {
    alert("Metal is not available on this OS.");
}
```

---

### app.buildName

`app.buildName`

**Description**

The name of the build of After Effects being run, used internally by Adobe for testing and troubleshooting.

**Type**

String; read-only.

---

### app.buildNumber

`app.buildNumber`

**Description**

The number of the build of After Effects being run, used internally by Adobe for testing and troubleshooting.

**Type**

Integer; read-only.

---

### app.disableRendering

`app.disableRendering`

#### NOTE
This functionality was added in After Effects 16.0 (CC 2019)

**Description**

When false (the default), rendering proceeds as normal. Set to true to disable rendering as if Caps Lock were turned on.

**Type**

Boolean; read/write.

---

### app.effects

`app.effects`

**Description**

The effects available in the application.

**Type**

Array, with each element containing the following properties; read-only:

| `displayName`   | String representing the localized display name of the<br/>effect as seen in the Effect menu.                                                                          |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `category`      | String representing the localized category label as seen<br/>in the Effect menu. This can be “” for synthetic effects<br/>that aren’t normally shown to the user.     |
| `matchName`     | String representing the internal unique name for the effect.<br/>This name does not change between versions of After Effects.<br/>Use this value to apply the effect. |
| `version`       | Effect’s internal version string.<br/>This value might be different than the version number the<br/>plug-in vendor decides to show in the effect’s about box.         |

**Example**

```javascript
var effectName = app.effects[12].displayName;
```

---

### app.exitAfterLaunchAndEval

`app.exitAfterLaunchAndEval`

**Description**

This attribute is used only when executing a script from a command line on Windows. When the application is launched from the command line, the `–r` or `–s` command line flag causes the application to run a script (from a file or from a string, respectively). If this attribute is set to true, After Effects will exit after the script is run; if it is false, the application will remain open. This attribute only has an effect when After Effects is run from the Windows command line. It has no effect in Mac OS.

**Type**

Boolean; read/write.

---

### app.exitCode

`app.exitCode`

**Description**

A numeric status code used when executing a script externally (that is, from a command line or AppleScript).

- In Windows, the value is returned on the command line when After Effects was launched on the command line (using the `afterfx` or `afterfx –m` command), and a script was specified with the `–r` or `–s` option.
- in Mac OS, the value is returned as the AppleScript `DoScript` result for each script.

In both Mac OS and Windows, the value is set to 0 (`EXIT_SUCCESS`) at the beginning of each script evaluation. In the event of an error while the script is running, the script can set this to a positive integer that indicates what error occurred.

**Type**

Integer; read/write.

**Example**

```javascript
app.exitCode = 2; // on quit, if value is 2, an error has occurred
```

---

### app.fonts

`app.fonts`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

Returns an object to navigate and retreive all the fonts currently available on your system.

**Type**

[Fonts object](../text/fontsobject.md#fontsobject); read-only.

---

### app.isoLanguage

`app.isoLanguage`

**Description**

A string indicating the locale (language and regional designations) After Effects is running.

#### NOTE
`$.locale` returns the operating system language, not the language of the After Effects application.

**Type**

String; read-only. Some common values include:

- `en_US` for English (United States)
- `de_DE` for German (Germany)
- `es_ES` for Spanish (Spain)
- `fr_FR` for French (France)
- `it_IT` for Italian (Italy)
- `ja_JP` for Japanese (Japan)
- `ko_KR` for Korean (Korea)

**Example**

```javascript
var lang = app.isoLanguage;
if (lang === "en_US") {
  alert("After Effects is running in English.");
} else if (lang === "fr_FR") {
  alert("After Effects is running in French.");
} else {
  alert("After Effects is running not in English or French.");
}
```

---

### app.isRenderEngine

`app.isRenderEngine`

**Description**

True if After Effects is running as a render engine.

**Type**

Boolean; read-only.

---

### app.isWatchFolder

`app.isWatchFolder`

**Description**

True if the Watch Folder dialog box is currently displayed and the application is currently watching a folder for rendering.

**Type**

Boolean; read-only.

---

### app.memoryInUse

`app.memoryInUse`

**Description**

The number of bytes of memory currently used by this application.

**Type**

Number; read-only.

---

### app.onError

`app.onError`

**Description**

The name of a callback function that is called when an error occurs. By creating a function and assigning it to this attribute, you can respond to errors systematically; for example, you can close and restart the application, noting the error in a log file if it occurred during rendering. See [RenderQueue.render()](../renderqueue/renderqueue.md#renderqueue-render). The callback function is passed the error string and a severity string. It should not return any value.

**Type**

A function name string, or null if no function is assigned; read/write.

**Example**

```javascript
function err(errString) {
  alert(errString) ;
}
app.onError = err;
```

---

### app.preferences

`app.preferences`

**Description**

The currently loaded AE app preferences. See [Preferences object](../other/preferences.md#preferences).

**Type**

Preferences object; read-only.

---

### app.project

`app.project`

**Description**

The project that is currently loaded. See [Project object](project.md#project).

**Type**

Project object; read-only.

---

### app.saveProjectOnCrash

`app.saveProjectOnCrash`

**Description**

When true (the default), After Effects attempts to display a dialog box that allows you to save the current project if an error causes the application to quit unexpectedly. Set to false to suppress this dialog box and quit without saving.

**Type**

Boolean; read/write.

---

### app.settings

`app.settings`

**Description**

The currently loaded settings. See [Settings object](../other/settings.md#settings).

**Type**

Settings object; read-only.

---

### app.version

`app.version`

#### NOTE
This functionality was added in After Effects 12.0 (CC)

**Description**

An alphanumeric string indicating which version of After Effects is running.

**Type**

String; read-only.

**Example**

```javascript
var ver = app.version;
alert("This machine is running version " + ver + " of AfterEffects.");
```

---

## Methods

### app.activate()

`app.activate()`

**Description**

Opens the application main window if it is minimized or iconified, and brings it to the front of the desktop.

**Parameters**

None.

**Returns**

Nothing.

---

### app.beginSuppressDialogs()

`app.beginSuppressDialogs()`

**Description**

Begins suppression of script error dialog boxes in the user interface. Use [app.endSuppressDialogs()]() to resume the display of error dialogs.

**Parameters**

None.

**Returns**

Nothing.

---

### app.beginUndoGroup()

`app.beginUndoGroup(undoString)`

**Description**

Marks the beginning of an undo group, which allows a script to logically group all of its actions as a single undoable action (for use with the Edit > Undo/Redo menu items). Use the [app.endUndoGroup()]() method to mark the end of the group.

`beginUndoGroup()` and `endUndoGroup()` pairs can be nested. Groups within groups become part of the larger group, and will undo correctly. In this case, the names of inner groups are ignored.

**Parameters**

| `undoString`   | The text that will appear for the Undo command in the<br/>Edit menu (that is, “Undo “)   |
|----------------|------------------------------------------------------------------------------------------|

**Returns**

Nothing.

---

### app.cancelTask()

`app.cancelTask(taskID)`

**Description**

Removes the specified task from the queue of tasks scheduled for delayed execution.

**Parameters**

| `taskID`   | An integer that identifies the task, as returned by<br/>[app.scheduleTask()]().   |
|------------|-----------------------------------------------------------------------------------|

**Returns**

Nothing.

---

### app.endSuppressDialogs()

`app.endSuppressDialogs(alert)`

**Description**

Ends the suppression of script error dialog boxes in the user interface. Error dialogs are displayed by default;call this method only if [app.beginSuppressDialogs()]() has previously been called.

**Parameters**

| `alert`   | Boolean;   | when true, errors that have occurred following<br/>the call to `beginSuppressDialogs()` are<br/>displayed in adialog box.   |
|-----------|------------|-----------------------------------------------------------------------------------------------------------------------------|

**Returns**

Nothing.

---

### app.endUndoGroup()

`app.endUndoGroup()`

**Description**

Marks the end of an undo group begun with the [app.beginUndoGroup()]() method. You can use this method to place an end to an undo group in the middle of a script, should you wish to use more than one undo group for a single script. If you are using only a single undo group for a given script, you do not need to use this method; in its absence at the end of a script, the system will close the undo group automatically. Calling this method without having set a `beginUndoGroup()` method yields an error.

**Parameters**

None.

**Returns**

Nothing.

---

### app.endWatchFolder()

`app.endWatchFolder()`

**Description**

Ends Watch Folder mode.

**Parameters**

None.

**Returns**

Nothing.

**See also**

- [app.watchFolder()]()
- [app.parseSwatchFile()]()
- [app.isWatchFolder]()

---

### app.executeCommand()

`app.executeCommand(id)`

**Description**

Menu Commands in the GUI application have an individual ID number, which can be used as the parameter for this method. For some functions not included in the API this is the only way to access them.

The [app.findMenuCommandId()](#app-findmenucommandid) method can be used to find the ID number for a command.

These web sites have more information and lists of the known numbers:

- [https://www.provideocoalition.com/after-effects-menu-command-ids/](https://www.provideocoalition.com/after-effects-menu-command-ids/)
- [https://hyperbrew.co/blog/after-effects-command-ids/](https://hyperbrew.co/blog/after-effects-command-ids/)

**Parameters**

| `id`   | The ID number of the command.   |
|--------|---------------------------------|

**Returns**

None.

**Example**

```javascript
// calls the Convert to Bezier Path command
app.executeCommand(4162);
```

---

### app.findMenuCommandId()

`app.findMenuCommandId(Command)`

**Description**

Menu Commands in the GUI application have an individual ID number, which can be used as a parameter for the [app.executeCommand()](#app-executecommand) command. For some functions not included in the API this is the only way to access them.

It should be noted that this method is not reliable across different language packages of AE, so you’ll likely want to find the command ID number during development and then call it directly using the number in production.

These web sites have more information and lists of the known numbers:

- [https://www.provideocoalition.com/after-effects-menu-command-ids/](https://www.provideocoalition.com/after-effects-menu-command-ids/)
- [https://hyperbrew.co/blog/after-effects-command-ids/](https://hyperbrew.co/blog/after-effects-command-ids/)

**Parameters**

| `Command`   | The text of the menu command, exactly as it is shown in the UI.   |
|-------------|-------------------------------------------------------------------|

**Returns**

Integer, the ID number of the menu command.

**Example**

```javascript
app.findMenuCommandId("Convert To Bezier Path")
```

---

### app.newProject()

`app.newProject()`

**Description**

Creates a new project in After Effects, replicating the File > New > New Project menu command. If the current project has been edited, the user is prompted to save it. If the user cancels out of the Save dialog box, the new project is not created and the method returns null. Use `app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES)` to close the current project before opening a new one. See [Project.close()](project.md#project-close)

**Parameters**

None.

**Returns**

A new Project object, or null if no new project is created.

**Example**

```javascript
app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.newProject();
```

---

### app.open()

`app.open()`
<br/>
`app.open(file)`
<br/>

**Description**

Opens a project.

**Parameters**

| `file`   | Optional   | An [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the project file to open. If not supplied, the method prompts the user to select a project file.   |
|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

A new Project object for the specified project, or null if the user cancels the Open dialog box.

**Example**

```javascript
var my_file = new File("../my_folder/my_test.aep");
if (my_file.exists) {
  var new_project = app.open(my_file);
  if (new_project) {
    alert(new_project.file.name);
  }
}
```

---

### app.openFast()

`app.openFast(file)`
<br/>

#### WARNING
This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

**Description**

Opens a project faster than `app.open()` by skipping some checks.

**Parameters**

| `file`   | An [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the project file to open.   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

A new Project object for the specified project.

**Example**

```javascript
var projectFile = new File("someFile.aep");

$.hiresTimer;
app.openFast(projectFile);
var fastEnd = $.hiresTimer / 1000;

app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);

$.hiresTimer;
app.open(projectFile);
var normalEnd = $.hiresTimer / 1000;

app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);

alert( "The difference is " + parseInt(normalEnd-fastEnd) + " ms" +
       "\n\nFast: " + fastEnd + " ms" +
       "\nNormal:" + normalEnd + " ms" );
```

---

### app.parseSwatchFile()

`app.parseSwatchFile(file)`

**Description**

Loads color swatch data from an Adobe Swatch Exchange (ASE) file.

**Parameters**

| `file`   | The file specification, an [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object.   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

The swatch data, in this format:

| `data.majorVersion`<br/>`data.minorVersion`                                          | The ASE version number.                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data.values`                                                                        | An array of Swatch Value.                                                                                                                                                                                                       |
| `SwatchValue.type`                                                                   | One of “RGB”, “CMYK”, “LAB”, “Gray”                                                                                                                                                                                             |
| `SwatchValue.r`<br/><br/>`SwatchValue.g`<br/>`SwatchValue.b`                         | When `type = "RGB"`, the color values in the<br/>range `[0.0..1.0]`.<br/>0, 0, 0 is Black.                                                                                                                                      |
| `SwatchValue.c`<br/><br/>`SwatchValue.m`<br/>`SwatchValue.y`<br/>`SwatchValue.k`     | When `type` = “CMYK”, the color values in the<br/>range  [0.0..1.0].<br/>0, 0, 0, 0 is White.                                                                                                                                   |
| `SwatchValue.L`<br/>`SwatchValue.a`<br/><br/>`SwatchValue.b`<br/>`SwatchValue.value` | When `type = "LAB"`, the color values.<br/>`L` is in the range [0.0..1.0]. `a` and `b`<br/>are in the range [-128.0..+128.0]<br/>0, 0, 0 is Black.<br/>When `type = "Gray"`, the `value` range is<br/>[0.0..1.0]. 0.0 is Black. |

---

### app.pauseWatchFolder()

`app.pauseWatchFolder(pause)`

**Description**

Pauses or resumes the search of the target watch folder for items to render.

**Parameters**

| `pause`   | True to pause, false to resume.   |
|-----------|-----------------------------------|

**Returns**

Nothing.

**See also**

- [app.isWatchFolder]()
- [app.watchFolder()]()
- [app.endWatchFolder()]()

---

### app.purge()

`app.purge(target)`

#### NOTE
This functionality was updated in After Effects 24.3 to allow the `ALL_CACHES` enumerated value to clear both the RAM and disk cache, with the ALL_MEMORY_CACHES enumerated value added to purge only the RAM.
<br/>
<br/>
In versions prior to 24.3, `ALL_CACHES` will only clear the RAM cache.
<br/>

**Description**

Purges unused data of the specified types. Replicates the Purge options in the Edit menu.

**Parameters**

| `target`   | The type of elements to purge from memory; a PurgeTarget enumerated value, one of:<br/><br/><br/>∙ `PurgeTarget.ALL_CACHES`: Purges all data that After Effects has cached to both RAM and disk cache.<br/><br/><br/>∙ `PurgeTarget.ALL_MEMORY_CACHES`: Purges all data that After Effects has cached to RAM.  *(new in 24.3)*<br/><br/><br/>∙ `PurgeTarget.UNDO_CACHES`: Purges all data saved in the undo cache.<br/><br/><br/>∙ `PurgeTarget.SNAPSHOT_CACHES`: Purges all data cached as composition/layer snapshots.<br/><br/><br/>∙ `PurgeTarget.IMAGE_CACHES`: Purges all saved image data.<br/><br/>   |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

Nothing.

---

### app.quit()

`app.quit()`

**Description**

Quits the After Effects application.

**Parameters**

None.

**Returns**

Nothing.

---

### app.scheduleTask()

`app.scheduleTask(stringToExecute, delay, repeat)`

**Description**

Schedules the specified JavaScript for delayed execution.

**Parameters**

| `stringToExecute`   | A string containing JavaScript to be executed.                                                                                                  |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `delay`             | A number of milliseconds to wait before executing<br/>the JavaScript. A floating-point value.                                                   |
| `repeat`            | When true, execute the script repeatedly, with the<br/>specified delay between each execution. When false the<br/>script is executed only once. |

**Returns**

Integer, a unique identifier for this task, which can be used to cancel it with [app.cancelTask()]().

---

### app.setMemoryUsageLimits()

`app.setMemoryUsageLimits(imageCachePercentage, maximumMemoryPercentage)`

**Description**

Sets memory usage limits as in the Memory & Cache preferences area. For both values, if installed RAM is less than a given amount (`n` gigabytes), the value is a percentage of the installed RAM, and is otherwise a percentage of `n`. The value of `n` is: 2 GB for 32-bit Windows, 4 GB for 64-bit Windows, 3.5 GB for Mac OS.

**Parameters**

| `imageCachePercentage`    | Floating-point value, the percentage of memory<br/>assigned to image cache.   |
|---------------------------|-------------------------------------------------------------------------------|
| `maximumMemoryPercentage` | Floating-point value, the maximum usable<br/>percentage of memory.            |

**Returns**

Nothing.

---

### app.setMultiFrameRenderingConfig()

`app.setMultiFrameRenderingConfig(mfr_on, max_cpu_perc)`

#### NOTE
This functionality was added in After Effects 22.0 (2022)

**Description**

Calling this function from a script will set the Multi-Frame Rendering configuration for the next render.
After execution of the script is complete, these settings will be reset to what was previously set in the UI.

**Parameters**

| `mfr_on`       | Boolean value. Set to `true` to enable Multi-Frame Rendering.                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `max_cpu_perc` | Value from 1-100 representing the maximum CPU percentage Multi-Frame Rendering should utilize. If `mfr_on` is set to `false`, pass in 100. |

**Returns**

Nothing.

---

### app.setSavePreferencesOnQuit()

`app.setSavePreferencesOnQuit(doSave)`

**Description**

Set or clears the flag that determines whether preferences are saved when the application is closed.

**Parameters**

| `doSave`   | When true, preferences saved on quit, when false they are not.   |
|------------|------------------------------------------------------------------|

**Returns**

Nothing.

---

### app.watchFolder()

`app.watchFolder(folder_object_to_watch)`

**Description**

Starts a Watch Folder (network rendering) process pointed at a specified folder.

**Parameters**

| `folder_object_to_watch`   | The [Folder](https://extendscript.docsforadobe.dev/file-system-access/folder-object.html) object for the folder to watch.   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|

**Returns**

Nothing.

**Example**

```javascript
var theFolder = new Folder("c:/tool");
app.watchFolder(theFolder);
```

**See also**

- [app.endWatchFolder()]()
- [app.parseSwatchFile()]()
- [app.isWatchFolder]()
