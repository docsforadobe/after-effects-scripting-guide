.. _AVItem:

AVItem object
################################################

``app.project.item(index)``

**Description**

The AVItem object provides access to attributes and methods of audio/visual files imported into After Effects.

    AVItem is a subclass of Item. All methods and attributes of Item, in addition to those listed below, are available when working with AVItem. See :ref:`Item`

    AVItem is the base class for both CompItem and FootageItem, so AVItem attributes and methods are also available when working with CompItem and FootageItem objects. See :ref:`CompItem` and :ref:`FootageItem`.

.. warning::
    CompItems and FootageItems, while logical descendants of AVItem, are not *really* subclasses of AVItem as AVItem doesn't exist in Extendscript, ie. attempting to check if ``item instanceof AVItem`` will fail because AVItem is undefined. This is also true for ``Item`` itself.

    See :ref:`Javascript.Classes` and :ref:`ClassHierarchy` for more info.

----

==========
Attributes
==========

.. _AVItem.duration:

AVItem.duration
*********************************************

``app.project.item(index).duration``

**Description**

Returns the duration, in seconds, of the item. Still footage items have a duration of 0.

-  In a CompItem, the value is linked to the duration of the composition, and is read/write.
-  In a FootageItem, the value is linked to the ``duration`` of the ``mainSource`` object, and is read-only.

**Type**

Floating-point value in the range [0.0..10800.0]; read/write for a ``CompItem``; otherwise, read-only.

----

.. _AVItem.footageMissing:

AVItem.footageMissing
*********************************************

``app.project.item(index).footageMissing``

**Description**

When true, the AVItem is a placeholder, or represents footage with a source file that cannot be found. In this case, the path of the missing source file is in the ``missingFootagePath`` attribute of the footage item's source-file object. See :ref:`FootageItem.mainSource` and :ref:`FileSource.missingFootagePath`.

**Type**

Boolean; read-only.

----

.. _AVItem.frameDuration:

AVItem.frameDuration
*********************************************

``app.project.item(index).frameDuration``

**Description**

Returns the length of a frame for this AVItem, in seconds. This is the reciprocal of ``frameRate``. When set, the reciprocal is automatically set as a new ``frameRate`` value. This attribute returns the reciprocal of the ``frameRate``, which may not be identical to a value you set, if that value is not evenly divisible into 1.0 (for example, 0.3). Due to numerical limitations, (1 / (1 / 0.3)) is close to, but not exactly, 0.3. If the AVItem is a FootageItem, this value is linked to the ``mainSource``, and is read-only. To change it, set the ``conformFrameRate`` of the ``mainSource`` object. This sets both the ``frameRate`` and ``frameDuration`` of the FootageItem.

**Type**

Floating-point value in the range [1/99.. 1.0]; read-only for a FootageItem, otherwise read/write.

----

.. _AVItem.frameRate:

AVItem.frameRate
*********************************************

``app.project.item(index).frameRate``

**Description**

The frame rate of the AVItem, in frames-per-second. This is the reciprocal of the ``frameDuration`` . When set, the reciprocal is automatically set as a new ``frameDuration`` value.

-  In a CompItem, the value is linked to the ``frameRate`` of the composition, and is read/write.
-  In a FootageItem, the value is linked to the ``frameRate`` of the ``mainSource`` object, and is read-only. To change it, set the ``conformFrameRate`` of the ``mainSource`` object. This sets both the ``frameRate`` and ``frameDuration`` of the FootageItem.

**Type**

Floating-point value in the range [1.0..99.0]; read-only for a FootageItem, otherwise read/write.

----

.. _AVItem.hasAudio:

AVItem.hasAudio
*********************************************

``app.project.item(index).hasAudio``

**Description**

When true, the AVItem has an audio component.

-  In a CompItem, the value is linked to the composition.
-  In a FootageItem, the value is linked to the ``mainSource`` object.

**Type**

Boolean; read-only.

----

.. _AVItem.hasVideo:

AVItem.hasVideo
*********************************************

``app.project.item(index).hasVideo``

**Description**

When true, the AVItem has a video component.

-  In a CompItem, the value is linked to the composition.
-  In a FootageItem, the value is linked to the ``mainSource`` object.

**Type**

Boolean; read-only.

