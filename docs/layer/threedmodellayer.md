# ThreeDModelLayer object

`app.project.item(index).layer(index)`

!!! note
    This functionality was added in After Effects 24.4

#### Description

The ThreeDModelLayer object represents a 3D Model layer within a composition.

!!! info
    ThreeDModelLayer is a subclass of [AVLayer object](avlayer.md). All methods and attributes of AVLayer are available when working with ThreeDModelLayer.

#### AE Properties

ThreeDModelLayer inherits the following properties and property groups from [AVLayer object](avlayer.md):

- Marker
- Time Remap
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
- Audio
    - AudioLevels

#### Example

If the first item in the project is a CompItem, and the first layer of that CompItem is an ThreeDModelLayer, the following checks its type.

```javascript
var modelLayer = app.project.item(1).layer(1);
if (modelLayer instanceof ThreeDModelLayer)
{
    // do something
}
```

## Attributes

### ThreeDModelLayer.canAddOrRemoveMaterialOverride

`app.project.item(index).layer(index).canAddOrRemoveMaterialOverride`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

`true` if this layer type supports adding or removing material overrides. This indicates type support, not whether any material override currently exists.

A single-material model has an always-present override and returns `false`; a multi-material model returns `true`.

#### Type

Boolean; read-only.

---

### ThreeDModelLayer.materialAssignment

`app.project.item(index).layer(index).materialAssignment`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The layer's material assignment group. Imported 3D models can contain multiple model-defined material names. Access assignments by 1-based index or exact name.

Each assignment exposes Texture Offset, Texture Rotation, and Texture Scale even for the default material. Other [material properties](../property/materialpropertygroup.md#ae-properties) depend on the source and projection mode. Uniform Tiling and Randomize Offset are not available on imported model layers.

#### Type

[MaterialAssignmentPropertyGroup object](../property/materialassignmentpropertygroup.md); read-only.

---

### ThreeDModelLayer.materialAssignmentCount

`app.project.item(index).layer(index).materialAssignmentCount`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The total number of material assignments defined by the imported 3D model, including assignments whose material override has not been added. This value is the same as `materialAssignment.numProperties`.

If the model has no available material assignments, accessing this attribute fails rather than returning 0.

#### Type

Integer; read-only.

---

## Methods

### ThreeDModelLayer.addAllMaterialOverrides()

`app.project.item(index).layer(index).addAllMaterialOverrides()`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

Adds every material override that is not already present, preserving existing material sources and property values.

On layers that support adding or removing overrides, this method does nothing if all overrides are already present.

This method requires a layer that supports adding or removing overrides and has available material assignments.

Single-material models always have their material override present, so this method is not supported on those layers.

#### Parameters

None.

#### Returns

Nothing.

---
