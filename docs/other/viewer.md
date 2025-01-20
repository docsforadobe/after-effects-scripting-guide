# Viewer object

`app.activeViewer`

#### Description

The Viewer object represents a Composition, Layer, or Footage panel.

#### Example

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

### Viewer.active

`viewer.active`

#### Description

When `true`, indicates if the viewer panel is focused, and thereby frontmost.

#### Type

Boolean; read-only.

---

### Viewer.activeViewIndex

`viewer.activeViewIndex`

#### Description

The index of the current active [View object](view.md), in the [Viewer.views](#viewerviews) array.

#### Type

Integer; read/write.

---

### Viewer.maximized

`viewer.maximized`

#### Description

When `true`, indicates if the viewer panel is at its maximized size.

#### Type

Boolean; read/write.

---

### Viewer.views

`viewer.views`

#### Description

All of the Views associated with this viewer.

#### Type

Array of [View object](view.md) objects; read-only.

---

### Viewer.type

`viewer.type`

#### Description

The content in the viewer panel.

#### Type

A `ViewerType` enumerated value; read-only. One of:

- `ViewerType.VIEWER_COMPOSITION`
- `ViewerType.VIEWER_LAYER`
- `ViewerType.VIEWER_FOOTAGE`

---

## Methods

### Viewer.setActive()

`viewer.setActive()`

#### Description

Moves the viewer panel to the front and places focus on it, making it active.
Calling this method will set the [viewer's active attribute](#vieweractive) to `true`.

#### Parameters

None.

#### Returns

Boolean indicating if the viewer panel was made active.
