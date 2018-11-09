.. highlight:: javascript
.. _RenderQueueItem:

RenderQueueItem object
################################################

``app.project.renderQueue.item(index)``

**Description**

The RenderQueueItem object represents an individual item in the render queue. It provides access to the specific settings for an item to be rendered. Create the object by adding a composition to the Render Queue with the :ref:`RQItemCollection`; see :ref:`RQItemCollection.add`.

----

==========
Attributes
==========

.. _RenderQueueItem.comp:

RenderQueueItem.comp
*********************************************

``app.project.renderQueue.item(index).comp``

**Description**

The composition that will be rendered by this render-queue item. To change the composition, you must delete this render-queue item and create a new one.

**Type**

:ref:`CompItem`; read-only.

----

.. _RenderQueueItem.elapsedSeconds:

RenderQueueItem.elapsedSeconds
*********************************************

``app.project.renderQueue.item(index).elapsedSeconds``

**Description**

The number of seconds spent rendering this item.

**Type**

Integer, or null if item has not been rendered; read-only.

----

.. _RenderQueueItem.logType:

RenderQueueItem.logType
*********************************************

``app.project.renderQueue.item(index).logType``

**Description**

A log type for this item, indicating which events should be logged while this item is being rendered.

**Type**

A ``LogType`` enumerated value; (read/write). One of:

-  ``LogType.ERRORS_ONLY``
-  ``LogType.ERRORS_AND_SETTINGS``
-  ``LogType.ERRORS_AND_PER_FRAME_INFO``

----

.. _RenderQueueItem.numOutputModules:

RenderQueueItem.numOutputModules
*********************************************

``app.project.renderQueue.item(index).numOutputModules``

**Description**

The total number of Output Modules assigned to this item.

**Type**

Integer; read-only.

----

.. _RenderQueueItem.onStatusChanged:

RenderQueueItem.onStatusChanged
*********************************************

``app.project.renderQueue.item(index).onStatusChanged``

**Description**

The name of a callback function that is called whenever the value of the :ref:`RenderQueueItem.status` attribute changes.

You cannot make changes to render queue items or to the application while rendering is in progress or paused; you can, however, use this callback to pause or stop the rendering process. See :ref:`RenderQueue.pauseRendering` and :ref:`RenderQueue.stopRendering`. See also :ref:`app.onError`.

**Type**

A function name string, or null if no function is assigned.

**Example**

::

    function myStatusChanged() {
        alert(app.project.renderQueue.item(1).status)
    }

    app.project.renderQueue.item(1).onStatusChanged = myStatusChanged();
    app.project.renderQueue.item(1).render = false; // changes status and shows dialog

----

.. _RenderQueueItem.outputModules:

RenderQueueItem.outputModules
*********************************************

``app.project.renderQueue.item(index).outputModules``

**Description**

The collection of Output Modules for the item.

**Type**

:ref:`OMCollection`; read-only.

----

.. _RenderQueueItem.render:

RenderQueueItem.render
*********************************************

``app.project.renderQueue.item(index).render``

**Description**

When true, the item will be rendered when the render queue is started. When set to true, the :ref:`RenderQueueItem.status` is set to ``RQItemStatus.QUEUED``. When set to false, ``status`` is set to
``RQItemStatus.UNQUEUED``.

**Type**

Boolean; read/write.

----

.. _RenderQueueItem.skipFrames:

RenderQueueItem.skipFrames
*********************************************

``app.project.renderQueue.item(index).skipFrames``

**Description**

The number of frames to skip when rendering this item. Use this to do rendering tests that are faster than a full render. A value of 0 skip no frames, and results in regular rendering of all frames. A value of 1 skips every other frame. This is equivalent to "rendering on twos." Higher values skip a larger number of frames. The total length of time remains unchanged. For example, if skip has a value of 1, a sequence output would have half the number of frames and in movie output, each frame would be double the duration.

**Type**

Integer in the range ``[0..99]``. Read/write.

----

.. _RenderQueueItem.startTime:

RenderQueueItem.startTime
*********************************************

``app.project.renderQueue.item(index).startTime``

**Description**

The day and time that this item started rendering.

**Type**

Date object, or null if the item has not started rendering; read-only.

----

.. _RenderQueueItem.status:

RenderQueueItem.status
*********************************************

``app.project.renderQueue.item(index).status``

**Description**

The current render status of the item.

**Type**

An ``RQItemStatus`` enumerated value; read-only. One of:

