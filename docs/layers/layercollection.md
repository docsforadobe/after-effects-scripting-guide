<a id="layercollection"></a>

# LayerCollection object

`app.project.item(index).layers`

**Description**

The LayerCollection object represents a set of layers. The LayerCollection belonging to a [CompItem object](../items/compitem.md#compitem) contains all the layer objects for layers in the composition. The methods of the collection object allow you to manipulate the layer list.

> LayerCollection is a subclass of [Collection object](../other/collection.md#collection). All methods and attributes of Collection, in addition to those listed below, are available when working with LayerCollection.

**Example**

Given that the first item in the project is a CompItem and the second item is an AVItem, this example shows the number of layers in the CompItem’s layer collection, adds a new layer based on an AVItem in the project, then displays the new number of layers.

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

<a id="layercollection-add"></a>

### LayerCollection.add()

`app.project.item(index).layers.add(item[, duration])`

**Description**

Creates a new [AVLayer object](avlayer.md#avlayer) containing the specified item, and adds it to this collection. The new layer honors the “Create Layers at Composition Start Time” preference. This method generates an exception if the item cannot be added as a layer to this CompItem.

**Parameters**

| `item`     | The AVItem object for the item to be added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `duration` | Optional, the length of a still layer in seconds, a<br/>floating-point value. Used only if the item contains a piece of<br/>still footage. Has no effect on movies, sequences or audio. If<br/>supplied, sets the du r at i on value of the new layer.<br/>Otherwise, the duration value is set according to user<br/>preferences. By default, this is the same as the duration of the<br/>containing CompItem. To set another preferred value, choose<br/>Edit > Preferences > Import (Windows) or After Effects ><br/>Preferences > Import (Mac OS), and specify options under Still<br/>Footage. |

**Returns**

[AVLayer object](avlayer.md#avlayer);

---

<a id="layercollection-addboxtext"></a>

### LayerCollection.addBoxText()

`app.project.item(index).layers.addBoxText([width, height])`

**Description**

Creates a new paragraph (box) text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocument-lineorientation) set to `LineOrientation.HORIZONTAL` and adds the new [TextLayer object](textlayer.md#textlayer) to this collection. To create a point text layer, use the [LayerCollection.addText()](#layercollection-addtext) method.

**Parameters**

| `[width, height]`   | An Array containing the dimensions of the new text box.   |
|---------------------|-----------------------------------------------------------|

**Returns**

TextLayer object.

---

<a id="layercollection-addcamera"></a>

### LayerCollection.addCamera()

`app.project.item(index).layers.addCamera(name, centerPoint)`

**Description**

Creates a new camera layer and adds the [CameraLayer object](cameralayer.md#cameralayer) to this collection. The new layer honors the “Create Layers at Composition Start Time” preference.

**Parameters**

| `name`        | A string containing the name of the new layer.                                                                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `centerPoint` | The center of the new camera, a floating-point array [x, y].<br/>This is used to set the initial x and y values of the new<br/>camera’s Point of Interest property. The z value is set to 0. |

**Returns**

[CameraLayer object](cameralayer.md#cameralayer).

---

<a id="layercollection-addlight"></a>

### LayerCollection.addLight()

`app.project.item(index).layers.addLight(name, centerPoint)`

**Description**

Creates a new light layer and adds the [LightLayer object](lightlayer.md#lightlayer) to this collection. The new layer honors the “Create Layers at Composition Start Time” preference.

**Parameters**

| `name`        | A string containing the name of the new layer.              |
|---------------|-------------------------------------------------------------|
| `centerPoint` | The center of the new light, a floating-point array [x, y]. |

**Returns**

[LightLayer object](lightlayer.md#lightlayer).

---

<a id="layercollection-addnull"></a>

### LayerCollection.addNull()

`app.project.item(index).layers.addNull([duration])`

**Description**

Creates a new null layer and adds the [AVLayer object](avlayer.md#avlayer) to this collection. This is the same as choosing Layer > New > Null Object.

**Parameters**

| `duration`   | Optional, the length of a still layer in seconds, a<br/>floating-point value. If supplied, sets the `duration` value of<br/>the new layer. Otherwise, the `duration` value is set according<br/>to user preferences. By default, this is the same as the duration<br/>of the containing CompItem. To set another preferred value,<br/>choose Edit > Preferences > Import (Windows) or After Effects ><br/>Preferences > Import (Mac OS), and specify options under Still<br/>Footage.   |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

[AVLayer object](avlayer.md#avlayer).

---

<a id="layercollection-addshape"></a>

### LayerCollection.addShape()

`app.project.item(index).layers.addShape()`

**Description**

Creates a new [ShapeLayer object](shapelayer.md#shapelayer) for a new, empty Shape layer. Use the ShapeLayer object to add properties, such as shape, fill, stroke, and path filters. This is the same as using a shape tool in “Tool Creates Shape” mode. Tools automatically add a vector group that includes Fill and Stroke as specified in the tool options.

**Parameters**

None.

**Returns**

ShapeLayer object.

---

<a id="layercollection-addsolid"></a>

### LayerCollection.addSolid()

`app.project.item(index).layers.addSolid(color, name, width, height, pixelAspect[, duration])`

**Description**

Creates a new [SolidSource object](../sources/solidsource.md#solidsource), with values set as specified; sets the new SolidSource as the `mainSource` value of a new [FootageItem object](../items/footageitem.md#footageitem), and adds the FootageItem to the project. Creates a new [AVLayer object](avlayer.md#avlayer), sets the new Footage Item as its `source`, and adds the layer to this collection.

**Parameters**

| `color`       | The color of the solid, an array of three floating-point<br/>values,<br/>`[R, G, B]`, in the range `[0.0..1.0]`.                                                                                                                                                                                                                                                                                                                                                                     |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | A string containing the name of the solid.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `width`       | The width of the solid in pixels, an integer in the range<br/>`[4..30000]`.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `height`      | The height of the solid in pixels, an integer in the range<br/>`[4..30000]`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pixelAspect` | The pixel aspect ratio of the solid, a floating-point value<br/>in the range `[0.01..100.0]`.                                                                                                                                                                                                                                                                                                                                                                                        |
| `duration`    | Optional, the length of a still layer in seconds, a<br/>floating-point value. If supplied, sets the `duration`<br/>value of the new layer. Otherwise, the `duration` value is<br/>set according to user preferences. By default, this is the<br/>same as the duration of the containing CompItem. To set<br/>another preferred value, choose Edit > Preferences > Import<br/>(Windows) or After Effects > Preferences > Import (MacOS), and<br/>specify options under Still Footage. |

**Returns**

[AVLayer object](avlayer.md#avlayer).

---

<a id="layercollection-addtext"></a>

### LayerCollection.addText()

`app.project.item(index).layers.addText([sourceText])`

**Description**

Creates a new point text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocument-lineorientation) set to `LineOrientation.HORIZONTAL` and adds the new [TextLayer object](textlayer.md#textlayer) to this collection. To create a paragraph (box) text layer, use [LayerCollection.addBoxText()](#layercollection-addboxtext).

**Parameters**

| `sourceText`   | Optional; a string containing the source text of the new<br/>layer, or a [TextDocument object](../text/textdocument.md#textdocument) containing the source text of<br/>the new layer.   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

[TextLayer object](textlayer.md#textlayer).

---

<a id="layercollection-addverticalboxtext"></a>

### LayerCollection.addVerticalBoxText()

`app.project.item(index).layers.addVerticalBoxText([width, height])`

#### NOTE
This functionality was added in After Effects 24.2

**Description**

Creates a new paragraph (box) text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocument-lineorientation) set to `LineOrientation.VERTICAL_RIGHT_TO_LEFT` and adds the new [TextLayer object](textlayer.md#textlayer) to this collection. To create a point text layer, use the [LayerCollection.addText()](#layercollection-addtext) or [LayerCollection.addVerticalText()](#layercollection-addverticaltext) methods.

**Parameters**

| `[width, height]`   | An Array containing the dimensions of the new text box.   |
|---------------------|-----------------------------------------------------------|

**Returns**

TextLayer object.

---

<a id="layercollection-addverticaltext"></a>

### LayerCollection.addVerticalText()

`app.project.item(index).layers.addVerticalText([sourceText])`

#### NOTE
This functionality was added in After Effects 24.2

**Description**

Creates a new point text layer with [TextDocument.lineOrientation](../text/textdocument.md#textdocument-lineorientation) set to `LineOrientation.VERTICAL_RIGHT_TO_LEFT` and adds the new [TextLayer object](textlayer.md#textlayer) to this collection. To create a paragraph (box) text layer, use the [LayerCollection.addBoxText()](#layercollection-addboxtext) or [LayerCollection.addVerticalBoxText()](#layercollection-addverticalboxtext) methods.

**Parameters**

| `sourceText`   | Optional; a string containing the source text of the new<br/>layer, or a [TextDocument object](../text/textdocument.md#textdocument) containing the source text of<br/>the new layer.   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

[TextLayer object](textlayer.md#textlayer).

---

<a id="layercollection-byname"></a>

### LayerCollection.byName()

`app.project.item(index).layers.byName(name)`

**Description**

Returns the first (topmost) layer found in this collection with the specified name, or null if no layer with the given name is found.

**Parameters**

| `name`   | A string containing the name.   |
|----------|---------------------------------|

**Returns**

[Layer object](layer.md#layer) or null.

---

<a id="layercollection-precompose"></a>

### LayerCollection.precompose()

`app.project.item(index).layers.precompose(layerIndicies, name[, moveAllAttributes])`

**Description**

Creates a new [CompItem object](../items/compitem.md#compitem) and moves the specified layers into its layer collection. It removes the individual layers from this collection, and adds the new CompItem to this collection.

**Parameters**

| `layerIndices`      | The position indexes of the layers to be collected. An<br/>array of integers.                                                                                                                                                                                                                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`              | The name of the new CompItem object.                                                                                                                                                                                                                                                                                                                                                                                          |
| `moveAllAttributes` | Optional. When true (the default), retains all<br/>attributes in the new composition. This is the same as<br/>selecting the “Move all attributes into the new<br/>composition” option in the Pre-compose dialog box. You<br/>can only set this to false if there is just one index in<br/>the `layerIndices` array. This is the same as<br/>selecting the “Leave all attributes in” option in the<br/>Pre-compose dialog box. |

**Returns**

[CompItem object](../items/compitem.md#compitem).
