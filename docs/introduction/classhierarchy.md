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

- [PropertyBase object](../properties/propertybase.md#propertybase) ⚠
  - [Property object](../properties/property.md#property)
  - [PropertyGroup object](../properties/propertygroup.md#propertygroup)
    - [MaskPropertyGroup object](../properties/maskpropertygroup.md#maskpropertygroup)
    - [Layer object](../layers/layer.md#layer) ⚠
      - [AVLayer object](../layers/avlayer.md#avlayer)
        - [ShapeLayer object](../layers/shapelayer.md#shapelayer)
        - [TextLayer object](../layers/textlayer.md#textlayer)
      - [CameraLayer object](../layers/cameralayer.md#cameralayer)
      - [LightLayer object](../layers/lightlayer.md#lightlayer)

---

## Project Items

- [Item object](../items/item.md#item) ❌
  - [AVItem object](../items/avitem.md#avitem) ❌
    - [CompItem object](../items/compitem.md#compitem)
    - [FootageItem object](../items/footageitem.md#footageitem)
  - [FolderItem object](../items/folderitem.md#folderitem)

---

## Footage Item Sources

- [FootageSource object](../sources/footagesource.md#footagesource) ❌
  - [FileSource object](../sources/filesource.md#filesource)
  - [PlaceholderSource object](../sources/placeholdersource.md#placeholdersource)
  - [SolidSource object](../sources/solidsource.md#solidsource)

---

## Collections

- [Collection object](../other/collection.md#collection) ❌
  - [ItemCollection object](../items/itemcollection.md#itemcollection)
  - [LayerCollection object](../layers/layercollection.md#layercollection)
  - [OMCollection object](../renderqueue/omcollection.md#omcollection)
  - [RQItemCollection object](../renderqueue/rqitemcollection.md#rqitemcollection)
