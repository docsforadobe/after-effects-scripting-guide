<a id="viewer"></a>

# Viewer object

`app.activeViewer`

**Description**

The Viewer object represents a Composition, Layer, or Footage panel.

**Example**

This maximizes the active viewer panel, and displays its type if it contains a composition.

```javascript
var activeViewer = app.activeViewer;
activeViewer.maximized = true;
if (activeViewer.type === ViewerType.VIEWER_COMPOSITION) {
    alert("Composition panel is active.");
}
```

---

## Attributes

<a id="viewer-active"></a>

### Viewer.active

`viewer.active`

**Description**

When true, indicates if the viewer panel is focused, and thereby frontmost.

**Type**

Boolean; read-only.

---

<a id="viewer-activeviewindex"></a>

### Viewer.activeViewIndex

`viewer.activeViewIndex`

**Description**

The index of the current active [View object](view.md#view), in the [Viewer.views](#viewer-views) array.

**Type**

Number; read/write.

---

<a id="viewer-maximized"></a>

### Viewer.maximized

`viewer.maximized`

**Description**

When true, indicates if the viewer panel is at its maximized size.

**Type**

Boolean; read/write.

---

<a id="viewer-views"></a>

### Viewer.views

`viewer.views`

**Description**

All of the Views associated with this viewer.

**Type**

Array of [View object](view.md#view) objects; read-only.

---

<a id="viewer-type"></a>

### Viewer.type

`viewer.type`

**Description**

The content in the viewer panel.

**Type**

A `ViewerType` enumerated value; read-only. One of:

- `ViewerType.VIEWER_COMPOSITION`
- `ViewerType.VIEWER_LAYER`
- `ViewerType.VIEWER_FOOTAGE`

---

## Methods

<a id="viewer-setactive"></a>

### Viewer.setActive()

`viewer.setActive()`

**Description**

Moves the viewer panel to the front and places focus on it, making it active.
Calling this method will set the [viewer’s active attribute](#viewer-active) to true.

**Parameters**

None.

**Returns**

Boolean indicating if the viewer panel was made active.
