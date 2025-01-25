# MaskPropertyGroup object

`app.project.item(index).layer(index).mask`

#### Description

The MaskPropertyGroup object encapsulates mask attributes in a layer.

!!! info
    MaskPropertyGroup is a subclass of [PropertyGroup object](propertygroup.md). All methods and attributes of [PropertyBase object](propertybase.md) and PropertyGroup, in addition to those listed below, are available when working with MaskPropertyGroup.

---

## Attributes

### MaskPropertyGroup.color

`app.project.item(index).layer(index).mask(index).color`

#### Description

The color used to draw the mask outline as it appears in the user interface (Composition panel, Layer panel, and Timeline panel).

#### Type

Array of three floating-point values, `[R, G, B]`, in the range `[0.0..1.0]`; read/write.

---

### MaskPropertyGroup.inverted

`app.project.item(index).layer(index).mask(index).inverted`

#### Description

When `true`, the mask is inverted; otherwise `false`.

#### Type

Boolean; read/write.

---

### MaskPropertyGroup.locked

`app.project.item(index).layer(index).mask(index).locked`

#### Description

When `true`, the mask is locked and cannot be edited in the user interface; otherwise `false`.

#### Type

Boolean; read/write.

---

### MaskPropertyGroup.maskFeatherFalloff

`app.project.item(index).layer(index).mask(index).maskFeatherFalloff`

#### Description

The feather falloff mode for the mask. Equivalent to the Layer > Mask > Feather Falloff setting.

#### Type

A `MaskFeatherFalloff` enumerated value; read/write. One of:

- `MaskFeatherFalloff.FFO_LINEAR`
- `MaskFeatherFalloff.FFO_SMOOTH`

---

### MaskPropertyGroup.maskMode

`app.project.item(index).layer(index).mask(index).maskMode`

#### Description

The masking mode for this mask.

#### Type

A `MaskMode` enumerated value; read/write. One of:

- `MaskMode.NONE`
- `MaskMode.ADD`
- `MaskMode.SUBTRACT`
- `MaskMode.INTERSECT`
- `MaskMode.LIGHTEN`
- `MaskMode.DARKEN`
- `MaskMode.DIFFERENCE`

---

### MaskPropertyGroup.maskMotionBlur

`app.project.item(index).layer(index).mask(index).maskMotionBlur`

#### Description

How motion blur is applied to this mask.

#### Type

A `MakMotionBlur` enumerated value; read/write. One of:

- `MaskMotionBlur.SAME_AS_LAYER`
- `MaskMotionBlur.ON`
- `MaskMotionBlur.OFF`

---

### MaskPropertyGroup.rotoBezier

`app.project.item(index).layer(index).mask(index).rotoBezier`

#### Description

When `true`, the mask is a RotoBezier shape; otherwise `false`.

#### Type

Boolean; read/write.
