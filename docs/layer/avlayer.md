# AVLayer object

`app.project.item(index).layer(index)`

#### Description

The AVLayer object provides an interface to those layers that contain AVItem objects (composition layers, footage layers, solid layers, text layers, and sound layers).

!!! info
    AVLayer is a subclass of [Layer object](layer.md). All methods and attributes of Layer, in addition to those listed below, are available when working with AVLayer.

!!! info
    AVLayer is a base class for [TextLayer object](textlayer.md), so AVLayer attributes and methods are available when working with TextLayer objects.

#### AE Properties

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

#### Example

If the first item in the project is a CompItem, and the first layer of that CompItem is an AVLayer, the following sets the layer `quality`, `startTime`, and `inPoint`.

```javascript
var firstLayer = app.project.item(1).layer(1);
firstLayer.quality = LayerQuality.BEST;
firstLayer.startTime = 1;
firstLayer.inPoint = 2;
```

---

## Attributes

### AVLayer.adjustmentLayer

`app.project.item(index).layer(index).adjustmentLayer`

#### Description

`true` if the layer is an adjustment layer.

#### Type

Boolean; read/write.

---

### AVLayer.audioActive

`app.project.item(index).layer(index).audioActive`

#### Description

`true` if the layer's audio is active at the current time. For this value to be true, `audioEnabled` must be true, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the `inPoint`
and `outPoint` of this layer.

#### Type

Boolean; read-only.

---

### AVLayer.audioEnabled

`app.project.item(index).layer(index).audioEnabled`

#### Description

When `true`, the layer's audio is enabled. This value corresponds to the audio toggle switch in the Timeline panel.

#### Type

Boolean; read/write.

---

### AVLayer.blendingMode

`app.project.item(index).layer(index).blendingMode`

#### Description

The blending mode of the layer.

#### Type

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
- `BlendingMode.SILHOUETE_ALPHA` - note the mispelling of 'SILHOUETTE'!
- `BlendingMode.SILHOUETTE_LUMA`
- `BlendingMode.SOFT_LIGHT`
- `BlendingMode.STENCIL_ALPHA`
- `BlendingMode.STENCIL_LUMA`
- `BlendingMode.SUBTRACT`
- `BlendingMode.VIVID_LIGHT`

---

### AVLayer.canSetCollapseTransformation

`app.project.item(index).layer(index).canSetCollapseTransformation`

#### Description

`true` if it is legal to change the value of the `collapseTransformation` attribute on this layer.

#### Type

Boolean; read-only.

---

### AVLayer.canSetTimeRemapEnabled

`app.project.item(index).layer(index).canSetTimeRemapEnabled`

#### Description

`true` if it is legal to change the value of the `timeRemapEnabled` attribute on this layer.

#### Type

Boolean; read-only.

---

### AVLayer.collapseTransformation

`app.project.item(index).layer(index).collapseTransformation`

#### Description

`true` if collapse transformation is on for this layer.

#### Type

Boolean; read/write.

---

### AVLayer.effectsActive

`app.project.item(index).layer(index).effectsActive`

#### Description

`true` if the layer's effects are active, as indicated by the `<f>` icon next to it in the user interface.

#### Type

Boolean; read/write.

---

### AVLayer.environmentLayer

`app.project.item(index).layer(index).environmentLayer`

#### Description

`true` if this is an environment layer in a Ray-traced 3D composition. Setting this attribute to `true` automatically makes the layer 3D (`threeDLayer` becomes true).

#### Type

Boolean; read/write.

---

### AVLayer.frameBlending

`app.project.item(index).layer(index).frameBlending`

#### Description

`true` if frame blending is enabled for the layer.

#### Type

Boolean; read-only.

---

### AVLayer.frameBlendingType

`app.project.item(index).layer(index).frameBlendingType`

#### Description

The type of frame blending to perform when frame blending is enabled for the layer.

#### Type

