.. _ClassHierarchy:

After Effects Class Hierarchy
#############################

This section lists the class hierarchies for relevant AE API elements. For a primer on what this means, see :ref:`Javascript.Classes`

When using this guide, any objects that exist as part of a class hierarchy will note whether they exist as a subclass or base class (or both) of another object.

As it can be useful to see all available class hierarchies in one place, we've created this list below.

Note that some classes exist only as base classes, and demonstrate unexpected behaviour when type checking via ``instanceof``, as noted in the table below. Classes with no symbol behave as expected.

**Symbol Legend**

==  ======================================================
⚠   ``instanceof`` is always ``false``
❌   Class is undefined; ``instanceof`` will throw an error
==  ======================================================

----

.. _ClassHierarchy.properties:

Properties, Property Groups, and Layers
*********************************************

- :ref:`PropertyBase` ⚠

  - :ref:`Property`

  - :ref:`PropertyGroup`

    - :ref:`MaskPropertyGroup`

    - :ref:`Layer` ⚠

      - :ref:`AVLayer`

        - :ref:`ShapeLayer`

        - :ref:`TextLayer`

      - :ref:`CameraLayer`

      - :ref:`LightLayer`

----

.. _ClassHierarchy.items:

Project Items
*********************************************

- :ref:`Item` ❌

  - :ref:`AVItem` ❌

    - :ref:`CompItem`

    - :ref:`FootageItem`

  - :ref:`FolderItem`

----

.. _ClassHierarchy.sources:

Footage Item Sources
*********************************************

- :ref:`FootageSource` ❌

  - :ref:`FileSource`

  - :ref:`PlaceholderSource`

  - :ref:`SolidSource`

----

.. _ClassHierarchy.collections:

Collections
*********************************************

- :ref:`Collection` ❌

  - :ref:`ItemCollection`

  - :ref:`LayerCollection`

  - :ref:`OMCollection`

  - :ref:`RQItemCollection`
