# View object

`app.activeViewer.views[0]`

#### Description

The View object represents a specific view.

---

## Attributes

### View.active

`app.activeViewer.views[0].active`

#### Description

When `true`, indicates if the viewer panel is focused, and thereby frontmost.

#### Type

Boolean; read-only.

---

### View.options

`app.activeViewer.views[0].options`

#### Description

Options object for this View

#### Type

[ViewOptions object](viewoptions.md)

---

## Methods

### View.setActive()

`app.activeViewer.views[0].setActive()`

#### Description

Moves this view panel to the front and places focus on it, making it active.
Calling this method will set the [view's active attribute](#viewactive) to `true`.

#### Parameters

None.

#### Returns

Boolean, indicating if the view panel was made active.
