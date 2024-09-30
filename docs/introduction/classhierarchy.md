# After Effects Class Hierarchy

This section lists the class hierarchies for relevant AE API elements. For a primer on what this means, see [Javascript Classes](javascript.md#javascriptclasses)

When using this guide, any objects that exist as part of a class hierarchy will note whether they exist as a subclass or base class (or both) of another object.

As it can be useful to see all available class hierarchies in one place, we've created this list below.

Note that some classes exist only as base classes, and demonstrate unexpected behaviour when type checking via `instanceof`, as noted in the table below. Classes with no symbol behave as expected.

#### Symbol Legend

| ⚠   | `instanceof` is always `false`                       |
|-----|------------------------------------------------------|
| ❌   | Class is undefined; `instanceof` will throw an error |

---

## Properties, Property Groups, and Layers

- [PropertyBase object](../properties/propertybase.md) ⚠
  - [Property object](../properties/property.md)
  - [PropertyGroup object](../properties/propertygroup.md)
    - [MaskPropertyGroup object](../properties/maskpropertygroup.md)
    - [Layer object](../layers/layer.md) ⚠
      - [AVLayer object](../layers/avlayer.md)
        - [ShapeLayer object](../layers/shapelayer.md)
        - [TextLayer object](../layers/textlayer.md)
      - [CameraLayer object](../layers/cameralayer.md)
      - [LightLayer object](../layers/lightlayer.md)

---

## Project Items

- [Item object](../items/item.md) ❌
  - [AVItem object](../items/avitem.md) ❌
    - [CompItem object](../items/compitem.md)
    - [FootageItem object](../items/footageitem.md)
  - [FolderItem object](../items/folderitem.md)

---

## Footage Item Sources

- [FootageSource object](../sources/footagesource.md) ❌
  - [FileSource object](../sources/filesource.md)
  - [PlaceholderSource object](../sources/placeholdersource.md)
  - [SolidSource object](../sources/solidsource.md)

---

## Collections

- [Collection object](../other/collection.md) ❌
  - [ItemCollection object](../items/itemcollection.md)
  - [LayerCollection object](../layers/layercollection.md)
  - [OMCollection object](../renderqueue/omcollection.md)
  - [RQItemCollection object](../renderqueue/rqitemcollection.md)
