.. highlight:: javascript
.. _ItemCollection:

ItemCollection object
################################################

``app.project.items``

**Description**

The ItemCollection object represents a collection of items. The ItemCollection belonging to a Project object contains all the Item objects for items in the project. The ItemCollection belonging to a FolderItem object contains all the Item objects for items in that folder.

    ItemCollection is a subclass of :ref:`Collection`. All methods and attributes of Collection, in addition to those listed below, are available when working with ItemCollection.

----

=======
Methods
=======

.. _ItemCollection.addComp:

ItemCollection.addComp()
*********************************************

``app.project.items.addComp(name, width, height, pixelAspect, duration, frameRate)``

**Description**

Creates a new composition. Creates and returns a new CompItem object and adds it to this collection. If the ItemCollection belongs to the project or the root folder, then the new item's ``parentFolder`` is the root folder. If the ItemCollection belongs to any other folder, the new item's ``parentFolder`` is that ``FolderItem``.

**Parameters**

===============  ==============================================================
``name``         A string containing the name of the composition.
``width``        The width of the composition in pixels, an integer in the
                 range ``[4..30000]``.
``height``       The height of the composition in pixels, an integer in the
                 range ``[4..30000]``.
``pixelAspect``  The pixel aspect ratio of the composition, a floating-point
                 value in the range ``[0.01..100.0]``.
``duration``     The duration of the composition in seconds, a floating-point
                 value in the range ``[0.0..10800.0]``.
``frameRate``    The frame rate of the composition, a floating-point value in
                 the range ``[1.0..99.0]``
===============  ==============================================================

**Returns**

CompItem object.

----

.. _ItemCollection.addFolder:

ItemCollection.addFolder()
*********************************************

``app.project.items.addFolder(name)``

**Description**

Creates a new folder. Creates and returns a new FolderItem object and adds it to this collection. If the ItemCollection belongs to the project or the root folder, then the new folder's ``parentFolder`` is the root folder. If the ItemCollection belongs to any other folder, the new folder's ``parentFolder`` is that ``FolderItem``. To put items in the folder, set the :ref:`item.parentFolder` attribute

**Parameters**

========  ============================================
``name``  A string containing the name of the folder.
========  ============================================

**Returns**

FolderItem object.

**Example**

This script creates a new FolderItem in the Project panel and moves compositions into it.

.. code:: javascript

    //create a new FolderItem in project, with name "comps"
    var compFolder = app.project.items.addFolder("comps");
    //move all compositions into new folder by setting
    //comp Item's parentFolder to "comps" folder
    for (var i = 1; i <= app.project.numItems; i++) {
      if (app.project.item(i) instanceof CompItem) {
        app.project.item(i).parentFolder = compFolder;
      }
    }
