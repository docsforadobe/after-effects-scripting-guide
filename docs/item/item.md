# Item object

`app.project.item(index)`

`app.project.items[index]`


#### Description

The Item object represents an item that can appear in the Project panel. The first item is at index 1.

!!! info
    Item is the base class for [AVItem object](avitem.md) and for [FolderItem object](folderitem.md), which are in turn the base classes for various other item types, so Item attributes and methods are available when working with all of these item types.

#### Example

This example gets the second item from the project and checks that it is a folder. It then removes from the folder any top-level item that is not currently selected. It also checks to make sure that, for each item in the folder, the parent is properly set to the correct folder.

```javascript
var myFolder = app.project.item(2);
if (!(myFolder instanceof FolderItem)) {
    alert("error: second item is not a folder");
} else {
    var numInFolder = myFolder.numItems;
    //Always run loops backwards when deleting things:
    for (var i = numInFolder; i >= 1; i--) {
        var curItem = myFolder.item(i);
        if (curItem.parentFolder !== myFolder) {
            alert("error within AE: the parentFolder is not set correctly");
        } else {
            if (!curItem.selected) {
                //found an unselected solid.
                curItem.remove();
            }
        }
    }
}
```

---

## Attributes

### Item.comment

`app.project.item(index).comment`

#### Description

A string that holds a comment, up to 15,999 bytes in length after any encoding conversion. The comment is for the user's purpose only; it has no effect on the item's appearance or behavior.

#### Type

String; read/write.

---

### Item.dynamicLinkGUID

`app.project.item(index).dynamicLinkGUID`

#### Description

A unique and persistent identification number used for the dynamic link, in form of `00000000-0000-0000-0000-000000000000`.

#### Type

String; read-only.

---

### Item.guides

`app.project.item(index).guides`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

An array of `guide` objects, containing `orientationType`, `positionType`, and `position` attributes.

#### Type

Array; read-only.

---

### Item.id

`app.project.item(index).id`

#### Description

A unique and persistent identification number used internally to identify an item between sessions. The value of the ID remains the same when the project is saved to a file and later reloaded. However, when you import this project into another project, new IDs are assigned to all items in the imported project. The ID is not displayed anywhere in the user interface.

#### Type

Integer; read-only.

---

### Item.label

`app.project.item(index).label`

#### Description

The label color for the item. Colors are represented by their number (0 for None, or 1 to 16 for one of the preset colors in the Labels preferences).

!!! tip
    Custom label colors cannot be set programmatically.

#### Type

Integer (0 to 16); read/write.

---

### Item.name

`app.project.item(index).name`

#### Description

The name of the item as displayed in the Project panel.

#### Type

String; read/write.

---

### Item.parentFolder

`app.project.item(index).parentFolder`

#### Description

The FolderItem object for the folder that contains this item. If this item is at the top level of the project, this is the project's root folder (`app.project.rootFolder`). You can use [ItemCollection.addFolder()](itemcollection.md#itemcollectionaddfolder) to add a new folder, and set this value to put items in the new folder.

#### Type

FolderItem object; read/write.

#### Example

This script creates a new FolderItem in the Project panel and moves compositions into it.

```javascript
//create a new FolderItem in project, with name "comps"
var compFolder = app.project.items.addFolder("comps");

//move all compositions into new folder by setting
//compItem's parentFolder to "comps" folder
for (var i = 1; i <= app.project.numItems; i++){
    if (app.project.item(i) instanceof CompItem) {
        app.project.item(i).parentFolder = compFolder;
    }
}
```

---

### Item.selected

`app.project.item(index).selected`

#### Description

When `true`, this item is selected. Multiple items can be selected at the same time. Set to `true` to select the item programmatically, or to `false` to deselect it.

#### Type

Boolean; read/write.

---

### Item.typeName

`app.project.item(index).typeName`

#### Description

A user-readable name for the item type; for example, "Folder", "Footage", or "Composition". These names are application locale-dependent, meaning that they are different depending on the application's interface language.

#### Type

String; read-only.

#### Localized strings

| Locale  |  Composition   |   Folder   |       Footage       |
| ------- | -------------- | ---------- | ------------------- |
| `en_US` | Composition    | Folder     | Footage             |
| `de_DE` | Komposition    | Ordner     | Footage             |
| `es_ES` | Composición    | Carpeta    | Material de archivo |
| `fr_FR` | Composition    | Dossier    | Métrage             |
| `it_IT` | Composizione   | Cartella   | Metraggio           |
| `ja_JP` | コンポジション | フォルダー | フッテージ          |
| `ko_KR` | 컴포지션       | 폴더       | 푸티지              |
| `pt_BR` | Composição     | Pasta      | Gravação            |
| `ru_ru` | Композиция     | Папка      | Видеоряд            |
| `zh_CN` | 合成           | 文件夹     | 素材                |

#### Example

```javascript
if (/Composition|Komposition|Composición|Composizione|コンポジション|컴포지션|Composição|Композиция|合成/.test(app.project.item(index).typeName)) {
    // item is a composition
} else if (/Folder|Ordner|Carpeta|Dossier|Cartella|フォルダー|폴더|Pasta|Папка|文件夹/.test(app.project.item(index).typeName)) {
    // item is a folder
}
```

---

## Methods

### Item.addGuide()

`app.project.item(index).addGuide(orientationType, position)`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

Creates a new guide and adds it to the `guides` object of the Item.

#### Parameters

|     Parameter     |  Type   |                                          Description                                          |
| ----------------- | ------- | --------------------------------------------------------------------------------------------- |
| `orientationType` | Integer | `0` for a horizontal guide, `1` for a vertical guide. Any other value defaults to horizontal. |
| `position`        | Integer | The X or Y coordinate position of the guide in pixels, depending on its `orientationType`.    |

#### Returns

Integer; the index of the newly-created guide.

#### Example

Adds a vertical guide at 500 pixels on the X axis to the `activeItem` of a project.

```javascript
app.project.activeItem.addGuide(1, 500);
```

---

### Item.remove()

`app.project.item(index).remove()`

#### Description

Deletes this item from the project and the Project panel. If the item is a FolderItem, all the items contained in the folder are also removed from the project. No files or folders are removed from the disk.

#### Parameters

None.

#### Returns

Nothing.

---

### Item.removeGuide()

`app.project.item(index).removeGuide(guideIndex)`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

Removes an existing guide. Choose the guide based on its index inside the `Item.guides` object.

#### Parameters

|  Parameter   |  Type   |              Description              |
| ------------ | ------- | ------------------------------------- |
| `guideIndex` | Integer | The index of the guide to be removed. |

#### Returns

Nothing.

#### Example

Removes the first guide in `activeItem`.

```javascript
app.project.activeItem.removeGuide(0);
```

!!! warning
    Removing a guide will cause all higher guide indexes to shift downward.

---

### Item.setGuide()

`app.project.item(index).setGuide(position,guideIndex)`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

Modifies the `position` of an existing guide. Choose the guide based on its `guideIndex` inside the `Item.guides` array.

A guide's `orientationType` may not be changed after it is created.

#### Parameters

|  Parameter   |  Type   |                                               Description                                               |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------- |
| `position`   | Integer | The new X or Y coordinate position of the guide in pixels, depending on its existing `orientationType`. |
| `guideIndex` | Integer | The index of the guide to be modified.                                                                  |

#### Returns

Nothing.

#### Example

Changes the position of the first guide in `activeItem` to 1200 pixels.

```javascript
app.project.activeItem.setGuide(1200, 0);
```
