.. highlight:: javascript
.. _ImportOptions:

ImportOptions object
################################################

|  ``new ImportOptions();``
|  ``new ImportOptions(file);``

**Description**

The ImportOptions object encapsulates the options used to import a file with the :ref:`Project.importFile` methods. The constructor takes an optional parameter, an ExtendScript File object for the file. If it is not supplied, you must explicitly set the value of the ``file`` attribute before using the object with the ``importFile`` method. For example:

::

    new ImportOptions().file = new File("myfile.psd");

----

==========
Attributes
==========

.. _ImportOptions.file:

ImportOptions.file
*********************************************

``importOptions.file``

**Description**

The file to be imported. If a file is set in the constructor, you can access it through this attribute.

**Type**

ExtendScript File object; read/write.

----

.. _ImportOptions.forceAlphabetical:

ImportOptions.forceAlphabetical
*********************************************

``importOptions.forceAlphabetical``

**Description**

When true, has the same effect as setting the "Force alphabetical order" option in the File > Import > File dialog box.

**Type**

Boolean; read/write.

----

.. _ImportOptions.importAs:

ImportOptions.importAs
*********************************************

``importOptions.importAs``

**Description**

The type of object for which the imported file is to be the source. Before setting, use `canImportAs <#importoptions-canimportas-method>`__ to check that a given file can be imported as the source of the given object type.

**Type**

An ``ImportAsType`` enumerated value; read/write. One of:

-  ``ImportAsType.COMP_CROPPED_LAYERS``
-  ``ImportAsType.FOOTAGE``
-  ``ImportAsType.COMP``
-  ``ImportAsType.PROJECT``

----

.. _ImportOptions.sequence:

ImportOptions.sequence
*********************************************

``importOptions.sequence``

**Description**

When true, a sequence is imported; otherwise, an individual file is imported.

**Type**

Boolean; read/write.

----

=======
Methods
=======

.. _ImportOptions.canImportAs:

ImportOptions.canImportAs()
*********************************************

``importOptions.canImportAs(type)``

**Description**

Reports whether the file can be imported as the source of a particular object type. If this method returns true, you can set the given type as the value of the :ref:`importAs <importoptions.importas>` attribute.

**Parameters**

========  =====================================================================
``type``  The type of file that can be imported. An ``ImportAsType`` enumerated
          value; one of:

          -  ``ImportAsType.COMP``
          -  ``ImportAsType.FOOTAGE``
          -  ``ImportAsType.COMP_CROPPED_LAYERS``
          -  ``ImportAsType.PROJECT``
========  =====================================================================

**Returns**

Boolean.

**Example**

::

    var io = new ImportOptions(File("c:\\myFile.psd"));
    if (io.canImportAs(ImportAsType.COMP)) {
        io.importAs = ImportAsType.COMP;
    }
