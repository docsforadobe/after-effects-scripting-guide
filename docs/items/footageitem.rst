.. _FootageItem:

FootageItem object
################################################

``app.project.item(index)``
``app.project.items[index]``

**Description**

The FootageItem object represents a footage item imported into a project, which appears in the Project panel. These are accessed by position index number in a project's item collection.

    FootageItem is a subclass of :ref:`AVItem`, which is a subclass of :ref:`Item`. All methods and attributes of AVItem and Item, in addition to those listed below, are available when working with FootageItem.

----

==========
Attributes
==========

.. _FootageItem.file:

FootageItem.file
*********************************************

``app.project.item(index).file``

**Description**

The `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the footage's source file.

If the FootageItem's ``mainSource`` is a FileSource, this is the same as :ref:`FootageItem.mainSource.file <FileSource.file>`. Otherwise it is null.

**Type**

`File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object; read-only.

----

.. _FootageItem.mainSource:

FootageItem.mainSource
*********************************************

``app.project.item(index).mainSource``

**Description**

The footage source, an object that contains all of the settings related to that footage item, including those that are normally accessed through the Interpret Footage dialog box. The attribute is read-only. To change its value, call one of the FootageItem "replace" methods. See the :ref:`FootageSource`, and its three types:

-  :ref:`SolidSource`
-  :ref:`FileSource`
-  :ref:`PlaceholderSource`

If this is a FileSource object, and the :ref:`footageMissing <AVItem.footageMissing>` value is true, the path to the missing footage file is in the :ref:`FileSource.missingFootagePath` attribute.

**Type**

:ref:`FootageSource`; read-only.

----

=======
Methods
=======

.. _FootageItem.openInViewer:

FootageItem.openInViewer()
*********************************************

``app.project.item(index).openInViewer()``

**Description**

Opens the footage in a Footage panel, and moves the Footage panel to front and gives it focus.

.. note::
   Missing and placeholder footage can be opened using this method, but cannot manually (via double-clicking it).

**Parameters**

None.

**Returns**

:ref:`Viewer` for the Footage panel, or null if the footage could not be opened.

----

.. _FootageItem.replace:

FootageItem.replace()
*********************************************

``app.project.item(index).replace(file)``

**Description**

Changes the source of this FootageItem to the specified file.

In addition to loading the file, the method creates a new FileSource object for the file and sets mainSource to that object. In the new source object, it sets the ``name``, ``width``, ``height``, ``frameDuration``, and ``duration`` attributes (see :ref:`AVItem`) based on the contents of the file.

The method preserves interpretation parameters from the previous ``mainSource`` object.

If the specified file has an unlabeled alpha channel, the method estimates the alpha interpretation.

**Parameters**

========  ==========================================================
``file``  An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file to be used as the footage main source.
========  ==========================================================

----

.. _FootageItem.replaceWithPlaceholder:

FootageItem.replaceWithPlaceholder()
*********************************************

``app.project.item(index).replaceWithPlaceholder(name, width, height, frameRate, duration)``

**Description**

Changes the source of this FootageItem to the specified placeholder. Creates a new PlaceholderSource object, sets its values from the parameters, and sets ``mainSource`` to that object.

**Parameters**

=============  =======================================================
``name``       A string containing the name of the placeholder.
``width``      The width of the placeholder in pixels, an integer
               in the range ``[4..30000]``.
``height``     The height of the placeholder in pixels, an integer
               in the range ``[4..30000]``.
``frameRate``  The frame rate of the placeholder, a floating-point
               value in the range ``[1.0..99.0]``
``duration``   The duration of the placeholder in seconds, a
               floating-point value in the range ``[0.0..10800.0]``.
=============  =======================================================

----

.. _FootageItem.replaceWithSequence:

FootageItem.replaceWithSequence()
*********************************************

``app.project.item(index).replaceWithSequence(file, forceAlphabetical)``

**Description**

Changes the source of this FootageItem to the specified image sequence.

In addition to loading the file, the method creates a new FileSource object for the file and sets ``mainSource`` to that object. In the new source object, it sets the ``name``, ``width``, ``height``, ``frameDuration``, and ``duration`` attributes (see :ref:`AVItem`) based on the contents of the file.

The method preserves interpretation parameters from the previous ``mainSource`` object. If the specified file has an unlabeled alpha channel, the method estimates the alpha interpretation.

**Parameters**

=====================  =====================================================
``file``               An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the first file in the sequence to be used as the footage main source.
``forceAlphabetical``  When true, use the "Force alphabetical order" option.
=====================  =====================================================

----

.. _FootageItem.replaceWithSolid:

FootageItem.replaceWithSolid()
*********************************************

``app.project.item(index).replaceWithSolid(color, name, width, height, pixelAspect)``

**Description**

Changes the source of this FootageItem to the specified solid. Creates a new SolidSource object, sets its values from the parameters, and sets ``mainSource`` to that object.

**Parameters**

===============  ===========================================================
``color``        The color of the solid, an array of three floating-point
                 values, ``[R, G, B]``, in the range ``[0.0..1.0]``.
``name``         A string containing the name of the solid.
``width``        The width of the solid in pixels, an integer in the range
                 ``[4..30000]``.
``height``       The height of the solid in pixels, an integer in the range
                 ``[4..30000]``.
``pixelAspect``  The pixel aspect ratio of the solid, a floating-point value
                 in the range ``[0.01..100.0]``.
===============  ===========================================================
