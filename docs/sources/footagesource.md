# FootageSource object

`app.project.item(index).mainSource`
<br/>
`app.project.item(index).proxySource`
<br/>

**Description**

The FootageSource object holds information describing the source of some footage. It is used as the `mainSource` of a [FootageItem object](../items/footageitem.md#footageitem), or the `proxySource` of a [CompItem object](../items/compitem.md#compitem) or FootageItem.

> FootageSource is the base class for [SolidSource object](solidsource.md#solidsource), so FootageSource attributes and methods are available when working with SolidSource objects.

---

## Attributes

### FootageSource.alphaMode

`app.project.item(index).mainSource.alphaMode`
<br/>
`app.project.item(index).proxySource.alphaMode`
<br/>

**Description**

Defines how the alpha information in the footage is interpreted. If `hasAlpha` is false, this attribute has no relevant meaning.

**Type**

An Alpha Mode enumerated value; (read/write). One of:

- `AlphaMode.IGNORE`
- `AlphaMode.STRAIGHT`
- `AlphaMode.PREMULTIPLIED`

---

### FootageSource.conformFrameRate

`app.project.item(index).mainSource.conformFrameRate`
<br/>
`app.project.item(index).proxySource.conformFrameRate`
<br/>

**Description**

A frame rate to use instead of the `nativeFrameRate` value. If set to 0, the `nativeFrameRate` is used instead. It is an error to set this value if [FootageSource.isStill](#footagesource-isstill) is true. It is an error to set this value to 0 if [removePulldown](#footagesource-removepulldown) is not set to `PulldownPhase.OFF`. If this is 0 when you set `removePulldown` to a value other than `PulldownPhase.OFF`, then this is automatically set to the value of `nativeFrameRate`.

**Type**

Floating-point value in the range `[0.0..99.0]`; read/write.

---

### FootageSource.displayFrameRate

`app.project.item(index).mainSource.displayFrameRate`
<br/>
`app.project.item(index).proxySource.displayFrameRate`
<br/>

**Description**

The effective frame rate as displayed and rendered in compositions by After Effects. If [removePulldown](#footagesource-removepulldown) is `PulldownPhase.OFF`, then this is the same as the `conformFrameRate` (if non-zero) or the `nativeFrameRate` (if `conformFrameRate` is 0). If `removePulldown` is not `PulldownPhase.OFF`, this is `conformFrameRate * 0.8`, the effective frame rate after removing 1 of every 5 frames.

**Type**

Floating-point value in the range `[0.0..99.0]`; read-only.

---

### FootageSource.fieldSeparationType

`app.project.item(index).mainSource.fieldSeparationType`
<br/>
`app.project.item(index).proxySource.fieldSeparationType`
<br/>

**Description**

How the fields are to be separated in non-still footage. It is an error to set this attribute if `isStill` is true. It is an error to set this value to `FieldSeparationType.OFF` if [removePulldown](#footagesource-removepulldown) is not `PulldownPhase.OFF`.

**Type**

A `FieldSeparationType` enumerated value; read/write. One of:

- `FieldSeparationType.OFF`
- `FieldSeparationType.UPPER_FIELD_FIRST`
- `FieldSeparationType.LOWER_FIELD_FIRST`

---

### FootageSource.hasAlpha

`app.project.item(index).mainSource.hasAlpha`
<br/>
`app.project.item(index).proxySource.hasAlpha`
<br/>

**Description**

When true, the footage has an alpha component. In this case, the attributes `alphaMode`, `invertAlpha`, and `premulColor` have valid values. When `false`, those attributes have no relevant meaning for the footage.

**Type**

Boolean; read-only.

---

### FootageSource.highQualityFieldSeparation

`app.project.item(index).mainSource.highQualityFieldSeparation`
<br/>
`app.project.item(index).proxySource.highQualityFieldSeparation`
<br/>

**Description**

When true, After Effects uses special algorithms to determine how to perform high-quality field separation. It is an error to set this attribute if `isStill` is true, or if `fieldSeparationType` is `FieldSeparationType.OFF`.

**Type**

Boolean; read/write.

---

### FootageSource.invertAlpha

`app.project.item(index).mainSource.invertAlpha`
<br/>
`app.project.item(index).proxySource.invertAlpha`
<br/>

**Description**

When true, an alpha channel in a footage clip or proxy should be inverted. This attribute is valid only if an alpha is present. If `hasAlpha` is false, or if `alphaMode` is `AlphaMode.IGNORE`, this attribute is ignored.

**Type**

Boolean; read/write.

---

### FootageSource.isStill

`app.project.item(index).mainSource.isStill`
<br/>
`app.project.item(index).proxySource.isStill`
<br/>

**Description**

When true the footage is still; when false, it has a time-based component. Examples of still footage are JPEG files, solids, and placeholders with a duration of 0. Examples of non-still footage are movie files, sound files, sequences, and placeholders of non-zero duration.

**Type**

Boolean; read-only.

---

### FootageSource.loop

`app.project.item(index).mainSource.loop`
<br/>
`app.project.item(index).proxySource.loop`
<br/>

**Description**

The number of times that the footage is to be played consecutively when used in a composition. It is an error to set this attribute if `isStill` is true.

**Type**

Integer in the range `[1..9999]`; default is 1; read/write.

---

### FootageSource.nativeFrameRate

`app.project.item(index).mainSource.nativeFrameRate`
<br/>
`app.project.item(index).proxySource.nativeFrameRate`
<br/>

**Description**

The native frame rate of the footage.

**Type**

Floating-point; read-only.

---

### FootageSource.premulColor

`app.project.item(index).mainSource.premulColor`
<br/>
`app.project.item(index).proxySource.premulColor`
<br/>

**Description**

The color to be premultiplied. This attribute is valid only if the `alphaMode` is `alphaMode.PREMULTIPLIED`.

**Type**

Array of three floating-point values `[R, G, B]`, in the range `[0.0..1.0]`; read/write.

---

### FootageSource.removePulldown

`app.project.item(index).mainSource.removePulldown`
<br/>
`app.project.item(index).proxySource.removePulldown`
<br/>

**Description**

How the pulldowns are to be removed when field separation is used. It is an error to set this attribute if `isStill` is true. It is an error to attempt to set this to a value other than `PulldownPhase.OFF` in the case where `fieldSeparationType` is `FieldSeparationType.OFF`.

**Type**

A `PulldownPhase` enumerated value; read/write. One of:

- `PulldownPhase.RemovePulldown.OFF`
- `PulldownPhase.RemovePulldown.WSSWW`
- `PulldownPhase.RemovePulldown.SSWWW`
- `PulldownPhase.RemovePulldown.SWWWS`
- `PulldownPhase.RemovePulldown.WWWSS`
- `PulldownPhase.RemovePulldown.WWSSW`
- `PulldownPhase.RemovePulldown.WSSWW_24P_ADVANCE`
- `PulldownPhase.RemovePulldown.SSWWW_24P_ADVANCE`
- `PulldownPhase.RemovePulldown.SWWWS_24P_ADVANCE`
- `PulldownPhase.RemovePulldown.WWWSS_24P_ADVANCE`
- `PulldownPhase.RemovePulldown.WWSSW_24P_ADVANCE`

---

## Methods

### FootageSource.guessAlphaMode()

`app.project.item(index).mainSource.guessAlphaMode()`
<br/>
`app.project.item(index).proxySource.guessAlphaMode()`
<br/>

**Description**

Sets `alphaMode`, `premulColor`, and `invertAlpha` to the best estimates for this footage source. If `hasAlpha` is false, no change is made.

**Parameters**

None.

**Returns**

Nothing.

---

### FootageSource.guessPulldown()

`app.project.item(index).mainSource.guessPulldown(method)`
<br/>
`app.project.item(index).proxySource.guessPulldown(method)`
<br/>

**Description**

Sets `fieldSeparationType` and [removePulldown](#footagesource-removepulldown) to the best estimates for this footage source. If `isStill` is true, no change is made.

**Parameters**

| `method`   | The method to use for estimation. A `PulldownMethod` enumerated<br/>value, one of:<br/><br/>- `PulldownMethod.PULLDOWN_3_2`<br/>- `PulldownMethod.ADVANCE_24P`   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

Nothing.
