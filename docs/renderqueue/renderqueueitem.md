# RenderQueueItem object

`app.project.renderQueue.item(index)`

#### Description

The RenderQueueItem object represents an individual item in the render queue. It provides access to the specific settings for an item to be rendered. Create the object by adding a composition to the Render Queue with the [RQItemCollection object](rqitemcollection.md); see [RQItemCollection.add()](rqitemcollection.md#rqitemcollectionadd).

---

## Attributes

### RenderQueueItem.comp

`app.project.renderQueue.item(index).comp`

#### Description

The composition that will be rendered by this render-queue item. To change the composition, you must delete this render-queue item and create a new one.

#### Type

[CompItem object](../item/compitem.md); read-only.

---

### RenderQueueItem.elapsedSeconds

`app.project.renderQueue.item(index).elapsedSeconds`

#### Description

The number of seconds spent rendering this item.

#### Type

Integer, or `null` if item has not been rendered; read-only.

---

### RenderQueueItem.logType

`app.project.renderQueue.item(index).logType`

#### Description

A log type for this item, indicating which events should be logged while this item is being rendered.

#### Type

A `LogType` enumerated value; (read/write). One of:

- `LogType.ERRORS_ONLY`
- `LogType.ERRORS_AND_SETTINGS`
- `LogType.ERRORS_AND_PER_FRAME_INFO`

---

### RenderQueueItem.numOutputModules

`app.project.renderQueue.item(index).numOutputModules`

#### Description

The total number of Output Modules assigned to this item.

#### Type

Integer; read-only.

---

### RenderQueueItem.onstatus

`app.project.renderQueue.item(index).onstatus`

#### Description

The name of a callback function that is called whenever the value of the [RenderQueueItem.status](#renderqueueitemstatus) attribute changes.

You cannot make changes to render queue items or to the application while rendering is in progress or paused; you can, however, use this callback to pause or stop the rendering process. See [RenderQueue.pauseRendering()](renderqueue.md#renderqueuepauserendering) and [RenderQueue.stopRendering()](renderqueue.md#renderqueuestoprendering). See also [app.onError](../general/application.md#apponerror).

#### Type

A function name string, or `null` if no function is assigned.

#### Example

```javascript
function myStatusChanged() {
    alert(app.project.renderQueue.item(1).status);
}

app.project.renderQueue.item(1).onstatus = myStatusChanged();
app.project.renderQueue.item(1).render = false; // changes status and shows dialog
```

---

### RenderQueueItem.outputModules

`app.project.renderQueue.item(index).outputModules`

#### Description

The collection of Output Modules for the item.

#### Type

[OMCollection object](omcollection.md); read-only.

---

### RenderQueueItem.queueItemNotify

`app.project.renderQueue.item(index).queueItemNotify`

!!! note
    This functionality was added in After Effects 22.0 (2022)

#### Description

Scripts can read and write the **Notify** checkbox for each individual item in the Render Queue. This is exposed in the UI as a checkbox next to each Render Queue item in the Notify column.

This column is hidden by default and may need to be selected to be visible by right clicking on the Render Queue column headers and choosing Notify.

#### Type

Boolean; read/write.

---

### RenderQueueItem.render

`app.project.renderQueue.item(index).render`

#### Description

When `true`, the item will be rendered when the render queue is started. When set to `true`, the [RenderQueueItem.status](#renderqueueitemstatus) is set to `RQItemStatus.QUEUED`. When set to `false`, `status` is set to
`RQItemStatus.UNQUEUED`.

#### Type

Boolean; read/write.

---

### RenderQueueItem.skipFrames

`app.project.renderQueue.item(index).skipFrames`

#### Description

The number of frames to skip when rendering this item. Use this to do rendering tests that are faster than a full render. A value of 0 skip no frames, and results in regular rendering of all frames. A value of 1 skips every other frame. This is equivalent to "rendering on twos." Higher values skip a larger number of frames. The total length of time remains unchanged. For example, if skip has a value of 1, a sequence output would have half the number of frames and in movie output, each frame would be double the duration.

#### Type

Integer, in the range `[0..99]`; read/write.

---

### RenderQueueItem.startTime

`app.project.renderQueue.item(index).startTime`

#### Description

The day and time that this item started rendering.

#### Type

Date object, or `null` if the item has not started rendering; read-only.

---

### RenderQueueItem.status

`app.project.renderQueue.item(index).status`

#### Description

The current render status of the item.

#### Type

An `RQItemStatus` enumerated value; read-only. One of:

- `RQItemStatus.WILL_CONTINUE`: Rendering process has been paused.
- `RQItemStatus.NEEDS_OUTPUT`: Item lacks a valid output path.
- `RQItemStatus.UNQUEUED`: Item is listed in the Render Queue panel but composition is not ready to render.
- `RQItemStatus.QUEUED`: Composition is ready to render.
- `RQItemStatus.RENDERING`: Composition is rendering
- `RQItemStatus.USER_STOPPED`: Rendering process was stopped by user or script.
- `RQItemStatus.ERR_STOPPED`: Rendering process was stopped due to an error.
- `RQItemStatus.DONE`: Rendering process for the item is complete.

---

### RenderQueueItem.templates

`app.project.renderQueue.item(index).templates`

#### Description

The names of all Render Settings templates available for the item. See also [RenderQueueItem.saveAsTemplate()](#renderqueueitemsaveastemplate).

#### Type

Array of strings; read-only.

---

### RenderQueueItem.timeSpanDuration

`app.project.renderQueue.item(index).timeSpanDuration`

#### Description

The duration in seconds of the composition to be rendered. The duration is determined by subtracting the start time from the end time. Setting this value is the same as setting a custom end time in the Render Settings dialog box.

#### Type

Floating-point value; read/write.

---

### RenderQueueItem.timeSpanStart

`app.project.renderQueue.item(index).timeSpanStart`

#### Description

The time in the composition, in seconds, at which rendering will begin. Setting this value is the same as setting a custom start time in the Render Settings dialog box.

#### Type

Floating-point value; read/write.

---

## Methods

### RenderQueueItem.applyTemplate()

`app.project.renderQueue.item(index).applyTemplate(templateName)`

#### Description

Applies a Render Settings template to the item. See also [RenderQueueItem.saveAsTemplate()](#renderqueueitemsaveastemplate) and [RenderQueueItem.templates](#renderqueueitemtemplates).

#### Parameters

|   Parameter    |  Type  |            Description             |
| -------------- | ------ | ---------------------------------- |
| `templateName` | String | The name of the template to apply. |

#### Returns

Nothing.

---

### RenderQueueItem.duplicate()

`app.project.renderQueue.item(index).duplicate()`

#### Description

Creates a duplicate of this item and adds it this render queue.

!!! tip
    Duplicating an item whose status is "Done" sets the new item's status to "Queued".

#### Parameters

None.

#### Returns

RenderQueueItem object.

---

### RenderQueueItem.getSetting()

`app.project.renderQueue.item(index).getSetting()`

!!! note
    This functionality was added in After Effects 13.0 (CC 2014)

#### Description

Gets a specific Render Queue Item setting.

- Depreciated Source: [https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)
- Archived version: [https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)

#### Example

```javascript
// Get current value of render setting's "Proxy Use"
// Key and value strings are English.
var rqItem1_proxyUse = app.project.renderQueue.item(1).getSetting("Proxy Use");

// Get string version of same setting, add "-str" at the end of key string
var rqItem1_proxyUse_str = app.project.renderQueue.item(1).getSetting("Proxy Use-str");
```

---

### RenderQueueItem.getSettings()

`app.project.renderQueue.item(index).getSettings()`

!!! note
    This functionality was added in After Effects 13.0 (CC 2014)

#### Description

Gets all settings for a given Render Queue Item.

- Depreciated Source: [https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)
- Archived version: [https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)

#### Example

```javascript
// Get object that contains all possible values of all render settings of
// render queue item 1 and convert to JSON format.

var rqItem1_spec_str = app.project.renderQueue.item(1).getSettings(GetSettingsFormat.SPEC);
var rqItem1_spec_str_json = rqItem1_spec_str.toSource();
```

---

### RenderQueueItem.outputModule()

`app.project.renderQueue.item(index).outputModule(index)`

#### Description

Gets an output module with the specified index position.

#### Parameters

| Parameter |                     Type                      |               Description                |
| --------- | --------------------------------------------- | ---------------------------------------- |
| `index`   | Integer, in the range `[1..numOutputModules]` | The position index of the output module. |

#### Returns

OutputModule object.

---

### RenderQueueItem.remove()

`app.project.renderQueue.item(index).remove()`

#### Description

Removes this item from the render queue.

#### Parameters

None.

#### Returns

Nothing.

---

### RenderQueueItem.saveAsTemplate()

`app.project.renderQueue.item(index).saveAsTemplate(name)`

#### Description

Saves the item's current render settings as a new template with the specified name.

#### Parameters

| Parameter |  Type  |          Description          |
| --------- | ------ | ----------------------------- |
| `name`    | String | The name of the new template. |


#### Returns

Nothing.

---

### RenderQueueItem.setSetting()

`app.project.renderQueue.item(index).setSetting()`

!!! note
    This functionality was added in After Effects 13.0 (CC 2014)

#### Description

Sets a specific setting for a given Render Queue Item.

Depreciated Source: [https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)

Archived version: [https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)

#### Example

```javascript
// Set value of "Proxy Use" to "Use All Proxies"

app.project.renderQueue.item(1).setSetting("Proxy Use", "Use All Proxies");

// You can use numbers, too.
// The next line does the same as the previous example.

app.project.renderQueue.item(1).setSetting("Proxy Use", 1);
```

---

### RenderQueueItem.setSettings()

`app.project.renderQueue.item(index).setSettings()`

!!! note
    This functionality was added in After Effects 13.0 (CC 2014)

#### Description

Sets a multiple settings for a given Render Queue Item.

- Depreciated Source: [https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)
- Archived version: [https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva](https://web.archive.org/web/20200622100656/https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/?segment=dva)

#### Example

```javascript
// Get an object that contains string version of settable render setting
// values of render queue item 1.
// To get the values in the number format, use
// GetSettingsFormat.NUMBER_SETTABLE as an argument.

var rqItem1_settable_str = app.project.renderQueue.item(1).getSettings( GetSettingsFormat.STRING_SETTABLE );

// Set render queue item 2 with values that you got from render
//queue item 1.

app.project.renderQueue.item(2).setSettings( rqItem1_settable_str );

// Set render queue item 3 with values you create.

var my_renderSettings = {
    "Color Depth":        "32 bits per channel",
    "Quality":            "Best",
    "Effects":            "All On",
    "Time Span Duration": "1.0",
    "Time Span Start":    "2.0"
};

app.project.renderQueue.item(2).setSettings( my_renderSettings );
```
