.. _RenderQueue:

RenderQueue object
################################################

``app.project.renderQueue``

**Description**

The RenderQueue object represents the render automation process, the data and functionality that is available through the Render Queue panel of a particular After Effects project. Attributes provide access to items in the render queue and their render status. Methods can start, pause, and stop the rendering process. The :ref:`RenderQueueItem` provides access to the specific settings for an item to be rendered.

----

==========
Attributes
==========

.. _RenderQueue.canQueueInAME:

RenderQueue.canQueueInAME
*********************************************

``app.project.renderQueue.canQueueInAME``

.. note::
   This functionality was added in After Effects 14.0 (CC 2017)

**Description**

indicates whether or not there are queued render items in the After Effects render queue. Only queued items can be added to the AME queue.

:ref:`RenderQueue.queueInAME`

**Type**

Boolean; read-only.

----

.. _RenderQueue.queueNotify:

RenderQueue.queueNotify
*********************************************

``app.project.renderQueue.queueNotify``

.. note::
   This functionality was added in After Effects 22.0 (2022)

**Description**

Read or write the **Notify** property for the entire Render Queue. 
This is exposed in the UI as a checkbox in the lower right corner of the Render Queue panel.

**Type**

Boolean; read/write.

----

.. _RenderQueue.items:

RenderQueue.items
*********************************************

``app.project.renderQueue.items``

**Description**

A collection of all items in the render queue. See :ref:`RenderQueueItem`.

**Type**

:ref:`RQItemCollection`; read-only.

----

.. _RenderQueue.numItems:

RenderQueue.numItems
*********************************************

``app.project.renderQueue.numItems``

**Description**

The total number of items in the render queue.

**Type**

Integer; read-only.

----

.. _RenderQueue.rendering:

RenderQueue.rendering
*********************************************

``app.project.renderQueue.rendering``

**Description**

When true, the rendering process is in progress or paused. When false, it is stopped.

**Type**

Boolean; read-only.

----

=======
Methods
=======

.. _RenderQueue.item:

RenderQueue.item()
*********************************************

``app.project.renderQueue.item(index)``

**Description**

Gets a specified item from the ite ms collection.

**Parameters**

``index``
The position index of the item. An integer in the range ``[0..numItems]``.

**Returns**

:ref:`RenderQueueItem`.

----

.. _RenderQueue.pauseRendering:

RenderQueue.pauseRendering()
*********************************************

``app.project.renderQueue.pauseRendering(pause)``

**Description**

Pauses the current rendering process, or continues a paused rendering process. This is the same as clicking Pause in the Render Queue panel during a render. You can call this method from an :ref:`RenderQueueItem.onstatus` or :ref:`app.onError` callback.

**Parameters**

=========  ====================================================================
``pause``  True to pause a current render process, false to continue a paused
           render.
=========  ====================================================================

**Returns**

Nothing.

----

.. _RenderQueue.render:

RenderQueue.render()
*********************************************

``app.project.renderQueue.render()``

**Description**

Starts the rendering process. This is the same as clicking Render in the Render Queue panel. The method does not return until the render process is complete. To pause or stop the rendering process, call :ref:`renderqueue.pauseRendering` or :ref:`renderqueue.stopRendering` from an ``onError`` or ``onstatus`` callback.

-  To respond to errors during the rendering process, define a callback function in :ref:`app.onError`.
-  To respond to changes in the status of a particular item while the render is progressing, define a callback function in :ref:`RenderQueueItem.onstatus` in the associated RenderQueueItem object.

**Parameters**

None.

**Returns**

Nothing.

----

.. _RenderQueue.showWindow:

RenderQueue.showWindow()
*********************************************

``app.project.renderQueue.showWindow(doShow)``

**Description**

Shows or hides the Render Queue panel.

**Parameters**

==========  =============================================================
``doShow``  When true, show the Render Queue panel. When false, hide it.
==========  =============================================================

**Returns**

Nothing.

----

.. _RenderQueue.stopRendering:

RenderQueue.stopRendering()
*********************************************

``app.project.renderQueue.stopRendering()``

**Description**

Stops the rendering process. This is the same as clicking Stop in the Render Queue panel during a render. You can call this method from an :ref:`RenderQueueItem.onstatus` or :ref:`app.onError` callback.

**Parameters**

None.

**Returns**

Nothing.

----

.. _RenderQueue.queueInAME:

RenderQueue.queueInAME()
*********************************************

``app.project.renderQueue.queueInAME(render_immediately_in_AME)``

.. note::
   This functionality was added in After Effects 14.0 (CC 2017)

**Description**

Calls the Queue In AME command. This method requires passing a boolean value, telling AME whether to only queue the render items (false) or if AME should also start processing its queue (true).

.. note::
   This requires Adobe Media Encoder CC 2017 (11.0) or later.

.. note::
   When AME receives the queued items, it applies the most recently used encoding preset. If ``render_immediately_in_AME`` is set to true, you will not have an opportunity to change the encoding settings.

**Parameters**

=============================  ==============================================================
``render_immediately_in_AME``  Telling AME whether to only queue the render items (``false``)
                               or if AME should also start processing its queue (``true``).
=============================  ==============================================================

**Returns**

Nothing.

**Example**

The following sample code checks to see if there are queued items in the render queue, and if so queues them in AME but does not immediately start rendering:

.. code:: javascript

    // Scripting support for Queue in AME.
    // Requires Adobe Media Encoder 11.0.
    if (app.project.renderQueue.canQueueInAME === true) {
        // Send queued items to AME, but do not start rendering.
        app.project.renderQueue.queueInAME(false);
    } else {
        alert("There are no queued item in the Render Queue.");
    }
