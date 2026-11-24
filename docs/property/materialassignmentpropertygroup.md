# MaterialAssignmentPropertyGroup object

`app.project.item(index).layer(index).materialAssignment`

!!! note
    This functionality was added in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The MaterialAssignmentPropertyGroup object contains the material assignments for a [ParametricMeshLayer object](../layer/parametricmeshlayer.md), [ThreeDModelLayer object](../layer/threedmodellayer.md), 3D [ShapeLayer object](../layer/shapelayer.md), and 3D [TextLayer object](../layer/textlayer.md).

Each assignment is a MaterialPropertyGroup whose [child material properties](materialpropertygroup.md#ae-properties) depend on the receiving layer type, material source, and projection mode.

!!! info
    MaterialAssignmentPropertyGroup is a subclass of [PropertyGroup object](propertygroup.md). All PropertyGroup methods and attributes are available on a MaterialAssignmentPropertyGroup.

The group can be accessed from the layer's `materialAssignment` attribute:

```javascript
var materialAssignments = layer.materialAssignment;
```

For match names, see [3D layer match names](../matchnames/layer/3dlayer.md#materials).

## Availability

### Layer requirements

Material assignments are available on [parametric mesh layers](../layer/parametricmeshlayer.md) and [imported 3D model layers](../layer/threedmodellayer.md).

[Text layers](../layer/textlayer.md) and [shape layers](../layer/shapelayer.md) support material assignments when they are 3D layers in a composition that uses the Advanced 3D renderer.

Other layer types do not support material assignments.

### Override state

Parametric mesh layers and single-material 3D model layers always have a material override. You can change its source, but you cannot add or remove the override.

Text layers, shape layers, and 3D model layers with multiple materials let you add or remove an override for each material assignment independently.

You can look up an assignment and read its [isOverride](materialpropertygroup.md#materialpropertygroupisoverride) and [materialSource](materialpropertygroup.md#materialpropertygroupmaterialsource) attributes even before adding its override. If `isOverride` is `false`, call [setMaterialOverride()](materialpropertygroup.md#materialpropertygroupsetmaterialoverride) before editing its material properties.

Setting the source to `null` selects the default material without removing the override.

## MaterialAssignment enum

The `MaterialAssignment` enumerated values identify material slots that have a known semantic role:

- `MaterialAssignment.FRONT`
- `MaterialAssignment.BEVEL`
- `MaterialAssignment.SIDE`
- `MaterialAssignment.BACK`
- `MaterialAssignment.DEFAULT`

`FRONT`, `BEVEL`, `SIDE`, and `BACK` select slots on 3D TextLayer and ShapeLayer objects. `DEFAULT` selects the material assignment on a ParametricMeshLayer. ThreeDModelLayer material names are model-defined, so access its slots by index or exact name.

## Methods

### MaterialAssignmentPropertyGroup.property()

`app.project.item(index).layer(index).materialAssignment.property(indexOrAssignmentOrName)`

#### Description

Finds and returns a material assignment by its 1-based index, a `MaterialAssignment` value, or an exact display name, English name, or match name. A valid index returns the slot even when its override has not been added.

The object can also be called directly as a shortcut:

```javascript
var front = textLayer.materialAssignment(MaterialAssignment.FRONT);
var sameFront = textLayer.materialAssignment.property(MaterialAssignment.FRONT);
var modelMaterial = modelLayer.materialAssignment.property("Material_MR");
var meshMaterial = meshLayer.materialAssignment.property(MaterialAssignment.DEFAULT);
```

Names are case-sensitive and must match the full display name, English name, or match name. Partial or unknown names return `null`; if duplicate names exist, the first match is returned.

An assignment enum is valid only for the corresponding layer type:

- Text and shape layers accept `FRONT`, `BEVEL`, `SIDE`, and `BACK`.
- Parametric mesh layers accept `DEFAULT`.
- Imported 3D models do not support assignment enum values; use an index or exact name.

Using an assignment enum that is not valid for the layer raises an error.

#### Parameters

| Parameter                       | Type            | Description                                                                                  |
| ------------------------------- | --------------- | -------------------------------------------------------------------------------------------- |
| `indexOrAssignmentOrName`       | Integer, `MaterialAssignment`, or String | A 1-based material index, a supported `MaterialAssignment` value, or an exact material name. |

#### Returns

[MaterialPropertyGroup object](materialpropertygroup.md), or `null` if a string name is not found. A non-integer outside the supported enum values is interpreted as a name, and an out-of-range integer reports a range error.

---
