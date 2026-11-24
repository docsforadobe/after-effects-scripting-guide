# ShapeLayer object

`app.project.item(index).layer(index)`

#### Description

The ShapeLayer object represents a shape layer within a composition. Create it using [LayerCollection.addShape()](layercollection.md#layercollectionaddshape). It can be accessed in an item's layer collection either by index number or by a name string.

!!! info
    ShapeLayer is a subclass of [AVLayer](avlayer.md), which is a subclass of [Layer](layer.md). All methods and attributes of AVLayer and Layer are available when working with ShapeLayer.

## Attributes

### ShapeLayer.canAddOrRemoveMaterialOverride

`app.project.item(index).layer(index).canAddOrRemoveMaterialOverride`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

`true` if Shape layers support adding or removing material overrides.

Shape layers return `true` even when they are 2D or the composition uses another renderer. Material assignment access and override operations will fail unless the layer is 3D in an Advanced 3D composition.

#### Type

Boolean; read-only.

---

### ShapeLayer.materialAssignment

`app.project.item(index).layer(index).materialAssignment`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The layer's material assignment group. Material assignments are available when the Shape layer is 3D and the composition uses the Advanced 3D renderer. The front, bevel, side, and back assignments can be selected with `MaterialAssignment.FRONT`, `MaterialAssignment.BEVEL`, `MaterialAssignment.SIDE`, and `MaterialAssignment.BACK`.

Each assignment's [material properties](../property/materialpropertygroup.md#ae-properties) depend on its source and projection mode. A default source exposes no additional material properties or texture transforms. Substance and layer sources expose texture controls, and a layer source also exposes material properties such as Opacity, Roughness, and Metallic.

#### Type

[MaterialAssignmentPropertyGroup object](../property/materialassignmentpropertygroup.md); read-only.

---

### ShapeLayer.materialAssignmentCount

`app.project.item(index).layer(index).materialAssignmentCount`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The total number of material assignments available on a 3D Shape layer in an Advanced 3D composition. The value is 4 for the front, bevel, side, and back assignments, including assignments whose override has not been added. This value is the same as `materialAssignment.numProperties`.

#### Type

Integer; read-only.

---

## Methods

### ShapeLayer.addAllMaterialOverrides()

`app.project.item(index).layer(index).addAllMaterialOverrides()`

!!! warning
    This functionality is in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

Adds every material override that is not already present, preserving existing material sources and property values.

On layers that support adding or removing overrides, this method does nothing if all overrides are already present.

The layer must be 3D, have available material assignments, and belong to a composition that uses the Advanced 3D renderer.

#### Parameters

None.

#### Returns

Nothing.

---
