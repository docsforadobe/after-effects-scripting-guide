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
