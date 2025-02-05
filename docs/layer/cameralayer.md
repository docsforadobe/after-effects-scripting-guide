# CameraLayer object

`app.project.item(index).layer(index)`

#### Description

The CameraLayer object represents a camera layer within a composition. Create it using [LayerCollection.addCamera()](layercollection.md#layercollectionaddcamera). It can be accessed in an item's layer collection either by index number or by a name string.

!!! info
    CameraLayer is a subclass of [Layer object](layer.md). All methods and attributes of Layer are available when working with CameraLayer.

#### AE Properties

CameraLayer defines no additional attributes, but has different AE properties than other layer types. It has the following properties and property groups:

- `Marker`
- `Transform`
    - `PointofInterest`
    - `Position`
    - `Scale`
    - `Orientation`
    - `XRotation`
    - `YRotation`
    - `Rotation`
    - `Opacity`
- `CameraOptions`
    - `Zoom`
    - `DepthofField`
    - `FocusDistance`
    - `BlurLevel`
