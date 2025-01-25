# AVItem object

`app.project.item(index)`

#### Description

The AVItem object provides access to attributes and methods of audio/visual files imported into After Effects.

!!! info
    AVItem is a subclass of Item. All methods and attributes of Item, in addition to those listed below, are available when working with AVItem. See [Item object](item.md)

!!! info
    AVItem is the base class for both CompItem and FootageItem, so AVItem attributes and methods are also available when working with CompItem and FootageItem objects. See [CompItem object](compitem.md) and [FootageItem object](footageitem.md).

!!! warning
    CompItems and FootageItems, while logical descendants of AVItem, are not *really* subclasses of AVItem as AVItem doesn't exist in Extendscript, ie. attempting to check if `item instanceof AVItem` will fail because AVItem is undefined. This is also true for `Item` itself.

See [Javascript Classes](../introduction/javascript.md#javascript-classes) and [After Effects Class Hierarchy](../introduction/classhierarchy.md) for more info.

---

## Attributes

### AVItem.duration

`app.project.item(index).duration`

#### Description

Returns the duration, in seconds, of the item. Still footage items have a duration of 0.

- In a CompItem, the value is linked to the duration of the composition, and is read/write.
- In a FootageItem, the value is linked to the `duration` of the `mainSource` object, and is read-only.

#### Type

Floating-point value, in the range `[0.0..10800.0]`; read/write for a [CompItem](../item/compitem.md); otherwise, read-only.

---

### AVItem.footageMissing

`app.project.item(index).footageMissing`

#### Description

When `true`, the AVItem is a placeholder, or represents footage with a source file that cannot be found. In this case, the path of the missing source file is in the `missingFootagePath` attribute of the footage item's source-file object. See [FootageItem.mainSource](footageitem.md#footageitemmainsource) and [FileSource.missingFootagePath](../sources/filesource.md#filesourcemissingfootagepath).

#### Type

Boolean; read-only.

---

### AVItem.frameDuration

`app.project.item(index).frameDuration`

#### Description

Returns the length of a frame for this AVItem, in seconds. This is the reciprocal of `frameRate`. When set, the reciprocal is automatically set as a new `frameRate` value. This attribute returns the reciprocal of the `frameRate`, which may not be identical to a value you set, if that value is not evenly divisible into 1.0 (for example, 0.3). Due to numerical limitations, (1 / (1 / 0.3)) is close to, but not exactly, 0.3. If the AVItem is a FootageItem, this value is linked to the `mainSource`, and is read-only. To change it, set the `conformFrameRate` of the `mainSource` object. This sets both the `frameRate` and `frameDuration` of the FootageItem.

#### Type

Floating-point value, in the range `[1/99..1.0]`; read-only for a [FootageItem](../item/footageitem.md), otherwise read/write.

---

### AVItem.frameRate

`app.project.item(index).frameRate`

#### Description

The frame rate of the AVItem, in frames-per-second. This is the reciprocal of the `frameDuration` . When set, the reciprocal is automatically set as a new `frameDuration` value.

- In a CompItem, the value is linked to the `frameRate` of the composition, and is read/write.
- In a FootageItem, the value is linked to the `frameRate` of the `mainSource` object, and is read-only. To change it, set the `conformFrameRate` of the `mainSource` object. This sets both the `frameRate` and `frameDuration` of the FootageItem.

#### Type

Floating-point value, in the range `[1.0..99.0]`; read-only for a [FootageItem](../item/footageitem.md), otherwise read/write.

---

### AVItem.hasAudio

`app.project.item(index).hasAudio`

#### Description

When `true`, the AVItem has an audio component.

- In a CompItem, the value is linked to the composition.
- In a FootageItem, the value is linked to the `mainSource` object.

#### Type

Boolean; read-only.

---

### AVItem.hasVideo

`app.project.item(index).hasVideo`

#### Description

When `true`, the AVItem has a video component.

- In a CompItem, the value is linked to the composition.
- In a FootageItem, the value is linked to the `mainSource` object.

#### Type

Boolean; read-only.

---

### AVItem.height

`app.project.item(index).height`

#### Description

The height of the item in pixels.

- In a CompItem, the value is linked to the composition, and is read/write.
- In a FootageItem, the value is linked to the `mainSource` object, and is read/write only if the `mainSource` object is a SolidSource. Otherwise, it is read-only.

#### Type

Integer, in the range `[1..30000]`; read/write, except as noted.

---

### AVItem.isMediaReplacementCompatible

`app.project.item(index).isMediaReplacementCompatible`

!!! note
    This functionality was added in After Effects 18.0 (2021)

#### Description

Test whether the AVItem can be used as an alternate source when calling [Property.setAlternateSource()](../property/property.md#propertysetalternatesource).

Returns `true` if the item can be used, or otherwise `false`.

A CompItem or a FootageItem can be used as an alternate source for the layer, with some restrictions:

- If the AVItem is a [FootageItem object](footageitem.md), then FootageItem.FootageSource should not be a [SolidSource object](../sources/solidsource.md).
- If the AVItem is a [FootageItem object](footageitem.md) and the FootageItem.FootageSource is a [FileSource object](../sources/filesource.md) then that FileSource should not point to a non-media file e.g. a JSX script file.
- Setting the AVItem cannot create a cyclical reference within the project.

#### Type

Boolean; read only.

---

### AVItem.name

`app.project.item(index).name`

#### Description

The name of the item, as shown in the Project panel.

- In a FootageItem, the value is linked to the `mainSource` object. If the `mainSource` object is a `FileSource`, this value controls the display name in the Project panel, but does not affect the file name.

#### Type

String; read/write.

---

### AVItem.pixelAspect

`app.project.item(index).pixelAspect`

#### Description

The pixel aspect ratio (PAR) of the item.

- In a CompItem, the value is linked to the composition.
- In a FootageItem, the value is linked to the mainSource object.

The value you retrieve after setting may be slightly different from the value you supplied. The following table compares the value as it appears in the UI with the more accurate value returned by this attribute.

| PAR in the After Effects UI | PAR returned by the pixelAspect attribute |
| --------------------------- | ----------------------------------------- |
| 0.91                        | 0.909091                                  |
| 1                           | 1                                         |
| 1.5                         | 1.5                                       |
| 1.09                        | 1.09402                                   |
| 1.21                        | 1.21212                                   |
| 1.33                        | 1.33333                                   |
| 1.46                        | 1.45869                                   |
| 2                           | 2                                         |

#### Type

Floating-point value, in the range `[0.01..100.0]`; read/write.

---

### AVItem.proxySource

`app.project.item(index).proxySource`

#### Description

The FootageSource being used as a proxy. The attribute is read-only; to change it, call any of the AVItem methods that change the proxy source: `setProxy()`, `setProxyWithSequence()`, `setProxyWithSolid()`, or `setProxyWithPlaceholder()`.

#### Type
`FootageSource` object; read-only.

---

### AVItem.time

`app.project.item(index).time`

#### Description

The current time of the item when it is being previewed directly from the Project panel. This value is a number of seconds. Use the global method [timeToCurrentFormat()](../general/globals.md#timetocurrentformat) to convert it to a string value that expresses the time in terms of frames. It is an error to set this value for a FootageItem whose `mainSource` is still (`item.mainSource.isStill` is `true`).

#### Type

Floating-point value; read/write.

---

### AVItem.usedIn

`app.project.item(index).usedIn`

#### Description

All the compositions that use this AVItem. Note that upon retrieval, the array value is copied, so it is not automatically updated. If you get this value, then add this item into another composition, you must retrieve the value again to get an array that includes the new item.

#### Type

Array of CompItem objects; read-only.

---

### AVItem.useProxy

`app.project.item(index).useProxy`

#### Description

When `true`, a proxy is used for the item. It is set to `true` by all the `SetProxy` methods, and to `false` by the `SetProxyToNone()` method.

#### Type

Boolean; read/write.

---

### AVItem.width

`app.project.item(index).width`

#### Description

The width of the item, in pixels.

- In a CompItem, the value is linked to the composition, and is read/write.
- In a FootageItem, the value is linked to the `mainSource` object, and is read/write only if the `mainSource` object is a SolidSource. Otherwise, it is read-only.

#### Type

Integer, in the range `[1..30000]`; read/write, except as noted.

---

## Methods

### AVItem.setProxy()

`app.project.item(index).setProxy(file)`

#### Description

Sets a file as the proxy of this AVItem.

Loads the specified file into a new FileSource object, sets this as the value of the `proxySource` attribute, and sets `useProxy` to `true`.

It does not preserve the interpretation parameters, instead using the user preferences. If the file has an unlabeled alpha channel, and the user preference says to ask the user what to do, the method estimates the alpha interpretation, rather than asking the user.

This differs from setting a FootageItem's `mainSource`, but both actions are performed as in the user interface.

#### Parameters

| Parameter |                                                 Type                                                  |           Description           |
| --------- | ----------------------------------------------------------------------------------------------------- | ------------------------------- |
| `file`    | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object | The file to be used as a proxy. |

#### Returns

None.

---

### AVItem.setProxyToNone()

`app.project.item(index).setProxyToNone()`

#### Description

Removes the proxy from this AVItem, sets the value of `proxySource` to `null`, and sets the value of `useProxy` to `false`.

#### Parameters

None.

#### Returns

Nothing.

---

### AVItem.setProxyWithPlaceholder()

`app.project.item(index).setProxyWithPlaceholder(name, width, height ,frameRate, duration)`

#### Description

Creates a PlaceholderSource object with specified values, sets this as the value of the `proxySource` attribute, and sets `useProxy` to `true`. It does not preserve the interpretation parameters, instead using the user preferences.

!!! note
    There is no direct way to set a placeholder as a proxy in the user interface; this behavior occurs when a proxy has been set and then moved or deleted.

#### Parameters

|  Parameter  |                  Type                  |                 Description                 |
| ----------- | -------------------------------------- | ------------------------------------------- |
| `name`      | String                                 | The name of the new object.                 |
| `width`     | Integer, in the range `[4..30000]`     | The pixel dimensions of the placeholder.    |
| `height`    | Integer, in the range `[4..30000]`     | The pixel dimensions of the placeholder.    |
| `frameRate` | Integer, in the range `[1..99]`        | Frame rate for the proxy.                   |
| `duration`  | Integer, in the range `[0.0..10800.0]` | The total length in seconds, up to 3 hours. |

#### Returns

Nothing.

---

### AVItem.setProxyWithSequence()

`app.project.item(index).setProxyWithSequence(file,forceAlphabetical)`

#### Description

Sets a sequence of files as the proxy of this AVItem, with the option of forcing alphabetical order.
Loads the specified file sequence into a new FileSource object, sets this as the value of the `proxySource` attribute, and sets `useProxy` to `true`.

It does not preserve the interpretation parameters, instead using the user preferences.
If any file has an unlabeled alpha channel, and the user preference says to ask the user what to do, the method estimates the alpha interpretation, rather than asking the user.

#### Parameters

|      Parameter      |                                                 Type                                                  |                       Description                       |
| ------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `file`              | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object | The first file in the sequence.                         |
| `forceAlphabetical` | Boolean                                                                                               | When `true`, use the "Force alphabetical order" option. |

#### Returns

Nothing.

---

### AVItem.setProxyWithSolid()

`app.project.item(index).setProxyWithSolid(color, name, width, height, pixelAspect)`

#### Description

Creates a [SolidSource object](../sources/solidsource.md) with specified values, sets this as the value of the `proxySource` attribute, and sets `useProxy` to `true`. It does not preserve the interpretation parameters, instead using the user preferences.

!!! note
    There is no way, using the user interface, to set a solid as a proxy; this feature is available only through scripting.

#### Parameters

|     Parameter     |                                     Type                                      |               Description                |
| ----------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| `color`           | Array of three floating-point values, `[R, G, B]`, in the range `[0.0..1.0]`. | The color of the solid.                  |
| `name`            | String                                                                        | The name of the new object.              |
| `width`, `height` | Integer, in the range `[1..30000]`                                            | The pixel dimensions of the placeholder. |
| `pixelAspect`     | Floating-point value, in the range `[0.01..100.0]`                            | The pixel aspect ratio of the solid.     |

#### Returns

Nothing.
