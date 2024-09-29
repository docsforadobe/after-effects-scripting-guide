<a id="omcollection"></a>

# OMCollection object

`app.project.renderQueue.items.outputModules`

**Description**

The OMCollection contains all of the output modules in a render queue. The collection provides access to the [OutputModule objects](outputmodule.md#outputmodule), and allows you to create them. The first OutputModule object in the collection is at index position 1.

> OMCollection is a subclass of [Collection object](../other/collection.md#collection). All methods and attributes of Collection are available when working with OMCollection.

---

## Methods

<a id="omcollection-add"></a>

### OMCollection.add()

`app.project.renderQueue.item(1).ouputModules.add()`

**Description**

Adds a new Output Module to the Render Queue Item, creating an OutputModule.

**Returns**

[OutputModule object](outputmodule.md#outputmodule).