----

.. _AVItem.height:

AVItem.height
*********************************************

``app.project.item(index).height``

**Description**

The height of the item in pixels.

-  In a CompItem, the value is linked to the composition, and is read/write.
-  In a FootageItem, the value is linked to the ``mainSource`` object, and is read/write only if the ``mainSource`` object is a SolidSource. Otherwise, it is read-only.

**Type**

Integer in the range [1...30000]; read/write, except as noted.

----

.. _AVItem.isMediaReplacementCompatible:

AVItem.isMediaReplacementCompatible
*********************************************

``app.project.item(index).isMediaReplacementCompatible``

.. note::
    This functionality was added in After Effects 18.0 (2021)

**Description**

Test whether the AVItem can be used as an alternate source when calling :ref:`Property.setAlternateSource`.

Returns true if the item can be used, or false otherwise.

A CompItem or a FootageItem can be used as an alternate source for the layer, with some restrictions:

-  If the AVItem is a :ref:`FootageItem`, then FootageItem.FootageSource should not be a :ref:`SolidSource`.
-  If the AVItem is a :ref:`FootageItem` and the FootageItem.FootageSource is a :ref:`FileSource` then that FileSource should not point to a non-media file e.g. a JSX script file.
-  Setting the AVItem cannot create a cyclical reference within the project.

**Type**

Boolean; read only.

----

.. _AVItem.name:

AVItem.name
*********************************************

``app.project.item(index).name``

**Description**

The name of the item, as shown in the Project panel.

-  In a FootageItem, the value is linked to the ``mainSource`` object. If the ``mainSource`` object is a ``FileSource``, this value controls the display name in the Project panel, but does not affect the file name.

**Type**

String; read/write.

----

.. _AVItem.pixelAspect:

AVItem.pixelAspect
*********************************************

``app.project.item(index).pixelAspect``

**Description**

The pixel aspect ratio (PAR) of the item.

-  In a CompItem, the value is linked to the composition.
-  In a FootageItem, the value is linked to the mainSource object.

The value you retrieve after setting may be slightly different from the value you supplied. The following table compares the value as it appears in the UI with the more accurate value returned by this attribute.

===========================  =========================================
PAR in the After Effects UI  PAR returned by the pixelAspect attribute
===========================  =========================================
0.91                         0.90909090909091
1                            1
1.5                          1.5
1.09                         1.09401709401709
1.21                         1.21212121212121
1.33                         1.33333333333333
1.46                         1.45868945868946
2                            2
===========================  =========================================

**Type**

Floating-point value, in the range [0.01..100.0]; read/write.

----

.. _AVItem.proxySource:

AVItem.proxySource
*********************************************

``app.project.item(index).proxySource``

**Description**

The FootageSource being used as a proxy. The attribute is read-only; to change it, call any of the AVItem methods that change the proxy source: ``setProxy()``, ``setProxyWithSequence()``, ``setProxyWithSolid()``, or ``setProxyWithPlaceholder()``.

**Type**
``FootageSource`` object; read-only.

----

.. _AVItem.time:

AVItem.time
*********************************************

``app.project.item(index).time``

**Description**

The current time of the item when it is being previewed directly from the Project panel. This value is a number of seconds. Use the global method :ref:`timeToCurrentFormat` to convert it to a string value that expresses the time in terms of frames. It is an error to set this value for a FootageItem whose ``mainSource`` is still (``item.mainSource.isStill`` is true).

**Type**

Floating-point value; read/write.

----

.. _AVItem.usedIn:

AVItem.usedIn
*********************************************

``app.project.item(index).usedIn``

**Description**

All the compositions that use this AVItem. Note that upon retrieval, the array value is copied, so it is not automatically updated. If you get this value, then add this item into another composition, you must retrieve the value again to get an array that includes the new item.

**Type**

Array of CompItem objects; read-only.

----

.. _AVItem.useProxy:

AVItem.useProxy
*********************************************

``app.project.item(index).useProxy``

**Description**

When true, a proxy is used for the item. It is set to true by all the ``SetProxy`` methods, and to false by the ``SetProxyToNone()`` method.

**Type**

Boolean; read/write.

----

.. _AVItem.width:

AVItem.width
*********************************************

``app.project.item(index).width``

**Description**

