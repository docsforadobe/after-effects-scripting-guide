# Collection object

#### Description

Like an array, a collection associates a set of objects or values as a logical group and provides access to them by index. However, most collection objects are read-only. You do not assign objects to them yourself—their contents update automatically as objects are created or deleted.

!!! tip
    The index numbering of a collection starts with 1, not 0.

## Objects

- [ItemCollection object](../item/itemcollection.md) All of the items (imported files, folders, solids, and so on) found in the Project panel.
- [LayerCollection object](../layer/layercollection.md) All of the layers in a composition.
- [OMCollection object](../renderqueue/omcollection.md) All of the Output Module items in the project.
- [RQItemCollection object](../renderqueue/rqitemcollection.md) All of the render-queue items in the project.

---

## Attributes

| Attribute |  Type   |               Description                |
| --------- | ------- | ---------------------------------------- |
| `length`  | Integer | The number of objects in the collection. |

---

## Methods

| Method | Return Type |                                        Description                                         |
| ------ | ----------- | ------------------------------------------------------------------------------------------ |
| `[]`   | Object      | Retrieves an object in the collection by its index number. The first object is at index 1. |
