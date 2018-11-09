.. highlight:: javascript
.. _Item:

Item object
################################################

|  ``app.project.item(index)``
|  ``app.project.items[index]``

**Description**

The Item object represents an item that can appear in the Project panel. The first item is at index 1.

    Item is the base class for :ref:`AVItem` and for :ref:`FolderItem`, which are in turn the base classes for various other item types, so Item attributes and methods are available when working with all of these item types.

**Example**

This example gets the second item from the project and checks that it is a folder. It then removes from thefolder any top-level item that is not currently selected. It also checks to make sure that, for each item in thefolder, the parent is properly set to the correct folder.

::

    var myFolder = app.project.item(2);
    if (myFolder.typeName != "Folder") {
        alert("error: second item is not a folder");
    }
    else {
        var numInFolder = myFolder.numItems;
        //Always run loops backwards when deleting things:
        for(i = numInFolder; i >= 1; i--) {
            var curItem = myFolder.item(i);
            if(curItem.parentFolder != myFolder) {
                alert("error within AE: the parentFolder is not set correctly");
            }
            else {
                if(!curItem.selected && curItem.typeName == "Footage")
                {
                    //found an unselected solid.
                    curItem.remove();
                }
            }
        }
    }

----

==========
Attributes
==========

.. _Item.comment:

Item.comment
*********************************************

``app.project.item(index).comment``

**Description**

A string that holds a comment, up to 15,999 bytes in length after any encoding conversion. The comment is for the user's purpose only; it has no effect on the item's appearance or behavior.

**Type**

String; read/write.

----

.. _Item.id:

Item.id
*********************************************

``app.project.item(index).id``

**Description**

A unique and persistent identification number used internally to identify an item between sessions. The value of the ID remains the same when the project is saved to a file and later reloaded. However, when you import this project into another project, new IDs are assigned to all items in the imported project. The ID is not displayed anywhere in the user interface.

**Type**

Integer; read-only.

----

.. _Item.label:

Item.label
*********************************************

``app.project.item(index).label``

**Description**

The label color for the item. Colors are represented by their number (0 for None, or 1 to 16 for one of the preset colors in the Labels preferences). Custom label colors cannot be set programmatically.

**Type**

Integer (0 to 16); read/write.

----

.. _Item.name:

Item.name
*********************************************

``app.project.item(index).name``

**Description**

The name of the item as displayed in the Project panel.

**Type**

String; read/write.

----

.. _Item.parentFolder:

Item.parentFolder
*********************************************

``app.project.item(index).parentFolder``

**Description**

The FolderItem object for the folder that contains this item. If this item is at the top level of the project, this is the project's root folder (``app.project.rootFolder``). You can use :ref:`ItemCollection.addFolder` to add a new folder, and set this value to put items in the new folder.

**Type**

FolderItem object; read/write.

**Example**

This script creates a new FolderItem in the Project panel and moves compositions into it.

::

    //create a new FolderItem in project, with name "comps"
    var compFolder = app.project.items.addFolder("comps");

    //move all compositions into new folder by setting
    //compItem's parentFolder to "comps" folder
    for(var i = 1; i <= app.project.numItems; i++){
        if(app.project.item(i) instanceof CompItem)
          app.project.item(i).parentFolder = compFolder;
    }

----

.. _Item.selected:

Item.selected
*********************************************

``app.project.item(index).selected``

**Description**

When true, this item is selected. Multiple items can be selected at the same time. Set to true to select the item programmatically, or to false to deselect it.

**Type**

Boolean; read/write.

----

.. _Item.typeName:

Item.typeName
*********************************************

``app.project.item(index).typeName``

**Description**

A user-readable name for the item type; for example, "Folder", "Footage", or "Composition".

**Type**

String; read-only.

----

=======
Methods
=======

.. _Item.remove:

Item.remove()
*********************************************

``app.project.item(index).remove()``

**Description**

Deletes this item from the project and from the Project panel. If the item is a FolderItem, all the items contained in the folder are also removed from the project. No files or folders are removed from disk.

**Parameters**

None.

**Returns**

Nothing.