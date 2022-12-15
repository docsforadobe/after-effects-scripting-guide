.. _ClassHierarchy:

After Effects Class Hierarchy
#############################

**Class Inheritance**

In Javascript/Extendscript, Class Inheritance is the idea that you can define some properties or methods for a given object, and then create a *subclass* (or "child class") that inherits all of those properties & methods and adds more, further refining it.

For example, "automobile" could be one base class, with "cars" being a subclass of the "automobile" base class, with "sedan" and "convertible" being two subclasses of the "car" base class. Any properties or methods from "automobile" are also accessible by "convertible," because there's a direct inheritance from "automobile" -> "car" -> "convertible".

**Class Inheritance in After Effects**

The same idea exists in After Effects scripting. Many API-accessible elements are part of class hierarchies that inherit and refine properties & methods. This lets the After Effects developers use existing structures to create new API-accessible components, and it allows script developers to use this same hierarchy to work with the After Effects DOM.

For example, :ref:`Layer` is a *subclass* of :ref:`PropertyGroup` and is the *base class* for :ref:`AVLayer`, :ref:`CameraLayer`, and :ref:`LightLayer`. This means that CameraLayer inherits everything from the Layer document, which inherits everything from the PropertyGroup document, which inherits everything from the PropertyBase document.

This is why you won't see the ``name`` or ``enabled`` parameters on the Layer page, but you can still use ``layer.name`` in your script; ``name`` is inherited from :ref:`PropertyBase.name`.

.. warning::
   In a few specific cases, properties & methods are **removed** with inheritance, not just added. Those cases are noted on the relevant object page.

**Checking Classes**

Typically in Javascript, you can use ``instanceof`` to check whether any given element matches an expected object type.

Keep in mind that you will need to check against the *most specific* class possible; an AE Text Layer will only return ``true`` for ``layer instanceof TextLayer``, and ``false`` for all parent classes (``layer instanceof AVLayer``, ``layer instanceof Layer``, etc.)

With that said, there exist some elements in the API that are *only* base classes for other classes; they exist to hold inherited properties & methods, but no DOM element is exactly of this type.

When checking ``object instanceof {class}`` with these classes, AE will either throw an error that ``{class} is undefined`` or return ``false``, depending on how the class was implemented. The list below documents which base-only classes report which behaviours.

----

=====================
Class Hierarchy Lists
=====================

When using this guide, any objects that exist as part of a class hierarchy will note whether they exist as a subclass or base class (or both) of another object.

As it can be useful to see all available class hierarchies in one place, we've created this list below.

Note that some classes exist only as base classes, and demonstrate unexpected behaviour when type checking via ``instanceof``, as noted in the table below.

**Symbol Legend**

==  ======================================================
✔   ``instanceof`` evaluates correctly
⚠   ``instanceof`` is always ``false``
❌   Class is undefined; ``instanceof`` will throw an error
==  ======================================================

----

.. _ClassHierarchy.properties:

Properties, Property Groups, and Layers
*********************************************

- :ref:`PropertyBase` ⚠

  - :ref:`Property` ✔
  - :ref:`PropertyGroup` ✔

    - :ref:`MaskPropertyGroup` ✔
    - :ref:`Layer` ⚠

      - :ref:`AVLayer` ✔

        - :ref:`ShapeLayer` ✔
        - :ref:`TextLayer` ✔

      - :ref:`CameraLayer` ✔
      - :ref:`LightLayer` ✔

----

.. _ClassHierarchy.items:

Project Items
*********************************************

- :ref:`Item` ❌

  - :ref:`AVItem` ❌

    - :ref:`CompItem` ✔
    - :ref:`FootageItem` ✔

  - :ref:`FolderItem` ✔

----

.. _ClassHierarchy.sources:

Footage Item Sources
*********************************************

- :ref:`FootageSource` ❌

  - :ref:`FileSource` ✔
  - :ref:`PlaceholderSource` ✔
  - :ref:`SolidSource` ✔

----

.. _ClassHierarchy.collections:

Collections
*********************************************

- :ref:`Collection` ❌

  - :ref:`ItemCollection` ✔
  - :ref:`LayerCollection` ✔
  - :ref:`OMCollection` ✔
  - :ref:`RQItemCollection` ✔
