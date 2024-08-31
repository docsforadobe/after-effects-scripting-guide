.. _OMCollection:

OMCollection object
################################################

``app.project.renderQueue.items.outputModules``

**Description**

The OMCollection contains all of the output modules in a render queue. The collection provides access to the :ref:`OutputModule objects <OutputModule>`, and allows you to create them. The first OutputModule object in the collection is at index position 1.

    OMCollection is a subclass of :ref:`Collection`. All methods and attributes of Collection are available when working with OMCollection.

----

=======
Methods
=======

.. _OMCollection.add:

OMCollection.add()
*********************************************

``app.project.renderQueue.item(1).ouputModules.add()``

**Description**

Adds a new Output Module to the Render Queue Item, creating an OutputModule.

**Returns**

:ref:`OutputModule`.
