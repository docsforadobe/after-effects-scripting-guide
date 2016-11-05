.. _Collection:

Collection object
################################################

Like an array, a collection associates a set of objects or values as a logical group and provides access to them by index. However, most collection objects are read-only. You do not assign objects to them yourself—their contents update automatically as objects are created or deleted.

.. note::
   The index numbering of a collection starts with 1, not 0.

=======
Objects
=======

-  :ref:`ItemCollection` All of the items (imported files, folders, solids, and so on) found in the Project panel.
-  :ref:`LayerCollection` All of the layers in a composition.
-  :ref:`OMCollection` All of the Output Module items in the project.
-  :ref:`RQItemCollection` All of the render-queue items in the project.

----

==========
Attributes
==========

==========  ========================================
``length``  The number of objects in the collection.
==========  ========================================

-----

=======
Methods
=======

==========  ==============================================================
``[]``      Retrieves an object in the collection by its index number. The
            first object is at index 1.
==========  ==============================================================
