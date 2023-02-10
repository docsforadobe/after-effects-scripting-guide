.. _FileSource:

FileSource object
################################################

|  ``app.project.item(index).mainSource``
|  ``app.project.item(index).proxySource``

**Description**

The FileSource object describes footage that comes from a file.

    FileSource is a subclass of :ref:`FootageSource`. All methods and attributes of FootageSource, in addition to those listed below, are available when working with FileSource.

----

==========
Attributes
==========

.. _FileSource.file:

FileSource.file
*********************************************

|  ``app.project.item(index).mainSource.file``
|  ``app.project.item(index).proxySource.file``

**Description**

The `Extendscript File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object for the file that defines this asset. To change the value:

-  If this FileSource is a :ref:`proxySource <AVItem.proxySource>` of an :ref:`AVItem <AVItem>`, call :ref:`setProxy() <AVItem.setProxy>` or :ref:`setProxyWithSequence() <AVItem.setProxyWithSequence>`.
-  If this FileSource is a :ref:`mainSource <FootageItem.mainSource>` of a :ref:`FootageItem <FootageItem>`, call :ref:`replace() <FootageItem.replace>` or :ref:`replaceWithSequence() <FootageItem.replaceWithSequence>`.

**Type**

`File <https://extendscript.docsforadobe.dev/file-system-access/file-object.html>`_ object; read-only.

----

.. _FileSource.missingFootagePath:

FileSource.missingFootagePath
*********************************************

|  ``app.project.item(index).mainSource.missingFootagePath``
|  ``app.project.item(index).proxySource.missingFootagePath``

**Description**

The path and filename of footage that is missing from this asset. See also :ref:`AVItem.footageMissing`.

**Type**

String; read-only.

----

=======
Methods
=======

.. _FileSource.reload:

FileSource.reload()
*********************************************

``app.project.item(index).mainSource.reload()``

**Description**

Reloads the asset from the file. This method can be called only on a ``mainSource``, not a ``proxySource``.

**Parameters**

None.

**Returns**

Nothing.