The width of the item, in pixels.

-  In a CompItem, the value is linked to the composition, and is read/write.
-  In a FootageItem, the value is linked to the ``mainSource`` object, and is read/write only if the ``mainSource`` object is a SolidSource. Otherwise, it is read-only.

**Type**

Integer in the range [1...30000]; read/write, except as noted.

----

=======
Methods
=======

.. _AVItem.setProxy:

AVItem.setProxy()
*********************************************

``app.project.item(index).setProxy(file)``

**Description**

Sets a file as the proxy of this AVItem.

Loads the specified file into a new FileSource object, sets this as the value of the ``proxySource`` attribute, and sets ``useProxy`` to true.

It does not preserve the interpretation parameters, instead using the user preferences. If the file has an unlabeled alpha channel, and the user preference says to ask the user what to do, the method estimates the alpha interpretation, rather than asking the user.

This differs from setting a FootageItem's ``mainSource``, but both actions are performed as in the user interface.

**Parameters**

========  ================================================================
``file``  An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file to be used as a proxy.
========  ================================================================

**Returns**

None.

----

.. _AVItem.setProxyToNone:

AVItem.setProxyToNone()
*********************************************

``app.project.item(index).setProxyToNone()``

**Description**

Removes the proxy from this AVItem, sets the value of ``proxySource`` to ``null``, and sets the value of ``useProxy`` to false.

**parameters**

None.

**Returns**

Nothing.

----

.. _AVItem.setProxyWithPlaceholder:

AVItem.setProxyWithPlaceholder()
*********************************************

``app.project.item(index).setProxyWithPlaceholder(name, width, height ,frameRate, duration)``

**Description**

Creates a PlaceholderSource object with specified values, sets this as the value of the ``proxySource`` attribute, and sets ``useProxy`` to true. It does not preserve the interpretation parameters, instead using the user preferences.

.. note::
   There is no direct way to set a placeholder as a proxy in the user interface; this behavior occurs when a proxy has been set and then moved or deleted.


**parameters**

=====================  ===================================================
``name``               A string containing the name of the new object.
``width``, ``height``  The pixel dimensions of the placeholder, an integer
                       in the range [4..30000]. ``frameRate`` The
                       frames-per-second, an integer in the range [1..99].
                       ``duration`` The total length in seconds, up to 3
                       hours. An integer in the range [0.0..10800.0].
=====================  ===================================================

**Returns**

Nothing.

----

.. _AVItem.setProxyWithSequence:

AVItem.setProxyWithSequence()
*********************************************

``app.project.item(index).setProxyWithSequence(file,forceAlphabetical)``

**Description**

Sets a sequence of files as the proxy of this AVItem, with the option of forcing alphabetical order.
Loads the specified file sequence into a new FileSource object, sets this as the value of the ``proxySource`` attribute, and sets ``useProxy`` to true.

It does not preserve the interpretation parameters, instead using the user preferences.
If any file has an unlabeled alpha channel, and the user preference says to ask the user what to do, the method estimates the alpha interpretation, rather than asking the user.

**parameters**

=====================  =====================================================
``file``               An `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the first file in the sequence.
``forceAlphabetical``  When true, use the "Force alphabetical order" option.
=====================  =====================================================

**Returns**

Nothing.

----

.. _AVItem.setProxyWithSolid:

AVItem.setProxyWithSolid()
*********************************************

``app.project.item(index).setProxyWithSolid(color, name, width, height, pixelAspect)``

**Description**

Creates a :ref:`SolidSource` with specified values, sets this as the value of the ``proxySource`` attribute, and sets ``useProxy`` to true. It does not preserve the interpretation parameters, instead using the user preferences.

.. note::
   There is no way, using the user interface, to set a solid as a proxy; this feature is available only through scripting.

**parameters**

=====================  ====================================================
``color``              The color of the solid, an array of 3 floating-point
                       values, [R, G, B], in the range [0.0..1.0]. ``name``
                       A string containing the name of the new object.
``width``, ``height``  The pixel dimensions of the placeholder, an integer
                       in the range [1...30000]. ``pixelAspect`` The pixel
                       aspect of the solid, a floating-point value in the
                       range [0.01... 100.0].
=====================  ====================================================

**Returns**

Nothing.
