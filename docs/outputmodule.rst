.. _OutputModule:

OutputModule object
################################################

``app.project.renderQueue.item(index).outputModule(index)``

**Description**

An OutputModule object of a :ref:`RenderQueueItem <RenderQueueItem>` generates a single file or sequence via a render operation, and contains attributes and methods relating to the file to be rendered.

----

==========
Attributes
==========

.. _OutputModule.file:

OutputModule.file
*********************************************

``app.project.renderQueue.item(index).outputModule(index).file``

**Description**

The ExtendScript File object for the file this output module is set to render.

**Type**

ExtendScript File object; read/write.

----

.. _OutputModule.includeSourceXMP:

OutputModule.includeSourceXMP
*********************************************

``app.project.renderQueue.item(index).outputModule(index).includeSourceXMP``

**Description**

When true, writes all source footage XMP metadata to the output file. Corresponds to the Include Source XMP Metadata option in the Output Module Settings dialog box.

**Type**

Boolean; read/write.

----

.. _OutputModule.name:

OutputModule.name
*********************************************

``app.project.renderQueue.item(index).outputModule(index).name``

**Description**

The name of the output module, as shown in the user interface.

**Type**

String; read-only.

----

.. _OutputModule.postRenderAction:

OutputModule.postRenderAction
*********************************************

``app.project.renderQueue.item(index).outputModule(index).postRenderAction``

**Description**

An action to be performed when the render operation is completed.

**Type**

A ``PostRenderAction`` enumerated value (read/write); one of:

-  ``PostRenderAction.NONE``
-  ``PostRenderAction.IMPORT``
-  ``PostRenderAction.IMPORT_AND_REPLACE_USAGE``
-  ``PostRenderAction.SET_PROXY``

----

.. _OutputModule.templates:

OutputModule.templates
*********************************************

``app.project.renderQueue.item(index).outputModule(index).templates``

**Description**

The names of all output-module templates available in the local installation of After Effects.

**Type**

Array of strings; read-only.

-----

=======
Methods
=======

.. _OutputModule.applyTemplate:

OutputModule.applyTemplate()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).applyTemplate(templateName)``

**Description**

Applies the specified existing output-module template.

**Parameters**

================  ===========================================================
``templateName``  A string containing the name of the template to be applied.
================  ===========================================================

**Returns**

Nothing.

----

.. _OutputModule.getSetting:

OutputModule.getSetting()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).getSetting()``

.. note::
   This functionality was added in After Effects 13.0

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _OutputModule.getSettings:

OutputModule.getSettings()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).getSettings()``

.. note::
   This functionality was added in After Effects 13.0

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _OutputModule.remove:

OutputModule.remove()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).remove()``

**Description**

Removes this OutputModule object from the collection.

**Parameters**

None.

**Returns**

Nothing.

----

.. _OutputModule.saveAsTemplate:

OutputModule.saveAsTemplate()
*****************************

``app.project.renderQueue.item(index).outputModule(index).saveAsTemplate(name)``

**Description**

Saves this output module as a template and adds it to the te mpl ate s array.

**Parameters**

========  =================================================
``name``  A string containing the name of the new template.
========  =================================================

**Returns**

Nothing.

----

.. _OutputModule.setSetting:

OutputModule.setSetting()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).setSetting()``

.. note::
   This functionality was added in After Effects 13.0

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _OutputModule.setSettings:

OutputModule.setSettings()
*********************************************

``app.project.renderQueue.item(index).outputModule(index).setSettings()``

.. note::
   This functionality was added in After Effects 13.0

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva
