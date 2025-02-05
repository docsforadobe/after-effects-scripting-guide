# ImportOptions object

`new ImportOptions();`

`new ImportOptions(file);`


#### Description

The ImportOptions object encapsulates the options used to import a file with the [Project.importFile()](../general/project.md#projectimportfile) methods.

The constructor takes an optional parameter, an [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the file.

If it is not supplied, you must explicitly set the value of the `file` attribute before using the object with the `importFile` method. For example:

```javascript
new ImportOptions().file = new File("myfile.psd");
```

---

## Attributes

### ImportOptions.file

`importOptions.file`

#### Description

The file to be imported. If a file is set in the constructor, you can access it through this attribute.

#### Type

[Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object; read/write.

---

### ImportOptions.forceAlphabetical

`importOptions.forceAlphabetical`

#### Description

When `true`, has the same effect as setting the "Force alphabetical order" option in the File > Import > File dialog box.

#### Type

Boolean; read/write.

---

### ImportOptions.importAs

`importOptions.importAs`

#### Description

The type of object for which the imported file is to be the source. Before setting, use [canImportAs](#importoptionscanimportas) to check that a given file can be imported as the source of the given object type.

#### Type

An `ImportAsType` enumerated value; read/write. One of:

- `ImportAsType.COMP_CROPPED_LAYERS`
- `ImportAsType.FOOTAGE`
- `ImportAsType.COMP`
- `ImportAsType.PROJECT`

---

### ImportOptions.rangeEnd

`importOptions.rangeEnd`

!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

#### Description

Sets the end clipping range of the sequence, that is going to be imported.

- Creates 'missing frames' (video-bards) if the `rangeEnd` exceeds the duration of the sequence to be imported.
- Has no effect if [sequence](#importoptionssequence) is set to `false`.
- Throws an exception if [forceAlphabetical](#importoptionsforcealphabetical) is set to `true`.
- Throws an exception if `rangeEnd` is less then [rangeStart](#importoptionsrangestart) and resets the range to include all the files.

#### Type

Integer; read/write.

---

### ImportOptions.rangeStart

`importOptions.rangeStart`

!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

#### Description

Sets the start clipping range of the sequence, that is going to be imported.

- Has no effect if [sequence](#importoptionssequence) is set to `false`.
- Throws an exception if [forceAlphabetical](#importoptionsforcealphabetical) is set to `true`.
- Throws an exception if [rangeEnd](#importoptionsrangeend) value is 0.
- Throws an exception if `rangeStart` is greater then [rangeEnd](#importoptionsrangeend) and resets the range to include all the files.

#### Type

Integer; read/write.

#### Example

```javascript
/*
    Import 20 frames of the sequence, starting at frame 10 and ending at frame 30
 */
var mySequence = '~/Desktop/sequence/image_000.png';

var importOptions = new ImportOptions();
importOptions.file = new File(mySequence);
importOptions.sequence = true;
importOptions.forceAlphabetical = false;
importOptions.rangeStart = 10;
importOptions.rangeEnd = 30;

var item = app.project.importFile(importOptions);
```

---

### ImportOptions.sequence

`importOptions.sequence`

#### Description

When `true`, a sequence is imported; otherwise, an individual file is imported.

#### Type

Boolean; read/write.

---

## Methods

### ImportOptions.canImportAs()

`importOptions.canImportAs(type)`

#### Description

Reports whether the file can be imported as the source of a particular object type. If this method returns `true`, you can set the given type as the value of the [importAs](#importoptionsimportas) attribute.

#### Parameters

+-----------+----------------------+------------------------------------------------+
| Parameter |         Type         |                  Description                   |
+===========+======================+================================================+
| `type`    | `ImportAsType` enum. | The type of file that can be imported. One of: |
|           |                      |                                                |
|           |                      | - `ImportAsType.COMP`                          |
|           |                      | - `ImportAsType.FOOTAGE`                       |
|           |                      | - `ImportAsType.COMP_CROPPED_LAYERS`           |
|           |                      | - `ImportAsType.PROJECT`                       |
+-----------+----------------------+------------------------------------------------+

#### Returns

Boolean.

#### Example

```javascript
var io = new ImportOptions(new File("c:\\myFile.psd"));
if (io.canImportAs(ImportAsType.COMP)) {
    io.importAs = ImportAsType.COMP;
}
```

---

### ImportOptions.isFileNameNumbered()

`importOptions.isFileNameNumbered(file)`

!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

#### Description

Reports whether the file object is numbered, i.e. file name has a digit.

#### Parameters

| Parameter |                                                 Type                                                  |    Description    |
| --------- | ----------------------------------------------------------------------------------------------------- | ----------------- |
| `file`    | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object | The file to check |

#### Returns

Object, containing 2 keys:

- `isNumbered`: Boolean; wether the file name contains any digit,
- `num`: Integer; a number found in file name. Returns 0 when `isNumbered` is `false`.

#### Example

```javascript
var importOptions = new ImportOptions();
importOptions.isFileNameNumbered('image.png');     // "isNumbered": false, "num": 0
importOptions.isFileNameNumbered('003image.png');  // "isNumbered": true, "num": 3
importOptions.isFileNameNumbered('ima0102ge.png'); // "isNumbered": true, "num": 102
importOptions.isFileNameNumbered('image0120.png'); // "isNumbered": true, "num": 120
```
