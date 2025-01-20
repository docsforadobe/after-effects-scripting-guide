# ViewOptions object

`app.activeViewer.views[0].options`

#### Description

The ViewOptions object represents the options for a given [View object](view.md)

#### Example

This enables checkerboards and locks guides for a given view

```javascript
var activeViewer = app.activeViewer;
var viewOptions = activeViewer.views[0].options;
viewOptions.checkerboards = true;
viewOptions.guidesLocked = true;
```

---

## Attributes

### ViewOptions.channels

`app.activeViewer.views[0].options.channels`

#### Description

The state of the Channels menu.

#### Type

A `ChannelType` enumerated value; read/write. One of:

- `CHANNEL_ALPHA`
- `CHANNEL_ALPHA_BOUNDARY`
- `CHANNEL_ALPHA_OVERLAY`
- `CHANNEL_BLUE`
- `CHANNEL_BLUE_COLORIZE`
- `CHANNEL_GREEN`
- `CHANNEL_GREEN_COLORIZE`
- `CHANNEL_RED`
- `CHANNEL_RED_COLORIZE`
- `CHANNEL_RGB`
- `CHANNEL_RGB_STRAIGHT`

---

### ViewOptions.checkerboards

`app.activeViewer.views[0].options.checkerboards`

#### Description

When `true`, checkerboards (transparency grid) is enabled in the current view.

#### Type

Boolean; read/write.

---

### ViewOptions.exposure

`app.activeViewer.views[0].options.exposure`

#### Description

The exposure value for the current view.

#### Type

Floating-point value, in the range `[-40..40]`

---

### ViewOptions.fastPreview

`app.activeViewer.views[0].options.fastPreview`

!!! note
    This functionality was added in After Effects 12.0 (CC)

#### Description

The state of the Fast Previews menu. This is a read/write attribute using an enumerated value:

!!! warning
    If you try to get or set the attribute's value in the Layer or Footage panel, you'll get an error message.

!!! tip
    The Draft preview mode is only available in ray-traced 3D compositions. If you try to use it in a Classic 3D composition, you'll get an error: "Cannot set Draft fast preview mode in a Classic 3D composition."

#### Type

A `FastPreviewType` enumerated value; read/write. One of:

- `FastPreviewType.FP_OFF`: Off (Final Quality)
- `FastPreviewType.FP_ADAPTIVE_RESOLUTION`: Adaptive Resolution
- `FastPreviewType.FP_DRAFT`: Draft
- `FastPreviewType.FP_FAST_DRAFT`: Fast Draft
- `FastPreviewType.FP_WIREFRAME`: Wireframe

#### Example

```javascript
app.activeViewer.views[0].options.fastPreview === FastPreviewType.FP_ADAPTIVE_RESOLUTION;
app.activeViewer.views[0].options.fastPreview === FastPreviewType.FP_DRAFT;
app.activeViewer.views[0].options.fastPreview === FastPreviewType.FP_FAST_DRAFT;
app.activeViewer.views[0].options.fastPreview === FastPreviewType.FP_OFF;
app.activeViewer.views[0].options.fastPreview === FastPreviewType.FP_WIREFRAME;
```

---

### ViewOptions.guidesLocked

`app.activeViewer.views[0].options.guidesLocked`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

When `true`, indicates guides are locked in the view.

#### Type

Boolean; read/write.

#### Example

```javascript
app.activeViewer.views[0].options.guidesLocked;
```

---

### ViewOptions.guidesSnap

`app.activeViewer.views[0].options.guidesSnap`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

When `true`, indicates layers snap to guides when dragged in the view.

#### Type

Boolean; read/write.

#### Example

```javascript
app.activeViewer.views[0].options.guidesSnap;
```

---

### ViewOptions.guidesVisibility

`app.activeViewer.views[0].options.guidesVisibility`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

When `true`, indicates guides are visible in the view.

#### Type

Boolean; read/write.

#### Example

```javascript
app.activeViewer.views[0].options.guidesVisibility;
```

---

### ViewOptions.rulers

`app.activeViewer.views[0].options.rulers`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

When `true`, indicates rulers are shown in the view.

#### Type

Boolean; read/write.

#### Example

```javascript
app.activeViewer.views[0].options.rulers;
```

---

### ViewOptions.zoom

`app.activeViewer.views[0].options.zoom`

#### Description

Sets the current zoom value for the view, as a normalized percentage between 1% (0.01) and 1600% (16).

#### Type

Floating-point value, in the range `[0.01..16]`
