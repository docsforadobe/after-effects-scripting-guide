# ItemCollection object

`app.project.items`

#### Description

The ItemCollection object represents a collection of [Items](../item/item.md).

The ItemCollection belonging to a [Project object](../general/project.md) contains all the Item objects for [items in the project](../general/project.md#projectitems).

The ItemCollection belonging to a [FolderItem object](../item/folderitem.md) contains all the Item objects for [items in that folder](../item/folderitem.md#folderitemitems).

!!! info
    ItemCollection is a subclass of [Collection object](../other/collection.md). All methods and attributes of Collection, in addition to those listed below, are available when working with ItemCollection.

---

## Methods

### ItemCollection.addComp()

`app.project.items.addComp(name, width, height, pixelAspect, duration, frameRate)`

#### Description

Creates and returns a new [CompItem object](../item/compitem.md) and adds it to this collection.

If the ItemCollection belongs to the project or the root folder, then the new item's [`parentFolder`](../item/item.md#itemparentfolder) is the [root folder](../general/project.md#projectrootfolder).

If the ItemCollection belongs to any other folder, the new item's `parentFolder` is that [FolderItem](../item/folderitem.md).

#### Parameters

|   Parameter   |                        Type                         |                 Description                 |
| ------------- | --------------------------------------------------- | ------------------------------------------- |
| `name`        | String                                              | The name of the composition.                |
| `width`       | Integer, in the range `[4..30000]`                  | The width of the composition in pixels.     |
| `height`      | Integer, in the range `[4..30000]`                  | The height of the composition in pixels.    |
| `pixelAspect` | Floating-point value, in the range `[0.01..100.0]`  | The pixel aspect ratio of the composition.  |
| `duration`    | Floating-point value, in the range `[0.0..10800.0]` | The duration of the composition in seconds. |
| `frameRate`   | Floating-point value, in the range `[1.0..99.0]`    | The frame rate of the composition.          |

#### Returns

[CompItem object](../item/compitem.md)

---

### ItemCollection.addFolder()

`app.project.items.addFolder(name)`

#### Description

Creates and returns a new [FolderItem object](../item/folderitem.md) and adds it to this collection.

If the ItemCollection belongs to the [project](../general/project.md#projectitems) or the [root folder](../general/project.md#projectrootfolder), then the new folder's `parentFolder` is the root folder.

If the ItemCollection belongs to any other folder, the new folder's `parentFolder` is that FolderItem. To put items in the folder, set the [Item.parentFolder](item.md#itemparentfolder) attribute.

#### Parameters

| Parameter |  Type  |       Description       |
| --------- | ------ | ----------------------- |
| `name`    | String | The name of the folder. |

#### Returns

[FolderItem object](../item/folderitem.md).

#### Example

This script creates a new [FolderItem](../item/folderitem.md) in the Project panel and moves compositions into it.

```javascript
//create a new FolderItem in project, with name "comps"
var compFolder = app.project.items.addFolder("comps");
//move all compositions into new folder by setting
//comp Item's parentFolder to "comps" folder
for (var i = 1; i <= app.project.numItems; i++) {
    if (app.project.item(i) instanceof CompItem) {
        app.project.item(i).parentFolder = compFolder;
    }
}
```