A FrameBlendingType enumerated value; read/write. One of:

- `FrameBlendingType.FRAME_MIX`
- `FrameBlendingType.NO_FRAME_BLEND`
- `FrameBlendingType.PIXEL_MOTION`

---

### AVLayer.guideLayer

`app.project.item(index).layer(index).guideLayer`

#### Description

`true` if the layer is a guide layer.

#### Type

Boolean; read/write.

---

### AVLayer.hasAudio

`app.project.item(index).layer(index).hasAudio`

#### Description

`true` if the layer contains an audio component, regardless of whether it is audio-enabled or soloed.

#### Type

Boolean; read-only.

---

### AVLayer.hasTrackMatte

`app.project.item(index).layer(index).hasTrackMatte`

!!! note
    This functionality was updated in After Effects 23.0. Track Matte is no longer dependent on layer order.

#### Description

`true` if this layer has track matte. When `true`, this layer's `trackMatteType` value controls how the matte is applied.

See [AVLayer.trackMatteType](#avlayertrackmattetype) for available track matte types.

#### Type

Boolean; read-only.

---

### AVLayer.height

`app.project.item(index).layer(index).height`

#### Description

The height of the layer in pixels.

#### Type

Floating-point value; read-only.

---

### AVLayer.isNameFromSource

`app.project.item(index).layer(index).isNameFromSource`

#### Description

`true` if the layer has no expressly set name, but contains a named source. In this case, `layer.name` has the same value as `layer.source.name`. `false` if the layer has an expressly set name, or if the layer does not have a source.

#### Type

Boolean; read-only.

---

### AVLayer.isTrackMatte

`app.project.item(index)layer(index).isTrackMatte`

!!! note
    This functionality was updated in After Effects 23.0. Track Matte is no longer dependent on layer order.

#### Description

`true` if this layer is being used as a track matte.

#### Type

Boolean; read-only.

---

### AVLayer.motionBlur

`app.project.item(index).layer(index).motionBlur`

#### Description

`true` if motion blur is enabled for the layer.

#### Type

Boolean; read/write.

---

### AVLayer.preserveTransparency

`app.project.item(index).layer(index).preserveTransparency`

#### Description

`true` if preserve transparency is enabled for the layer.

#### Type

Boolean; read/write.

---

### AVLayer.quality

`app.project.item(index).layer(index).quality`

#### Description

The quality with which this layer is displayed.

#### Type

A `LayerQuality` enumerated value; read/write. One of:

- `LayerQuality.BEST`
- `LayerQuality.DRAFT`
- `LayerQuality.WIREFRAME`

---

### AVLayer.samplingQuality

`app.project.item(index).layer(index).samplingQuality`

!!! note
    This functionality was added in After Effects 12.0 (CC)

#### Description

Set/get layer sampling method (bicubic or bilinear)

#### Type

A `LayerSamplingQuality` enumerated value; read/write. One of:

- `LayerSamplingQuality.BICUBIC`
- `LayerSamplingQuality.BILINEAR`

---

### AVLayer.source

`app.project.item(index).layer(index).source`

#### Description

The source AVItem for this layer. The value is `null` in a Text layer. Use [AVLayer.replaceSource()](#avlayerreplacesource) to change the value.

#### Type

AVItem object; read-only.

---

### AVLayer.threeDLayer

`app.project.item(index).layer(index).threeDLayer`

#### Description

`true` if this is a 3D layer.

#### Type

Boolean; read/write.

---

### AVLayer.threeDPerChar

`app.project.item(index).layer(index).threeDPerChar`

#### Description

`true` if this layer has the Enable Per-character 3D switch set, allowing its characters to be animated off the plane of the text layer. Applies only to text layers.

#### Type

Boolean; read/write.

---

### AVLayer.timeRemapEnabled

`app.project.item(index).layer(index).timeRemapEnabled`

#### Description

`true` if time remapping is enabled for this layer.

#### Type

Boolean; read/write.

---

### AVLayer.trackMatteLayer

`app.project.item(index).layer(index).trackMatteLayer`

!!! note
    This functionality was added in After Effects 23.0

#### Description

Returns the track matte layer for this layer. Returns `null` if this layer has no track matte layer.

#### Type

AVLayer object; read only.

---

### AVLayer.trackMatteType

`app.project.item(index).layer(index).trackMatteType`

!!! note
    This functionality was updated in After Effects 23.0

!!! warning
    This is a Legacy API we don't recommend using for setting Track Matte Type in new scripts. Please consider using the latest track matte APIs [AVLayer.setTrackMatte()](#avlayersettrackmatte) and [AVLayer.removeTrackMatte()](#avlayerremovetrackmatte) for your tasks.

#### Description

If this layer has a track matte, specifies the way the track matte is applied.
Specifying the `TrackMatteType.NO_TRACK_MATTE` type will remove the track matte for this layer and reset the track matte type.

#### Type

A `TrackMatteType` enumerated value; read/write. One of:

- `TrackMatteType.ALPHA`
- `TrackMatteType.ALPHA_INVERTED`
- `TrackMatteType.LUMA`
- `TrackMatteType.LUMA_INVERTED`
- `TrackMatteType.NO_TRACK_MATTE`

#### Example

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

### AVLayer.width

`app.project.item(index).layer(index).width`

#### Description

The width of the layer in pixels.

#### Type

Floating-point value; read-only.

---

## Methods

### AVLayer.addToMotionGraphicsTemplate()

`app.project.item(index).layer(index).addToMotionGraphicsTemplate(comp)`

!!! note
    This functionality was added in After Effects 18.0 (2021)

#### Description

Adds the layer to the Essential Graphics Panel for the specified composition.

Returns `true` if the layer is successfully added, or otherwise `false`.

If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition. After Effects will present a warning dialog if the layer cannot be added to the EGP.

Use the [AVLayer.canAddToMotionGraphicsTemplate()](#avlayercanaddtomotiongraphicstemplate) method to test whether the layer can be added to a Motion Graphics template.

#### Parameters

| Parameter |                  Type                   |                          Description                           |
| --------- | --------------------------------------- | -------------------------------------------------------------- |
| `comp`    | [CompItem object](../item/compitem.md) | The composition where you wish to add the property to the EGP. |

#### Returns

Boolean.

---

### AVLayer.addToMotionGraphicsTemplateAs()

`app.project.item(index).layer(index).addToMotionGraphicsTemplateAs(comp, name)`

!!! note
    This functionality was added in After Effects 18.0 (2021)

#### Description

Adds the layer to the Essential Graphics Panel for the specified composition.

Returns `true` if the layer is successfully added, or otherwise `false`.

If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition. After Effects will present a warning dialog if the layer cannot be added to the EGP.

Use the [AVLayer.canAddToMotionGraphicsTemplate()](#avlayercanaddtomotiongraphicstemplate) method to test whether the layer can be added to a Motion Graphics template.

#### Parameters

| Parameter |                  Type                   |                          Description                           |
| --------- | --------------------------------------- | -------------------------------------------------------------- |
| `comp`    | [CompItem object](../item/compitem.md) | The composition where you wish to add the property to the EGP. |
| `name`    | String                                  | The new name.                                                  |

#### Returns

Boolean.

---

### AVLayer.audioActiveAtTime()

`app.project.item(index).layer(index).audioActiveAtTime(time)`

#### Description

Returns `true` if this layer's audio will be active at the specified time.

For this method to return `true`, `audioEnabled` must be `true`, no other layer with audio may be soloing unless this layer is soloed too, and the time must be between the `inPoint` and `outPoint` of this layer.

#### Parameters

| Parameter |         Type         |      Description      |
| --------- | -------------------- | --------------------- |
| `time`    | Floating-point value | The time, in seconds. |

#### Returns

Boolean.

---

### AVLayer.calculateTransformFromPoints()

`app.project.item(index).layer(index).calculateTransformFromPoints(pointTopLeft, pointTopRight, pointBottomRight)`

#### Description

Calculates a transformation from a set of points in this layer.

#### Parameters

|     Parameter      |                    Type                     |             Description             |
| ------------------ | ------------------------------------------- | ----------------------------------- |
| `pointTopLeft`     | Array of floating-point values, `[x, y, z]` | The top left point coordinates.     |
| `pointTopRight`    | Array of floating-point values, `[x, y, z]` | The top right point coordinates.    |
| `pointBottomRight` | Array of floating-point values, `[x, y, z]` | The bottom right point coordinates. |

#### Returns

An Object with the transformation properties set.

#### Example

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

### AVLayer.canAddToMotionGraphicsTemplate()

`app.project.item(index).layer(index).canAddToMotionGraphicsTemplate(comp)`

!!! note
    This functionality was added in After Effects 18.0 (2021)

#### Description

Test whether or not the layer can be added to the Essential Graphics Panel for the specified composition.

Returns `true` if the layer can be added, or otherwise `false`.

If the layer cannot be added, it is either because it is not a layer type for which media can be replaced (referred to as Media Replacement Layers), or the layer has already been added to the EGP for that composition.

Media Replacement layers are recognized as AVLayers with an [AVLayer.source](#avlayersource) set to a [FootageItem object](../item/footageitem.md) (with specific source types) or a [CompItem object](../item/compitem.md).

The AVLayer needs to comply with the restrictions below in order to be treated as a Media Replacement layer:

- [Layer.hasVideo](../layer/layer.md#layerhasvideo) should return `true`.
- [AVLayer.adjustmentLayer](#avlayeradjustmentlayer) should return `false`.
- [Layer.nullLayer](../layer/layer.md#layernulllayer) should return `false`.
- If the [AVLayer.source](#avlayersource) is a [FootageItem object](../item/footageitem.md), then FootageItem.FootageSource should not be a [SolidSource object](../sources/solidsource.md).
- If the [AVLayer.source](#avlayersource) is a [FootageItem object](../item/footageitem.md) and the FootageItem.FootageSource is a [FileSource object](../sources/filesource.md) then that FileSource should not point to a non-media file e.g. a JSX script file.

#### Parameters

| Parameter |                  Type                   |                          Description                           |
| --------- | --------------------------------------- | -------------------------------------------------------------- |
| `comp`    | [CompItem object](../item/compitem.md) | The composition where you wish to add the property to the EGP. |

#### Returns

Boolean.

---

### AVLayer.compPointToSource()

`app.project.item(index).layer(index).compPointToSource()`

!!! note
    This functionality was added in After Effects 13.2 (CC 2014.2)

#### Description

Converts composition coordinates, such as `sourcePointToComp`, to layer coordinates.

!!! warning
    This value only reflects the first character in the text layer at the current time.

#### Parameters

|      Parameter      |                   Type                   |                Description                |
| ------------------- | ---------------------------------------- | ----------------------------------------- |
| `sourcePointToComp` | Array of floating-point values, `[x, y]` | Position array of composition coordinates |

#### Returns

Array of ([X,Y]) position coordinates; read-only.

---

### AVLayer.openInViewer()

`app.project.item(index).layer(index).openInViewer()`

#### Description

Opens the layer in a Layer panel, and moves the Layer panel to front and gives it focus.

#### Parameters

None.

#### Returns

Viewer object for the Layer panel, or `null` if the layer could not be opened (e.g., for text or shape layers, which cannot be opened in the Layer panel).

---

### AVLayer.removeTrackMatte()

`app.project.item(index).layer(index).removeTrackMatte()`

!!! note
    This functionality was added in After Effects 23.0

#### Description

Removes the track matte for this layer while preserving the TrackMatteType.
See [AVLayer.setTrackMatte()](#avlayersettrackmatte) for another way of removing track matte.

#### Parameters

None.

#### Returns

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

### AVLayer.replaceSource()

`app.project.item(index).layer(index).replaceSource(newSource, fixExpressions)`

#### Description

Replaces the source for this layer.

!!! warning
    If this method is performed on a null layer, the layers `isNull` attribute is not changed from `true`. This causes the layer not to be visible in comp viewer and renders.

#### Parameters

+------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|    Parameter     |                Type                |                                                                                                       Description                                                                                                        |
+==================+====================================+==========================================================================================================================================================================================================================+
| `newSource`      | [AVItem object](../item/avitem.md) | The new source AVItem object.                                                                                                                                                                                            |
+------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fixExpressions` | Boolean                            | `true` to adjust expressions for the new source, otherwise `false`.                                                                                                                                                      |
|                  |                                    |                                                                                                                                                                                                                          |
|                  |                                    | !!! warning                                                                                                                                                                                                              |
|                  |                                    |      This feature can be resource-intensive; if replacing a large amount of footage, do this only at the end of the operation. See also [Project.autoFixExpressions()](../general/project.md#projectautofixexpressions). |
+------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Nothing.

---

### AVLayer.setTrackMatte()

`app.project.item(index).layer(index).setTrackMatte(trackMatteLayer, trackMatteType)`

!!! note
    This functionality was added in After Effects 23.0

#### Description

Sets the track matte layer and type for this layer. Passing in `null` to trackMatteLayer parameter removes the track matte.
See [AVLayer.removeTrackMatte()](#avlayerremovetrackmatte) for another way of removing track matte.

#### Parameters

|     Parameter     |                     Type                      |                  Description                   |
| ----------------- | --------------------------------------------- | ---------------------------------------------- |
| `trackMatteLayer` | [AVLayer](../layer/avlayer.md)               | The layer to be used as the track matte layer. |
| `trackMatteType`  | [TrackMatteType](#avlayertrackmattetype) enum | The type of the track matte to be used.        |

!!! warning
    Passing in `TrackMatteType.NO_TRACK_MATTE` as type is invalid and will result in no-op.

#### Returns

Nothing

#### Example

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

### AVLayer.sourcePointToComp()

`app.project.item(index).layer(index).sourcePointToComp()`

!!! note
    This functionality was added in After Effects 13.2 (CC 2014.2)

#### Description

Converts layer coordinates, such as `boxTextPos`, to composition coordinates.

!!! warning
    This value only reflects the first character in the text layer at the current time.

#### Parameters

|  Parameter   |                   Type                   |              Description               |
| ------------ | ---------------------------------------- | -------------------------------------- |
| `boxTextPos` | Array of floating-point values, `[x, y]` | A position array of layer coordinates. |

#### Returns

Array of ([X,Y]) position coordinates; read-only.

#### Example

```javascript
// For a paragraph text layer.
// Converts position in layer coordinates to comp coordinates.
var boxTextCompPos = myTextLayer.sourcePointToComp(boxTextLayerPos);
```

---

### AVLayer.sourceRectAtTime()

`app.project.item(index).layer(index).sourceRectAtTime(timeT, extents)`

#### Description

Retrieves the rectangle bounds of the layer at the specified time index, corrected for text or shape layer content. Use, for example, to write text that is properly aligned to the baseline.

#### Parameters

| Parameter |         Type         |                                                              Description                                                               |
| --------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `timeT`   | Floating-point value | The time index, in seconds.                                                                                                            |
| `extents` | Boolean              | `true` to include the extents, otherwise `false`. Extents apply to shape layers, increasing the size of the layer bounds as necessary. |

#### Returns

A JavaScript object with four attributes, [`top`, `left`, `width`, `height`].
