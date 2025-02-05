# After Effects Class Hierarchy

This section lists the class hierarchies for relevant AE API elements. For a primer on what this means, see [Javascript Classes](javascript.md#javascript-classes)

When using this guide, any objects that exist as part of a class hierarchy will note whether they exist as a subclass or base class (or both) of another object.

As it can be useful to see all available class hierarchies in one place, we've created this list below.

Note that some classes exist only as base classes, and demonstrate unexpected behaviour when type checking via `instanceof`, as noted in the table below. Classes with no symbol behave as expected.

#### Symbol Legend

| Symbol |                      Definition                      |
| ------ | ---------------------------------------------------- |
| ⚠      | `instanceof` is always `false`                       |
| ❌      | Class is undefined; `instanceof` will throw an error |

---

## Properties, Property Groups, and Layers

- [PropertyBase object](../property/propertybase.md) ⚠
    - [Property object](../property/property.md)
    - [PropertyGroup object](../property/propertygroup.md)
        - [MaskPropertyGroup object](../property/maskpropertygroup.md)
        - [Layer object](../layer/layer.md) ⚠
            - [AVLayer object](../layer/avlayer.md)
                - [ShapeLayer object](../layer/shapelayer.md)
                - [TextLayer object](../layer/textlayer.md)
            - [CameraLayer object](../layer/cameralayer.md)
            - [LightLayer object](../layer/lightlayer.md)

---

## Project Items

- [Item object](../item/item.md) ❌
    - [AVItem object](../item/avitem.md) ❌
        - [CompItem object](../item/compitem.md)
        - [FootageItem object](../item/footageitem.md)
    - [FolderItem object](../item/folderitem.md)

---

## Footage Item Sources

- [FootageSource object](../sources/footagesource.md) ❌
    - [FileSource object](../sources/filesource.md)
    - [PlaceholderSource object](../sources/placeholdersource.md)
    - [SolidSource object](../sources/solidsource.md)

---

## Collections

- [Collection object](../other/collection.md) ❌
    - [ItemCollection object](../item/itemcollection.md)
    - [LayerCollection object](../layer/layercollection.md)
    - [OMCollection object](../renderqueue/omcollection.md)
    - [RQItemCollection object](../renderqueue/rqitemcollection.md)
