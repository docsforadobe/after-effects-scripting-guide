# MaterialPropertyGroup object

`app.project.item(index).layer(index).materialAssignment.property(index)`

!!! note
    This functionality was added in After Effects (Beta) 27.1 and is subject to change while it remains in Beta.

#### Description

The MaterialPropertyGroup object represents one material assignment on a material-capable layer. It provides access to the material properties and to the assignment's source and override state.

!!! info
    MaterialPropertyGroup is a subclass of [PropertyGroup object](propertygroup.md). All PropertyGroup methods and attributes are available on a MaterialPropertyGroup.

!!! warning
    `materialSource` is read-only. Use `setMaterialOverride()` to assign or reset the source.

#### AE Properties

The available AE properties depend on the receiving layer type, [materialSource](#materialpropertygroupmaterialsource), and selected projection mode. The following properties are available on an added override, subject to the [layer and renderer requirements](materialassignmentpropertygroup.md#availability):

- `Ambient`
- `Base Color`
- `Blend Softness`
- `Emission Color`
- `Emission Intensity`
- `Metallic`
- `Opacity`
- `Projection Mode`
- `Randomize Offset`
- `Randomize Offset Seed`
- `Roughness`
- `Texture Offset`
- `Texture Rotation`
- `Texture Scale`
- `Uniform Tiling`

| Material source | Available properties |
| --- | --- |
| Default (`materialSource === null`) | Parametric meshes: `Ambient`, `Base Color`, `Emission Color`, `Emission Intensity`, `Metallic`, and `Roughness`. Imported models: `Texture Offset`, `Texture Rotation`, and `Texture Scale`. Text and Shape layers: none. |
| Substance material item | Texture transforms and projection controls. Material appearance comes from the Substance item. |
| Eligible layer | Texture transforms and projection controls, plus `Ambient`, `Emission Color`, `Emission Intensity`, `Metallic`, `Opacity`, and `Roughness`. Material color comes from the source layer's rendered pixels. |

`Blend Softness` requires Triplanar projection. `Uniform Tiling`, `Randomize Offset`, and `Randomize Offset Seed` are available only on 3D Text and Shape layers with a Substance or layer source. `Uniform Tiling` is unavailable with Triplanar projection. `Randomize Offset Seed` remains accessible when `Randomize Offset` is off.

#### Example

```javascript
var material = textLayer.materialAssignment.property(MaterialAssignment.FRONT);
material.setMaterialOverride(sourceLayer);
// Retrieve the group again because its available properties can change.
material = textLayer.materialAssignment.property(MaterialAssignment.FRONT);
material.property("Roughness").setValue(50);
```

---

## Attributes

### MaterialPropertyGroup.isOverride

`app.project.item(index).layer(index).materialAssignment.property(index).isOverride`

#### Description

`true` if the material override has been added for this assignment; otherwise `false`.

Some layers, such as parametric meshes and single-material 3D models, always have their material override present. On text, shape, and multi-material 3D model layers, an override can be added or removed when the layer reports `canAddOrRemoveMaterialOverride` as `true`.

#### Type

Boolean; read-only.

---

### MaterialPropertyGroup.materialSource

`app.project.item(index).layer(index).materialAssignment.property(index).materialSource`

#### Description

The source currently assigned to the material. The value is:

- A [FootageItem object](../item/footageitem.md) whose footage is a Substance material.
- An eligible visual [AVLayer object](../layer/avlayer.md) from the same composition. The layer can be 2D.
- `null` when the assignment uses its default material.

The following layers are ineligible as material sources:

- The layer receiving the material assignment.
- A layer in another composition.
- A null layer.
- An adjustment layer.
- An imported 3D model layer.
- A Parametric Mesh Layer.
- An audio-only layer.
- A layer that depends on the target layer and would create a circular material dependency.

An unadded material override is readable and returns `null`.

#### Type

FootageItem object, AVLayer object, or `null`; read-only.

---

## Methods

### MaterialPropertyGroup.removeMaterialOverride()

`app.project.item(index).layer(index).materialAssignment.property(index).removeMaterialOverride()`

#### Description

Removes the material override and resets its source, property values, keyframes, and expressions to the layer's default material state.

The layer's `canAddOrRemoveMaterialOverride` and the assignment's `isOverride` attributes must both be `true` before calling this method.

#### Parameters

None.

#### Returns

Nothing.

---

### MaterialPropertyGroup.setMaterialOverride()

`app.project.item(index).layer(index).materialAssignment.property(index).setMaterialOverride([materialSource])`

#### Description

Adds the material override if necessary, then assigns the supplied material source. Passing no argument or `null` adds or updates the override with the default material. The override remains added after resetting its source to the default.

A project item source must be a Substance material item. Assigning the same source again is allowed.

A layer source must be a suitable visual AVLayer with a nonempty name in the same composition. It may be a 2D layer. See [materialSource](#materialpropertygroupmaterialsource) for the complete list of ineligible layer types and references.

An invalid source is rejected before the material override is added or changed.

#### Parameters

| Parameter        | Type                            | Description                                                                                 |
| ---------------- | ------------------------------- | ------------------------------------------------------------------------------------------- |
| `materialSource` | Substance FootageItem object or AVLayer object | Optional material source. If omitted or `null`, the default material is selected. |

#### Returns

Nothing.

---
