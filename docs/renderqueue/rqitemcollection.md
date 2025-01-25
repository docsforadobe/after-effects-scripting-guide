# RQItemCollection object

`app.project.renderQueue.items`

#### Description

The RQItemCollection contains all of the render-queue items in a project, as shown in the Render Queue panel of the project. The collection provides access to the [RenderQueueItem objects](renderqueueitem.md), and allows you to create them from compositions. The first RenderQueueItem object in the collection is at index position 1.

!!! info
    RQItemCollection is a subclass of [Collection object](../other/collection.md). All methods and attributes of Collection are available when working with RQItemCollection.

---

## Methods

### RQItemCollection.add()

`app.project.renderQueue.items.add(comp)`

#### Description

Adds a composition to the Render Queue, creating a RenderQueueItem.

#### Parameters

| Parameter |                  Type                   |         Description          |
| --------- | --------------------------------------- | ---------------------------- |
| `comp`    | [CompItem object](../item/compitem.md) | The composition to be added. |

#### Returns

[RenderQueueItem object](renderqueueitem.md).
