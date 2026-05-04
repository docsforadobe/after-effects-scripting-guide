# ParametricMeshLayer object

`app.project.item(index).layer(index)`

!!! note
    This functionality was added in After Effects (Beta) 26.3 and is subject to change while it remains in Beta.

#### Description

The ParametricMeshLayer object represents a Parametric Mesh layer within a composition.

!!! info
	ParametricMeshLayer is a subclass of [AVLayer object](avlayer.md). It inherits the following properties and property groups from [AVLayer object](avlayer.md):

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

If the first item in the project is a CompItem, and the first layer of that CompItem is a ParametricMeshLayer, the following checks its type.

```javascript
var layer = app.project.item(1).layer(1);
if (layer instanceof ParametricMeshLayer)
{
    // do something
}
```

## Attributes

### ParametricMeshLayer.parametricMeshType

`app.project.item(index).layer(index).parametricMeshType`

!!! note
    This functionality was added in After Effects (Beta) 26.3 and is subject to change while it remains in Beta.

#### Description

For a parametric mesh layer, its mesh type. Trying to set this attribute for a non-parametric mesh layer produces an error.

#### Type

A `ParametricMeshType` enumerated value; read/write. One of:

- `ParametricMeshType.SPHERE`
- `ParametricMeshType.PLANE`
- `ParametricMeshType.CYLINDER`
- `ParametricMeshType.CONE`
- `ParametricMeshType.TORUS`
- `ParametricMeshType.CUBE`

---

### ParametricMeshLayer.parametricMeshOptions

`app.project.item(index).layer(index).parametricMeshOptions`

!!! note
    This functionality was added in After Effects (Beta) 26.3 and is subject to change while it remains in Beta.

#### Description

Gets/sets details about the structure of the parametric mesh.

#### Type

`ParametricMeshOptions` based on the ParametricMeshType of the layer, as follows.

#### For ParametricMeshType.CUBE
- `parametricMeshOptions.width`
- `parametricMeshOptions.height`
- `parametricMeshOptions.depth`
- `parametricMeshOptions.smoothingAngle`

#### For ParametricMeshType.SPHERE
- `parametricMeshOptions.radius`
- `parametricMeshOptions.sides`
- `parametricMeshOptions.sliceCaps`
- `parametricMeshOptions.sliceStart`
- `parametricMeshOptions.sliceEnd`
- `parametricMeshOptions.smoothingAngle`

#### For ParametricMeshType.PLANE
- `parametricMeshOptions.width`
- `parametricMeshOptions.length`
- `parametricMeshOptions.cornerRadius`
- `parametricMeshOptions.cornerSides`

#### For ParametricMeshType.TORUS
- `parametricMeshOptions.ringRadius`
- `parametricMeshOptions.pipeRadius`
- `parametricMeshOptions.ringSides`
- `parametricMeshOptions.pipeSides`
- `parametricMeshOptions.caps`
- `parametricMeshOptions.sliceStart`
- `parametricMeshOptions.sliceEnd`
- `parametricMeshOptions.smoothingAngle`

#### For ParametricMeshType.CONE
- `parametricMeshOptions.topRadius`
- `parametricMeshOptions.bottomRadius`
- `parametricMeshOptions.height`
- `parametricMeshOptions.sides`
- `parametricMeshOptions.topCap`
- `parametricMeshOptions.bottomCap`
- `parametricMeshOptions.sliceCaps`
- `parametricMeshOptions.sliceStart`
- `parametricMeshOptions.sliceEnd`
- `parametricMeshOptions.smoothingAngle`

#### For ParametricMeshType.CYLINDER
- `parametricMeshOptions.radius`
- `parametricMeshOptions.height`
- `parametricMeshOptions.sides`
- `parametricMeshOptions.topCap`
- `parametricMeshOptions.bottomCap`
- `parametricMeshOptions.sliceCaps`
- `parametricMeshOptions.sliceStart`
- `parametricMeshOptions.sliceEnd`
- `parametricMeshOptions.smoothingAngle`

---

### ParametricMeshLayer.parametricBevelOptions

`app.project.item(index).layer(index).parametricBevelOptions`

!!! note
    This functionality was added in After Effects (Beta) 26.3 and is subject to change while it remains in Beta.

#### Description

Gets/sets details about the beveling of the parametric mesh.

!!! info
	Only Parametric Mesh Layers with `ParametricMeshType.CUBE`, `ParametricMeshType.CONE`, and `ParametricMeshType.CYLINDER` have `parametricBevelOptions`.

#### Type

`ParametricBevelOptions` based on the ParametricMeshType of the layer, as follows.

#### For ParametricMeshType.CUBE
- `parametricBevelOptions.radius`
- `parametricBevelOptions.sides`

#### For ParametricMeshType.CONE
- `parametricBevelOptions.topRadius`
- `parametricBevelOptions.topSides`
- `parametricBevelOptions.bottomRadius`
- `parametricBevelOptions.bottomSides`

#### For ParametricMeshType.CYLINDER
- `parametricBevelOptions.radius`
- `parametricBevelOptions.sides`

---