-  ``RQItemStatus.WILL_CONTINUE``: Rendering process has been paused.
-  ``RQItemStatus.NEEDS_OUTPUT``: Item lacks a valid output path.
-  ``RQItemStatus.UNQUEUED``: Item is listed in the Render Queue panel but composition is not ready to render.
-  ``RQItemStatus.QUEUED``: Composition is ready to render.
-  ``RQItemStatus.RENDERING``: Composition is rendering
-  ``RQItemStatus.USER_STOPPED``: Rendering process was stopped by user or script.
-  ``RQItemStatus.ERR_STOPPED``: Rendering process was stopped due to an error.
-  ``RQItemStatus.DONE``: Rendering process for the item is complete.

----

.. _RenderQueueItem.templates:

RenderQueueItem.templates
*********************************************

``app.project.renderQueue.item(index).templates``

**Description**

The names of all Render Settings templates available for the item. See also :ref:`RenderQueueItem.saveAsTemplate`.

**Type**

Array of strings; read-only.

----

.. _RenderQueueItem.timeSpanDuration:

RenderQueueItem.timeSpanDuration
*********************************************

``app.project.renderQueue.item(index).timeSpanDuration``

**Description**

The duration in seconds of the composition to be rendered. The duration is determined by subtracting the start time from the end time. Setting this value is the same as setting a custom end time in the Render Settings dialog box.

**Type**

Floating-point value; read/write.

----

.. _RenderQueueItem.timeSpanStart:

RenderQueueItem.timeSpanStart
*********************************************

``app.project.renderQueue.item(index).timeSpanStart``

**Description**

The time in the composition, in seconds, at which rendering will begin. Setting this value is the same as setting a custom start time in the Render Settings dialog box.

**Type**

Floating-point value; read/write.

----

=======
Methods
=======

.. _RenderQueueItem.applyTemplate:

RenderQueueItem.applyTemplate()
*********************************************

``app.project.renderQueue.item(index).applyTemplate(templateName)``

**Description**

Applies a Render Settings template to the item. See also :ref:`RenderQueueItem.saveAsTemplate` and :ref:`RenderQueueItem.templates`.

**Parameters**

================  ======================================================
``templateName``  A string containing the name of the template to apply.
================  ======================================================

**Returns**

Nothing.

----

.. _RenderQueueItem.duplicate:

RenderQueueItem.duplicate()
*********************************************

``app.project.renderQueue.item(index).duplicate()``

**Description**

Creates a duplicate of this item and adds it this render queue.

.. note::
   Duplicating an item whose status is "Done" sets the new item's status to "Queued".

**Parameters**

None.

**Returns**

RenderQueueItem object.

----

.. _RenderQueueItem.getSetting:

RenderQueueItem.getSetting()
*********************************************

``app.project.renderQueue.item(index).getSetting()``

.. note::
   This functionality was added in After Effects 13.0 (CC 2014)

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _RenderQueueItem.getSettings:

RenderQueueItem.getSettings()
*********************************************

``app.project.renderQueue.item(index).getSettings()``

.. note::
   This functionality was added in After Effects 13.0 (CC 2014)

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _RenderQueueItem.outputModule:

RenderQueueItem.outputModule()
*********************************************

``app.project.renderQueue.item(index).outputModule(index)``

**Description**

Gets an output module with the specified index position.

**Parameters**

=========  ====================================================================
``index``  The position index of the output module. An integer in the range
           ``[1..numOutputModules]``.
=========  ====================================================================

**Returns**

OutputModule object.

----

.. _RenderQueueItem.remove:

RenderQueueItem.remove()
*********************************************

``app.project.renderQueue.item(index).remove()``

**Description**

Removes this item from the render queue.

**Parameters**

None.

**Returns**

Nothing.

----

.. _RenderQueueItem.saveAsTemplate:

RenderQueueItem.saveAsTemplate()
*********************************************

``app.project.renderQueue.item(index).saveAsTemplate(name)``

**Description**

Saves the item's current render settings as a new template with the specified name.

**Parameters**

========  ==================================================
``name``  A string containing the name of the new template.
========  ==================================================

**Returns**

Nothing.

----

.. _RenderQueueItem.setSetting:

RenderQueueItem.setSetting()
*********************************************

``app.project.renderQueue.item(index).setSetting()``

.. note::
   This functionality was added in After Effects 13.0 (CC 2014)

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva

----

.. _RenderQueueItem.setSettings:

RenderQueueItem.setSettings()
*********************************************

``app.project.renderQueue.item(index).setSettings()``

.. note::
   This functionality was added in After Effects 13.0 (CC 2014)

**Description**

See https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva