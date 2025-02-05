# LayerCollection object

`app.project.item(index).layers`

#### Description

The LayerCollection object represents a set of layers. The LayerCollection belonging to a [CompItem object](../item/compitem.md) contains all the layer objects for layers in the composition. The methods of the collection object allow you to manipulate the layer list.

!!! info
    LayerCollection is a subclass of [Collection object](../other/collection.md). All methods and attributes of Collection, in addition to those listed below, are available when working with LayerCollection.

#### Example

Given that the first item in the project is a CompItem and the second item is an AVItem, this example shows the number of layers in the CompItem's layer collection, adds a new layer based on an AVItem in the project, then displays the new number of layers.

```javascript
var firstComp = app.project.item(1);
var layerCollection = firstComp.layers;
alert("number of layers before is " + layerCollection.length);
var anAVItem = app.project.item(2);
layerCollection.add(anAVItem);
alert("number of layers after is " + layerCollection.length);
```

---

## Methods

### LayerCollection.add()

`app.project.item(index).layers.add(item[, duration])`

#### Description

Creates a new [AVLayer object](avlayer.md) containing the specified item, and adds it to this collection. The new layer honors the "Create Layers at Composition Start Time" preference. This method generates an exception if the item cannot be added as a layer to this CompItem.

#### Parameters

+------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter  |                Type                |                                                                                                                                Description                                                                                                                                |
+============+====================================+===========================================================================================================================================================================================================================================================================+
| `item`     | [AVItem object](../item/avitem.md) | The item to be added.                                                                                                                                                                                                                                                     |
+------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `duration` | Floating-point value               | Optional. The length of a still layer in seconds. Used only if the item contains a piece of still footage. Has no effect on movies, sequences or audio.                                                                                                                   |
|            |                                    |                                                                                                                                                                                                                                                                           |
|            |                                    | If supplied, sets the duration value of the new layer. Otherwise, the duration value is set according to user preferences.                                                                                                                                                |
|            |                                    |                                                                                                                                                                                                                                                                           |
|            |                                    | By default, this is the same as the duration of the containing [CompItem](../item/compitem.md). To set another preferred value, open `Edit > Preferences > Import` (Windows) or `After Effects > Preferences > Import` (Mac OS), and specify options under Still Footage. |
+------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

[AVLayer object](avlayer.md);

---

### LayerCollection.addBoxText()

`app.project.item(index).layers.addBoxText([width, height])`

#### Description

Creates a new paragraph (box) text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocumentlineorientation) set to `LineOrientation.HORIZONTAL` and adds the new [TextLayer object](textlayer.md) to this collection. To create a point text layer, use the [LayerCollection.addText()](#layercollectionaddtext) method.

#### Parameters

|     Parameter     |              Type              |             Description             |
| ----------------- | ------------------------------ | ----------------------------------- |
| `[width, height]` | Array of floating-point values | The dimensions of the new text box. |

#### Returns

TextLayer object.

---

### LayerCollection.addCamera()

`app.project.item(index).layers.addCamera(name, centerPoint)`

#### Description

Creates a new camera layer and adds the [CameraLayer object](cameralayer.md) to this collection. The new layer honors the "Create Layers at Composition Start Time" preference.

#### Parameters

|   Parameter   |                   Type                   |                                             Description                                             |
| ------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `name`        | String                                   | The name of the new layer.                                                                          |
| `centerPoint` | Array of floating-point values, `[x, y]` | The initial X and Y values of the new camera's Point of Interest property. The z value is set to 0. |

#### Returns

[CameraLayer object](cameralayer.md).

---

### LayerCollection.addLight()

`app.project.item(index).layers.addLight(name, centerPoint)`

#### Description

Creates a new light layer and adds the [LightLayer object](lightlayer.md) to this collection. The new layer honors the "Create Layers at Composition Start Time" preference.

#### Parameters

|   Parameter   |                   Type                   |         Description         |
| ------------- | ---------------------------------------- | --------------------------- |
| `name`        | String                                   | The name of the new layer.  |
| `centerPoint` | Array of floating-point values, `[x, y]` | The center of the new light |

#### Returns

[LightLayer object](lightlayer.md).

---

### LayerCollection.addNull()

`app.project.item(index).layers.addNull([duration])`

#### Description

Creates a new null layer and adds the [AVLayer object](avlayer.md) to this collection. This is the same as choosing Layer > New > Null Object.

#### Parameters

+------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter  |         Type         |                                                                                                                                Description                                                                                                                                |
+============+======================+===========================================================================================================================================================================================================================================================================+
| `duration` | Floating-point value | Optional. The length of a still layer in seconds. If supplied, sets the `duration` value of the new layer. Otherwise, the `duration` value is set according to user preferences.                                                                                          |
|            |                      |                                                                                                                                                                                                                                                                           |
|            |                      | By default, this is the same as the duration of the containing [CompItem](../item/compitem.md). To set another preferred value, open `Edit > Preferences > Import (Windows)` or `After Effects > Preferences > Import (Mac OS)`, and specify options under Still Footage. |
+------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

[AVLayer object](avlayer.md).

---

### LayerCollection.addShape()

`app.project.item(index).layers.addShape()`

#### Description

Creates a new [ShapeLayer object](shapelayer.md) for a new, empty Shape layer. Use the ShapeLayer object to add properties, such as shape, fill, stroke, and path filters. This is the same as using a shape tool in "Tool Creates Shape" mode. Tools automatically add a vector group that includes Fill and Stroke as specified in the tool options.

#### Parameters

None.

#### Returns

ShapeLayer object.

---

### LayerCollection.addSolid()

`app.project.item(index).layers.addSolid(color, name, width, height, pixelAspect[, duration])`

#### Description

Creates a new [SolidSource object](../sources/solidsource.md), with values set as specified; sets the new SolidSource as the `mainSource` value of a new [FootageItem object](../item/footageitem.md), and adds the FootageItem to the project. Creates a new [AVLayer object](avlayer.md), sets the new Footage Item as its `source`, and adds the layer to this collection.

#### Parameters

+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |                 Type                 |                                                                                                                               Description                                                                                                                                |
+===============+======================================+==========================================================================================================================================================================================================================================================================+
| `color`       | Array of three floating-point values | The color of the solid. Three numbers, `[R, G, B]`, in the range `[0.0..1.0]`                                                                                                                                                                                            |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `name`        | String                               | The name of the solid.                                                                                                                                                                                                                                                   |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `width`       | Integer                              | The width of the solid in pixels, in the range `[4..30000]`                                                                                                                                                                                                              |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `height`      | Integer                              | The height of the solid in pixels, in the range `[4..30000]`                                                                                                                                                                                                             |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pixelAspect` | Floating-point value                 | The pixel aspect ratio of the solid, in the range `[0.01..100.0]`                                                                                                                                                                                                        |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `duration`    | Floating-point value                 | Optional. The length of a still layer in seconds. If supplied, sets the `duration` value of the new layer. Otherwise, the `duration` value is set according to user preferences.                                                                                         |
|               |                                      |                                                                                                                                                                                                                                                                          |
|               |                                      | By default, this is the same as the duration of the containing [CompItem](../item/compitem.md). To set another preferred value, open `Edit > Preferences > Import` (Windows) or `After Effects > Preferences > Import` (MacOS), and specify options under Still Footage. |
+---------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

[AVLayer object](avlayer.md).

---

### LayerCollection.addText()

`app.project.item(index).layers.addText([sourceText])`

#### Description

Creates a new point text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocumentlineorientation) set to `LineOrientation.HORIZONTAL` and adds the new [TextLayer object](textlayer.md) to this collection. To create a paragraph (box) text layer, use [LayerCollection.addBoxText()](#layercollectionaddboxtext).

#### Parameters

|  Parameter   |  Type  |                                                                 Description                                                                  |
| ------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `sourceText` | String | Optional. The source text of the new layer, or a [TextDocument object](../text/textdocument.md) containing the source text of the new layer. |

#### Returns

[TextLayer object](textlayer.md).

---

### LayerCollection.addVerticalBoxText()

`app.project.item(index).layers.addVerticalBoxText([width, height])`

!!! note
    This functionality was added in After Effects 24.2

#### Description

Creates a new paragraph (box) text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocumentlineorientation) set to `LineOrientation.VERTICAL_RIGHT_TO_LEFT` and adds the new [TextLayer object](textlayer.md) to this collection. To create a point text layer, use the [LayerCollection.addText()](#layercollectionaddtext) or [LayerCollection.addVerticalText()](#layercollectionaddverticaltext) methods.

#### Parameters

|     Parameter     |              Type              |             Description             |
| ----------------- | ------------------------------ | ----------------------------------- |
| `[width, height]` | Array of floating-point values | The dimensions of the new text box. |


#### Returns

TextLayer object.

---

### LayerCollection.addVerticalText()

`app.project.item(index).layers.addVerticalText([sourceText])`

!!! note
    This functionality was added in After Effects 24.2

#### Description

Creates a new point text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocumentlineorientation) set to `LineOrientation.VERTICAL_RIGHT_TO_LEFT` and adds the new [TextLayer object](textlayer.md) to this collection. To create a paragraph (box) text layer, use the [LayerCollection.addBoxText()](#layercollectionaddboxtext) or [LayerCollection.addVerticalBoxText()](#layercollectionaddverticalboxtext) methods.

#### Parameters

|  Parameter   |  Type  |                                                                 Description                                                                  |
| ------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `sourceText` | String | Optional. The source text of the new layer, or a [TextDocument object](../text/textdocument.md) containing the source text of the new layer. |

#### Returns

[TextLayer object](textlayer.md).

---

### LayerCollection.byName()

`app.project.item(index).layers.byName(name)`

#### Description

Returns the first (topmost) layer found in this collection with the specified name, or `null` if no layer with the given name is found.

#### Parameters

| `name` | A string containing the name. |

#### Returns

[Layer object](layer.md) or `null`.

---

### LayerCollection.precompose()

`app.project.item(index).layers.precompose(layerIndicies, name[, moveAllAttributes])`

#### Description

Creates a new [CompItem object](../item/compitem.md) and moves the specified layers into its layer collection. It removes the individual layers from this collection, and adds the new CompItem to this collection.

#### Parameters

|      Parameter      |       Type        |                                                                                                                                                                                              Description                                                                                                                                                                                              |
| ------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `layerIndices`      | Array of integers | The position indexes of the layers to be collected.                                                                                                                                                                                                                                                                                                                                                   |
| `name`              | String            | The name of the new [CompItem](../item/compitem.md) object.                                                                                                                                                                                                                                                                                                                                          |
| `moveAllAttributes` | Boolean           | Optional. When `true` (the default), retains all attributes in the new composition. This is the same as selecting the "Move all attributes into the new composition" option in the Pre-compose dialog box. You can only set this to `false` if there is just one index in the `layerIndices` array. This is the same as selecting the "Leave all attributes in" option in the Pre-compose dialog box. |

#### Returns

[CompItem object](../item/compitem.md).
