.. _RQItemCollection:

RQItemCollection object
################################################

``app.project.renderQueue.items``

**Description**

The RQItemCollection contains all of the render-queue items in a project, as shown in the Render Queue panel of the project. The collection provides access to the :ref:`RenderQueueItem objects <RenderQueueItem>`, and allows you to create them from compositions. The first RenderQueueItem object in the collection is at index position 1.

    RQItemCollection is a subclass of :ref:`Collection`. All methods and attributes of Collection are available when working with RQItemCollection.

----

=======
Methods
=======

.. _RQItemCollection.add:

RQItemCollection.add()
*********************************************

``app.project.renderQueue.items.add(comp)``

**Description**

Adds a composition to the Render Queue, creating a RenderQueueItem.

**Parameters**

========  ====================================================
``comp``  The CompItem object for the composition to be added.
========  ====================================================


**Returns**

:ref:`RenderQueueItem`.
