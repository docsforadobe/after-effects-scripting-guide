<a id="avlayer"></a>

# AVLayer object

`app.project.item(index).layer(index)`

**Description**

The AVLayer object provides an interface to those layers that contain AVItem objects (composition layers, footage layers, solid layers, text layers, and sound layers).

> AVLayer is a subclass of [Layer object](layer.md#layer). All methods and attributes of Layer, in addition to those listed below, are available when working with AVLayer.

> AVLayer is a base class for [TextLayer object](textlayer.md#textlayer), so AVLayer attributes and methods are available when working with TextLayer objects.

**AE Properties**

Different types of layers have different AE properties. AVLayer has the following properties and property groups:

- Marker
- Time Remap
- Motion Trackers
- Masks
- Effects
- Transform
  - Anchor Point
  - Position
  - Scale
  - Orientation
  - X Rotation
  - Y Rotation
  - Rotation
  - Opacity
- Layer Styles
- Geometry Options // Ray-traced 3D
- Material Options
  - Casts Shadows
  - Light Transmission
  - Accepts Shadows
  - Accepts Lights
  - Appears in Reflections // Ray-traced 3D
  - Ambient
  - Diffuse
  - Specular Intensity
  - Specular Shininess
  - Metal
  - Reflection Intensity // Ray-traced 3D
  - Reflection Sharpness // Ray-traced 3D
  - Reflection Rolloff // Ray-traced 3D
  - Transparency // Ray-traced 3D
  - Transparency Rolloff // Ray-traced 3D
  - Index of Refraction // Ray-traced 3D
- Audio
  - AudioLevels

**Example**

If the first item in the project is a CompItem, and the first layer of that CompItem is an AVLayer, the following sets the layer `quality`, `startTime`, and `inPoint`.

```javascript
var firstLayer = app.project.item(1).layer(1);
firstLayer.quality = LayerQuality.BEST;
firstLayer.startTime = 1;
firstLayer.inPoint = 2;
```

---

## Attributes

<a id="avlayer-adjustmentlayer"></a>

### AVLayer.adjustmentLayer

`app.project.item(index).layer(index).adjustmentLayer`

**Description**

True if the layer is an adjustment layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-audioactive"></a>

### AVLayer.audioActive

`app.project.item(index).layer(index).audioActive`

**Description**

True if the layer’s audio is active at the current time. For this value to be true, `audioEnabled` must be true, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the `inPoint`
and `outPoint` of this layer.

**Type**

Boolean; read-only.

---

<a id="avlayer-audioenabled"></a>

### AVLayer.audioEnabled

`app.project.item(index).layer(index).audioEnabled`

**Description**

When true, the layer’s audio is enabled. This value corresponds to the audio toggle switch in the Timeline panel.

**Type**

Boolean; read/write.

---

<a id="avlayer-blendingmode"></a>

### AVLayer.blendingMode

`app.project.item(index).layer(index).blendingMode`

**Description**

The blending mode of the layer.

**Type**

A BlendingMode enumerated value; read/write. One of:

- `BlendingMode.ADD`
- `BlendingMode.ALPHA_ADD`
- `BlendingMode.CLASSIC_COLOR_BURN`
- `BlendingMode.CLASSIC_COLOR_DODGE`
- `BlendingMode.CLASSIC_DIFFERENCE`
- `BlendingMode.COLOR`
- `BlendingMode.COLOR_BURN`
- `BlendingMode.COLOR_DODGE`
- `BlendingMode.DANCING_DISSOLVE`
- `BlendingMode.DARKEN`
- `BlendingMode.DARKER_COLOR`
- `BlendingMode.DIFFERENCE`
- `BlendingMode.DISSOLVE`
- `BlendingMode.DIVIDE`
- `BlendingMode.EXCLUSION`
- `BlendingMode.HARD_LIGHT`
- `BlendingMode.HARD_MIX`
- `BlendingMode.HUE`
- `BlendingMode.LIGHTEN`
- `BlendingMode.LIGHTER_COLOR`
- `BlendingMode.LINEAR_BURN`
- `BlendingMode.LINEAR_DODGE`
- `BlendingMode.LINEAR_LIGHT`
- `BlendingMode.LUMINESCENT_PREMUL`
- `BlendingMode.LUMINOSITY`
- `BlendingMode.MULTIPLY`
- `BlendingMode.NORMAL`
- `BlendingMode.OVERLAY`
- `BlendingMode.PIN_LIGHT`
- `BlendingMode.SATURATION`
- `BlendingMode.SCREEN`
- `BlendingMode.SUBTRACT`
- `BlendingMode.SILHOUETE_ALPHA` - note the mispelling of ‘SILHOUETTE’!
- `BlendingMode.SILHOUETTE_LUMA`
- `BlendingMode.SOFT_LIGHT`
- `BlendingMode.STENCIL_ALPHA`
- `BlendingMode.STENCIL_LUMA`
- `BlendingMode.SUBTRACT`
- `BlendingMode.VIVID_LIGHT`

---

<a id="avlayer-cansetcollapsetransformation"></a>

### AVLayer.canSetCollapseTransformation

`app.project.item(index).layer(index).canSetCollapseTransformation`

**Description**

True if it is legal to change the value of the `collapseTransformation` attribute on this layer.

**Type**

Boolean; read-only.

---

<a id="avlayer-cansettimeremapenabled"></a>

### AVLayer.canSetTimeRemapEnabled

`app.project.item(index).layer(index).canSetTimeRemapEnabled`

**Description**

True if it is legal to change the value of the `timeRemapEnabled` attribute on this layer.

**Type**

Boolean; read-only.

---

<a id="avlayer-collapsetransformation"></a>

### AVLayer.collapseTransformation

`app.project.item(index).layer(index).collapseTransformation`

**Description**

True if collapse transformation is on for this layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-effectsactive"></a>

### AVLayer.effectsActive

`app.project.item(index).layer(index).effectsActive`

**Description**

True if the layer’s effects are active, as indicated by the `<f>` icon next to it in the user interface.

**Type**

Boolean; read/write.

---

<a id="avlayer-environmentlayer"></a>

### AVLayer.environmentLayer

`app.project.item(index).layer(index).environmentLayer`

**Description**

True if this is an environment layer in a Ray-traced 3D composition. Setting this attribute to true automatically makes the layer 3D (`threeDLayer` becomes true).

**Type**

Boolean; read/write.

---

<a id="avlayer-frameblending"></a>

### AVLayer.frameBlending

`app.project.item(index).layer(index).frameBlending`

**Description**

True if frame blending is enabled for the layer.

**Type**

Boolean; read-only.

---

<a id="avlayer-frameblendingtype"></a>

### AVLayer.frameBlendingType

`app.project.item(index).layer(index).frameBlendingType`

**Description**

The type of frame blending to perform when frame blending is enabled for the layer.

**Type**

A FrameBlendingType enumerated value; read/write. One of:

- `FrameBlendingType.FRAME_MIX`
- `FrameBlendingType.NO_FRAME_BLEND`
- `FrameBlendingType.PIXEL_MOTION`

---

<a id="avlayer-guidelayer"></a>

### AVLayer.guideLayer

`app.project.item(index).layer(index).guideLayer`

**Description**

True if the layer is a guide layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-hasaudio"></a>

### AVLayer.hasAudio

`app.project.item(index).layer(index).hasAudio`

**Description**

True if the layer contains an audio component, regardless of whether it is audio-enabled or soloed.

**Type**

Boolean; read-only.

---

<a id="avlayer-hastrackmatte"></a>

### AVLayer.hasTrackMatte

`app.project.item(index).layer(index).hasTrackMatte`

#### NOTE
This functionality was updated in After Effects 23.0. Track Matte is no longer dependent on layer order.

**Description**

True if this layer has track matte. When true, this layer’s `trackMatteType` value controls how the matte is applied.
See [AVLayer.trackMatteType](#avlayer-trackmattetype) for available track matte types.

**Type**

Boolean; read-only.

---

<a id="avlayer-height"></a>

### AVLayer.height

`app.project.item(index).layer(index).height`

**Description**

The height of the layer in pixels.

**Type**

Floating-point; read-only.

---

<a id="avlayer-isnamefromsource"></a>

### AVLayer.isNameFromSource

`app.project.item(index).layer(index).isNameFromSource`

**Description**

True if the layer has no expressly set name, but contains a named source. In this case, `layer.name` has the same value as `layer.source.name`. False if the layer has an expressly set name, or if the layer does not have a source.

**Type**

Boolean; read-only.

---

<a id="avlayer-istrackmatte"></a>

### AVLayer.isTrackMatte

`app.project.item(index)layer(index).isTrackMatte`

#### NOTE
This functionality was updated in After Effects 23.0. Track Matte is no longer dependent on layer order.

**Description**

True if this layer is being used as a track matte.

**Type**

Boolean; read-only.

---

<a id="avlayer-motionblur"></a>

### AVLayer.motionBlur

`app.project.item(index).layer(index).motionBlur`

**Description**

True if motion blur is enabled for the layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-preservetransparency"></a>

### AVLayer.preserveTransparency

`app.project.item(index).layer(index).preserveTransparency`

**Description**

True if preserve transparency is enabled for the layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-quality"></a>

### AVLayer.quality

`app.project.item(index).layer(index).quality`

**Description**

The quality with which this layer is displayed.

**Type**

A `LayerQuality` enumerated value; read/write. One of:

- `LayerQuality.BEST`
- `LayerQuality.DRAFT`
- `LayerQuality.WIREFRAME`

---

<a id="avlayer-samplingquality"></a>

### AVLayer.samplingQuality

`app.project.item(index).layer(index).samplingQuality`

#### NOTE
This functionality was added in After Effects 12.0 (CC)

**Description**

Set/get layer sampling method (bicubic or bilinear)

**Type**

A `LayerSamplingQuality` enumerated value; read/write. One of:

- `LayerSamplingQuality.BICUBIC`
- `LayerSamplingQuality.BILINEAR`

---

<a id="avlayer-source"></a>

### AVLayer.source

`app.project.item(index).layer(index).source`

**Description**

The source AVItem for this layer. The value is null in a Text layer. Use `AVLayer.replaceSource()` to change the value.

**Type**

AVItem object; read-only.

---

<a id="avlayer-threedlayer"></a>

### AVLayer.threeDLayer

`app.project.item(index).layer(index).threeDLayer`

**Description**

True if this is a 3D layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-threedperchar"></a>

### AVLayer.threeDPerChar

`app.project.item(index).layer(index).threeDPerChar`

**Description**

`True` if this layer has the Enable Per-character 3D switch set, allowing its characters to be animated off the plane of the text layer. Applies only to text layers.

**Type**

Boolean; read/write.

---

<a id="avlayer-timeremapenabled"></a>

### AVLayer.timeRemapEnabled

`app.project.item(index).layer(index).timeRemapEnabled`

**Description**

True if time remapping is enabled for this layer.

**Type**

Boolean; read/write.

---

<a id="avlayer-trackmattelayer"></a>

### AVLayer.trackMatteLayer

`app.project.item(index).layer(index).trackMatteLayer`

#### NOTE
This functionality was added in After Effects 23.0

**Description**

Returns the track matte layer for this layer. Returns `null` if this layer has no track matte layer.

**Type**

AVLayer object; read only.

---

<a id="avlayer-trackmattetype"></a>

### AVLayer.trackMatteType

`app.project.item(index).layer(index).trackMatteType`

#### NOTE
This functionality was updated in After Effects 23.0

#### WARNING
This is a Legacy API we don’t recommend using for setting Track Matte Type in new scripts. Please consider using the latest track matte APIs [AVLayer.setTrackMatte()](#avlayer-settrackmatte) and [AVLayer.removeTrackMatte()](#avlayer-removetrackmatte) for your tasks.

**Description**

If this layer has a track matte, specifies the way the track matte is applied.
Specifying the `TrackMatteType.NO_TRACK_MATTE` type will remove the track matte for this layer and reset the track matte type.

**Type**

A `TrackMatteType` enumerated value; read/write. One of:

- `TrackMatteType.ALPHA`
- `TrackMatteType.ALPHA_INVERTED`
- `TrackMatteType.LUMA`
- `TrackMatteType.LUMA_INVERTED`
- `TrackMatteType.NO_TRACK_MATTE`

**Example**

```javascript
// Returns the current track matte type for myLayer
var type = myLayer.trackMatteType;

// *** We recommend using the new Track Matte APIs for the operations below (See Warning) ***

// Changes the track matte type for myLayer to TrackMatteType.ALPHA_INVERTED
myLayer.trackMatteType = TrackMatteType.ALPHA_INVERTED;

// Removes the track matte and also resets the type
myLayer.trackMatteType = TrackMatteType.NO_TRACK_MATTE;
```

---

<a id="avlayer-width"></a>

### AVLayer.width

`app.project.item(index).layer(index).width`

**Description**

The width of the layer in pixels.

**Type**

Floating-point; read-only.

---

## Methods

<a id="avlayer-addtomotiongraphicstemplate"></a>

### AVLayer.addToMotionGraphicsTemplate()

`app.project.item(index).layer(index).addToMotionGraphicsTemplate(comp)`

#### NOTE
This functionality was added in After Effects 18.0 (2021)

**Description**

Adds the layer to the Essential Graphics Panel for the specified composition.

Returns true if the layer is successfully added, or false otherwise.

- If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition. After Effects will present a warning dialog if the layer cannot be added to the EGP.
- Use the [AVLayer.canAddToMotionGraphicsTemplate()](#avlayer-canaddtomotiongraphicstemplate) method to test whether the layer can be added to a Motion Graphics template.

**Parameters**

| `comp`   | A CompItem object; the composition where you wish to add the property to the EGP. Required.   |
|----------|-----------------------------------------------------------------------------------------------|

**Returns**

Boolean.

---

<a id="avlayer-addtomotiongraphicstemplateas"></a>

### AVLayer.addToMotionGraphicsTemplateAs()

`app.project.item(index).layer(index).addToMotionGraphicsTemplateAs(comp, name)`

#### NOTE
This functionality was added in After Effects 18.0 (2021)

**Description**

Adds the layer to the Essential Graphics Panel for the specified composition.

Returns true if the layer is successfully added, or false otherwise.

- If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition. After Effects will present a warning dialog if the layer cannot be added to the EGP.
- Use the [AVLayer.canAddToMotionGraphicsTemplate()](#avlayer-canaddtomotiongraphicstemplate) method to test whether the layer can be added to a Motion Graphics template.

**Parameters**

| `comp`   | A CompItem object; the composition where you wish to add<br/>the property to the EGP. Required.   |
|----------|---------------------------------------------------------------------------------------------------|
| `name`   | A string for the new name. Required.                                                              |

**Returns**

Boolean.

---

<a id="avlayer-audioactiveattime"></a>

### AVLayer.audioActiveAtTime()

`app.project.item(index).layer(index).audioActiveAtTime(time)`

**Description**

Returns true if this layer’s audio will be active at the specified time. For this method to return true, `audioEnabled` must be true, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the `inPoint` and `outPoint` of this layer.

**Parameters**

| `time`   | The time, in seconds. A floating-point value.   |
|----------|-------------------------------------------------|

**Returns**

Boolean.

---

<a id="avlayer-calculatetransformfrompoints"></a>

### AVLayer.calculateTransformFromPoints()

`app.project.item(index).layer(index).calculateTransformFromPoints(pointTopLeft, pointTopRight, pointBottomRight)`

**Description**

Calculates a transformation from a set of points in this layer.

**Parameters**

| `pointTopLeft`     | The top left point coordinates in the form of an array,<br/>[x , y, z] .      |
|--------------------|-------------------------------------------------------------------------------|
| `pointTopRight`    | The top right point coordinates in the form of an array,<br/>[ x, y, z ] .    |
| `pointBottomRight` | The bottom right point coordinates in the form of an<br/>array, [ x, y, z ] . |

**Returns**

An Object with the transformation properties set.

**Example**

```javascript
var newLayer = comp.layers.add(newFootage);
newLayer.threeDLayer = true;
newLayer.blendingMode = BlendingMode.ALPHA_ADD;
var transform = newLayer.calculateTransformFromPoints(tl, tr, bl);
for (var sel in transform) {
  newLayer.transform[sel].setValue(transform[sel]);
}
```

---

<a id="avlayer-canaddtomotiongraphicstemplate"></a>

### AVLayer.canAddToMotionGraphicsTemplate()

`app.project.item(index).layer(index).canAddToMotionGraphicsTemplate(comp)`

#### NOTE
This functionality was added in After Effects 18.0 (2021)

**Description**

Test whether or not the layer can be added to the Essential Graphics Panel for the specified composition.

Returns true if the layer can be added, or false otherwise.

If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition.

Media Replacement layers are recognized as AVLayers with an [AVLayer.source](#avlayer-source) set to a [FootageItem object](../items/footageitem.md#footageitem) (with specific source types) or a [CompItem object](../items/compitem.md#compitem).

The AVLayer needs to comply with the restrictions below in order to be treated as a Media Replacement layer:

- [Layer.hasVideo](layer.md#layer-hasvideo) should return true.
- [AVLayer.adjustmentLayer](#avlayer-adjustmentlayer) should return false.
- [Layer.nullLayer](layer.md#layer-nulllayer) should return false.
- If the [AVLayer.source](#avlayer-source) is a [FootageItem object](../items/footageitem.md#footageitem), then FootageItem.FootageSource should not be a [SolidSource object](../sources/solidsource.md#solidsource).
- If the [AVLayer.source](#avlayer-source) is a [FootageItem object](../items/footageitem.md#footageitem) and the FootageItem.FootageSource is a [FileSource object](../sources/filesource.md#filesource) then that FileSource should not point to a non-media file e.g. a JSX script file.

**Parameters**

| `comp`   | A CompItem object; the composition where you wish to add the property to the EGP. Required.   |
|----------|-----------------------------------------------------------------------------------------------|

**Returns**

Boolean.

---

<a id="avlayer-comppointtosource"></a>

### AVLayer.compPointToSource()

`app.project.item(index).layer(index).compPointToSource()`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

Converts composition coordinates, such as `sourcePointToComp`, to layer coordinates.

#### WARNING
This value only reflects the first character in the text layer at the current time.

**Parameters**

| `sourcePointToComp`   | A position array of composition coordinates in ([X, Y]) format.   |
|-----------------------|-------------------------------------------------------------------|

**Returns**

Array of ([X,Y]) position coordinates; read-only.

---

<a id="avlayer-openinviewer"></a>

### AVLayer.openInViewer()

`app.project.item(index).layer(index).openInViewer()`

**Description**

Opens the layer in a Layer panel, and moves the Layer panel to front and gives it focus.

**Parameters**

None.

**Returns**

Viewer object for the Layer panel, or null if the layer could not be opened (e.g., for text or shape layers, which cannot be opened in the Layer panel).

---

<a id="avlayer-removetrackmatte"></a>

### AVLayer.removeTrackMatte()

`app.project.item(index).layer(index).removeTrackMatte()`

#### NOTE
This functionality was added in After Effects 23.0

**Description**

Removes the track matte for this layer while preserving the TrackMatteType.
See [AVLayer.setTrackMatte()](#avlayer-settrackmatte) for another way of removing track matte.

**Parameters**

None.

**Returns**

Nothing.

```javascript
// Sets the track matte layer of myLayer with otherLayer as LUMA type
myLayer.setTrackMatte(otherLayer, TrackMatteType.LUMA);

// Removes the track matte for myLayer but preserves the LUMA type
myLayer.removeTrackMatte();

// Still returns TrackMatteType.LUMA
alert(myLayer.trackMatteType);
```

---

<a id="avlayer-replacesource"></a>

### AVLayer.replaceSource()

`app.project.item(index).layer(index).replaceSource(newSource, fixExpressions)`

**Description**

Replaces the source for this layer.

**Parameters**

| `newSource`      | The new source AVItem object.                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fixExpressions` | `True` to adjust expressions for the new source,<br/>`false` otherwise. Note that this feature can be<br/>resource-intensive; if replacing a large amount of<br/>footage, do this only at the end of the operation. See<br/>also [Project.autoFixExpressions()](../general/project.md#project-autofixexpressions). |

**Returns**

Nothing.

#### WARNING
If this method is performed on a null layer, the layers `isNull` attribute is not changed from `true`. This causes the layer not to be visible in comp viewer and renders.

---

<a id="avlayer-settrackmatte"></a>

### AVLayer.setTrackMatte()

`app.project.item(index).layer(index).setTrackMatte(trackMatteLayer, trackMatteType)`

#### NOTE
This functionality was added in After Effects 23.0

**Description**

Sets the track matte layer and type for this layer. Passing in `null` to trackMatteLayer parameter removes the track matte.
See [AVLayer.removeTrackMatte()](#avlayer-removetrackmatte) for another way of removing track matte.

**Parameters**

| `trackMatteLayer`   | The AVLayer to be used as the track matte layer.                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------|
| `trackMatteType`    | The type of the track matte to be used. Please see [AVLayer.trackMatteType](#avlayer-trackmattetype) for available types. |

#### WARNING
Passing in `TrackMatteType.NO_TRACK_MATTE` as type is invalid and will result in no-op.

**Returns**

Nothing

**Example**

```javascript
// Sets the track matte layer of myLayer with otherLayer as Alpha type
myLayer.setTrackMatte(otherLayer, TrackMatteType.ALPHA);

// Keeps the same trackMatteLayer and only changes the track matte type
myLayer.setTrackMatte(myLayer.trackMatteLayer, TrackMatteType.LUMA);

// Changes the track matte layer but keep the same track matte type
myLayer.setTrackMatte(newTrackMatteLayer, myLayer.trackMatteType);

// Removes the track matte for myLayer and sets the new specified TrackMatteType
myLayer.setTrackMatte(null, TrackMatteType.ALPHA);
myLayer.setTrackMatte(null, TrackMatteType.NO_TRACK_MATTE);

// Invalid. Nothing happens
myLayer.setTrackMatte(otherLayer, TrackMatteType.NO_TRACK_MATTE);
```

---

<a id="avlayer-sourcepointtocomp"></a>

### AVLayer.sourcePointToComp()

`app.project.item(index).layer(index).sourcePointToComp()`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

Converts layer coordinates, such as `boxTextPos`, to composition coordinates.

#### WARNING
This value only reflects the first character in the text layer at the current time.

**Parameters**

| `boxTextPos`   | A position array of layer coordinates in ([X, Y]) format.   |
|----------------|-------------------------------------------------------------|

**Returns**

Array of ([X,Y]) position coordinates; read-only.

**Example**

```javascript
// For a paragraph text layer.
// Converts position in layer coordinates to comp coordinates.
var boxTextCompPos = myTextLayer.sourcePointToComp(boxTextLayerPos);
```

---

<a id="avlayer-sourcerectattime"></a>

### AVLayer.sourceRectAtTime()

`app.project.item(index).layer(index).sourceRectAtTime(timeT, extents)`

**Description**

Retrieves the rectangle bounds of the layer at the specified time index, corrected for text or shape layer content. Use, for example, to write text that is properly aligned to the baseline.

**Parameters**

| `timeT`   | The time index, in seconds. A floating-point value.                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `extents` | `True` to include the extents, `false` otherwise. Extents<br/>apply to shape layers, increasing the size of the layer bounds<br/>as necessary. |

**Returns**

A JavaScript object with four attributes, [`top`, `left`, `width`, `height`].
