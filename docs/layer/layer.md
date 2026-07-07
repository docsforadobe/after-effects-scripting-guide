# Layer object

`app.project.item(index).layer(index)`

#### Description

The Layer object provides access to layers within compositions. It can be accessed from an item's layer collection either by index number or by a name string.

!!! info
    Layer is a subclass of [PropertyGroup](../property/propertygroup.md), which is a subclass of [PropertyBase](../property/propertybase.md). All methods and attributes of PropertyGroup, in addition to those listed below, are available when working with Layer, with the exception that `propertyIndex` attribute is set to `undefined`.

!!! info
    Layer is the base class for [CameraLayer object](cameralayer.md), [LightLayer object](lightlayer.md), and [AVLayer object](avlayer.md), so Layer attributes and methods are available when working with all layer types. Layers contain AE properties, in addition to their JavaScript attributes and methods. For examples of how to access properties in layers, see [PropertyBase object](../property/propertybase.md).

#### Example

If the first item in the project is a [CompItem](../item/compitem.md), this example disables the first layer in that composition and renames it. This might, for example, turn an icon off in the composition.

```javascript
var firstLayer = app.project.item(1).layer(1);
firstLayer.enabled = false;
firstLayer.name = "DisabledLayer";
```

---

## Attributes

### Layer.autoOrient

`app.project.item(index).layer(index).autoOrient`

#### Description

The type of automatic orientation to perform for the layer.

#### Type

An `AutoOrientType` enumerated value; read/write. One of:

- `AutoOrientType.ALONG_PATH` Layer faces in the direction of the motion path.
- `AutoOrientType.CAMERA_OR_POINT_OF_INTEREST` Layer always faces the active camera or points at its point of interest.
- `AutoOrientType.CHARACTERS_TOWARD_CAMERA` Each character in a per-character 3D text layer automatically faces the active camera.
- `AutoOrientType.NO_AUTO_ORIENT` Layer rotates freely, independent of any motion path, point of interest, or other layers.

---

### Layer.comment

`app.project.item(index).layer(index).comment`

#### Description

A descriptive comment for the layer.

#### Type

String; read/write.

---

### Layer.containingComp

`app.project.item(index).layer(index).containingComp`

#### Description

The composition that contains this layer.

#### Type

CompItem object; read-only.

---

### Layer.guides

`app.project.item(index).layer(index).guides`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

An array of objects describing the guides in the layer's view. The properties on each entry depend on the version of After Effects.

In After Effects 16.1 (CC 2019) and later, each entry has the following properties:

| Property          | Type                 | Description                                           |
| ----------------- | -------------------- | ----------------------------------------------------- |
| `orientationType` | Integer              | `0` for a horizontal guide, `1` for a vertical guide. |
| `positionType`    | Integer              | Always `0` (a pixel position).                        |
| `position`        | Floating-point value | The guide's position, in pixels.                      |

In After Effects (Beta) 26.5 and later, each entry has the following properties:

| Property          | Type                   | Description                                                              |
| ----------------- | ---------------------- | ------------------------------------------------------------------------ |
| `orientationType` | `GuideOrientationType` | `GuideOrientationType.HORIZONTAL` or `GuideOrientationType.VERTICAL`.     |
| `positionType`    | `GuidePositionType`    | `GuidePositionType.PIXEL` or `GuidePositionType.PERCENTAGE`.             |
| `position`        | Floating-point value   | The guide's position, in pixels or percent depending on `positionType`.  |
| `color`           | Array of 3 floats      | `[R, G, B]`, each `0.0`-`1.0`.                                            |
| `pinned`          | Boolean                | `true` if pinned to the opposite (bottom/right) edge.                    |

!!! warning "Differences between versions"
    **Breaking change:** The integer values behind `orientationType` and `positionType` differ between versions of After Effects. In the beta, always compare against the enumerated constants (for example [GuideOrientationType.HORIZONTAL](../other/guideoptions.md#guideorientationtype)) rather than raw integer literals — a test such as `guide.orientationType === 0` is not portable and may stop matching in a future version.

#### Type

Array of objects; read-only.

---

### Layer.hasVideo

`app.project.item(index).layer(index).hasVideo`

#### Description

When `true`, the layer has a video switch (the eyeball icon) in the Timeline panel; otherwise `false`.

#### Type

Boolean; read-only.

---

### Layer.id

`app.project.item(index).layer(index).id`

!!! note
    This functionality was added in After Effects 22.0 (2022)

#### Description

Instance property on Layer which returns a unique and persistent identification number used internally to identify a Layer between sessions.

The value of the ID remains the same when the project is saved to a file and later reloaded.

However, when you import this project into another project, new IDs are assigned to all Layers in the imported project.
The ID is not displayed anywhere in the user interface..

#### Type

Integer; read-only.

---

### Layer.index

`app.project.item(index).layer(index).index`

#### Description

The index position of the layer.

#### Type

Integer, in the range `[1..numLayers]`; read-only.

---

### Layer.inPoint

`app.project.item(index).layer(index).inPoint`

#### Description

The "in" point of the layer, expressed in composition time (seconds).

#### Type

Floating-point value, in the range `[-10800.0..10800.0]` (minus or plus three hours); read/write.

---

### Layer.isNameSet

`app.project.item(index).layer(index).isNameSet`

#### Description

`true` if the value of the name attribute has been set explicitly, rather than automatically from the source.

!!! tip
    This always returns `true` for layers that do not have a [AVLayer.source](avlayer.md#avlayersource)

#### Type

Boolean; read-only.

---

### Layer.label

`app.project.item(index).layer(index).label`

#### Description

The label color for the item. Colors are represented by their number (0 for None, or 1 to 16 for one of the preset colors in the Labels preferences).

!!! tip
    Custom label colors cannot be set programmatically.

#### Type

Integer (0 to 16); read/write.

---

### Layer.locked

`app.project.item(index).layer(index).locked`

#### Description

When `true`, the layer is locked; otherwise `false`. This corresponds to the lock toggle in the Layer panel.

#### Type

Boolean; read/write.

---

### Layer.marker

`app.project.item(index).layer(index).marker`

#### Description

A [PropertyGroup object](../property/propertygroup.md) that contains all a layer's markers. Layer marker scripting has the same functionality as [Comp markers](../item/compitem.md#compitemmarkerproperty).

See [MarkerValue object](../other/markervalue.md).

#### Type

PropertyGroup object or `null`; read-only.

#### Example

The following sample code creates two layer markers with different properties

```javascript
var solidLayer = comp.layers.addSolid([1, 1, 1], "mylayer", 1920, 1080, 1.0);

var layerMarker = new MarkerValue("This is a layer marker!");
layerMarker.duration = 1;

var layerMarker2 = new MarkerValue("Another comp marker!");
layerMarker2.duration = 1;

solidLayer.marker.setValueAtTime(1, layerMarker);
solidLayer.marker.setValueAtTime(3, layerMarker2);
```

---

### Layer.nullLayer

`app.project.item(index).layer(index).nullLayer`

#### Description

When `true`, the layer was created as a null object; otherwise `false`.

#### Type

Boolean; read-only.

---

### Layer.outPoint

`app.project.item(index).layer(index).outPoint`

#### Description

The "out" point of the layer, expressed in composition time (seconds).

#### Type

Floating-point value, in the range `[-10800.0..10800.0]` (minus or plus three hours); read/write.

---

### Layer.parent

`app.project.item(index).layer(index).parent`

#### Description

The parent of this layer; can be `null`.

Offset values are calculated to counterbalance any transforms above this layer in the hierarchy, so that when you set the parent there is no apparent jump in the layer's transform.

For example, if the new parent has a rotation of 30 degrees, the child layer is assigned a rotation of -30 degrees.

To set the parent without changing the child layer's transform values, use the [setParentWithJump](#layersetparentwithjump) method.

#### Type

Layer object or `null`; read/write.

---

### Layer.selectedProperties

`app.project.item(index).layer(index).selectedProperties`

#### Description

An array containing all of the currently selected [Property](../property/property.md) and [PropertyGroup](../property/propertygroup.md) objects in the layer.

#### Type

Array of [PropertyBase](../property/propertybase.md) objects; read-only.

---

### Layer.shy

`app.project.item(index).layer(index).shy`

#### Description

When `true`, the layer is "shy", meaning that it is hidden in the Layer panel if the composition's "Hide all shy layers" option is toggled on.

#### Type

Boolean; read/write.

---

### Layer.solo

`app.project.item(index).layer(index).solo`

#### Description

When `true`, the layer is soloed, otherwise `false`.

#### Type

Boolean; read/write.

---

### Layer.startTime

`app.project.item(index).layer(index).startTime`

#### Description

The start time of the layer, expressed in composition time (seconds).

#### Type

Floating-point value, in the range `[-10800.0..10800.0]` (minus or plus three hours); read/write.

---

### Layer.stretch

`app.project.item(index).layer(index).stretch`

#### Description

The layer's time stretch, expressed as a percentage. A value of 100 means no stretch. Values between 0 and 1 are set to 1, and values between -1 and 0 (not including 0) are set to -1.

#### Type

Floating-point value, in the range `[-9900.0..9900.0]`; read/write.

---

### Layer.time

`app.project.item(index).layer(index).time`

#### Description

The current time of the layer, expressed in composition time (seconds).

#### Type

Floating-point value; read-only.

---

## Methods

### Layer.activeAtTime()

`app.project.item(index).layer(index).activeAtTime(time)`

#### Description

Returns `true` if this layer will be active at the specified time.

To return `true`, the layer must be enabled, no other layer may be soloing unless this layer is soloed too, and the time must be between the `inPoint` and `outPoint` values of this layer.

#### Parameters

| Parameter |         Type         |     Description      |
| --------- | -------------------- | -------------------- |
| `time`    | Floating-point value | The time in seconds. |

#### Returns

Boolean.

---

### Layer.addGuide()

`app.project.item(index).layer(index).addGuide(orientationType, position)`

`app.project.item(index).layer(index).addGuide(guideOptions)`

!!! note
    The `(orientationType, position)` form was added in After Effects 16.1 (CC 2019). The `GuideOptions` form was added in After Effects (Beta) 26.5 and is subject to change while it remains in Beta.

#### Description

Adds a guide to the layer's view and returns its index. There are two forms:

- **`addGuide(orientationType, position)`** - adds a pixel guide using an orientation and a pixel position.
- **`addGuide(guideOptions)`** - adds a guide described by a [GuideOptions](../other/guideoptions.md) object, allowing percentage positioning, per-guide color, and pinning. *(After Effects (Beta) 26.5 and later; calling this form in an earlier version raises an error.)*

#### Parameters

|     Parameter     |         Type         |                                                Description                                                |
| ----------------- | -------------------- | --------------------------------------------------------------------------------------------------------- |
| `orientationType` | Integer              | `0` for a horizontal guide, `1` for a vertical guide. Any other value defaults to horizontal. In After Effects (Beta) 26.5 and later you may also pass `GuideOrientationType.HORIZONTAL` / `GuideOrientationType.VERTICAL`. |
| `position`        | Floating-point value | The X or Y coordinate position of the guide in pixels. Clamped to ±100,000; non-finite values are rejected. |
| `guideOptions`    | GuideOptions object  | A [GuideOptions](../other/guideoptions.md) describing the new guide.                                      |

#### Returns

Integer; the index of the newly-created guide.

#### Example

```javascript
var layer = app.project.item(1).layer(1);

// (orientationType, position) form: a vertical guide at 500 px on the X axis.
layer.addGuide(1, 500);

// GuideOptions form: a vertical guide at 50%, red, pinned to the right edge.
var opts = new GuideOptions();
opts.orientation = GuideOrientationType.VERTICAL;
opts.position = 50;
opts.positionType = GuidePositionType.PERCENTAGE;
opts.color = [1, 0, 0];
opts.pinned = true;
layer.addGuide(opts);
```

---

### Layer.applyPreset()

`app.project.item(index).layer(index).applyPreset(presetName);`

#### Description

Applies the specified collection of animation settings (an animation preset) to all the currently selected layers of the comp to which the layer belongs. If no layer is selected, it applies the animation preset to a new solid layer.

Predefined animation preset files are installed in the Presets folder, and users can create new animation presets through the user interface.

!!! warning
    The animation preset is applied to the the selected layer(s) of the comp, not to the layer whose applyPreset function is called. Hence, the layer whose applyPreset function is called effectively just determines the comp whose layers are processed.

#### Parameters

|  Parameter   |                                                 Type                                                  |                Description                |
| ------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `presetName` | [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object | The file containing the animation preset. |

#### Returns

Nothing.

---

### Layer.copyToComp()

`app.project.item(index).layer(index).copyToComp(intoComp)`

#### Description

Copies the layer into the specified composition. The original layer remains unchanged.

Creates a new Layer object with the same values as this one, and prepends the new object to the [LayerCollection object](layercollection.md) in the target CompItem. Retrieve the copy using into `Comp.layer(1)`.

Copying in a layer changes the index positions of previously existing layers in the target composition.

This is the same as copying and pasting a layer through the user interface.

!!! note
    As of After Effects 13.6, this method no longer causes After Effects to crash when the layer has a parent.

!!! warning
    As of After Effects 13.7 (13.6, has not been tested), if the copied layer has an effect on it and the user undoes the action, After Effects will Crash.

#### Parameters

| Parameter  |                  Type                  |       Description       |
| ---------- | -------------------------------------- | ----------------------- |
| `intoComp` | [CompItem object](../item/compitem.md) | The target composition. |

#### Returns

Nothing.

---

### Layer.doSceneEditDetection()

`app.project.item(index).layer(index).doSceneEditDetection(applyOptions)`

!!! note
    This functionality was added in After Effects 22.3 (2022)

#### Description

Runs Scene Edit Detection on the layer that the method is called on and returns an array containing the times of any detected scenes. This is the same as selecting a layer in the Timeline and choosing "Layer > Scene Edit Detection" with the single argument determining whether the edits are applied as markers, layer splits, pre-comps, or are not applied to the layer.

Just as in the UI, `doSceneEditDetection` will fail and error if called on a non-video layer or a video layer with Time Remapping enabled.

#### Parameters

+----------------+-------------------------------+------------------------------------------------------------------------------------------------+
|   Parameter    |             Type              |                                          Description                                           |
+================+===============================+================================================================================================+
| `applyOptions` | `SceneEditDetectionMode` enum | How the detected edits will be applied. One of:                                                |
|                |                               |                                                                                                |
|                |                               | - `SceneEditDetectionMode.MARKERS`: Create markers at edit points.                             |
|                |                               | - `SceneEditDetectionMode.SPLIT`: Split layer.                                                 |
|                |                               | - `SceneEditDetectionMode.SPLIT_PRECOMP`: Split layer at edit points and pre-compose each one. |
|                |                               | - `SceneEditDetectionMode.NONE`: Detected edits are not applied to the layer.                  |
+----------------+-------------------------------+------------------------------------------------------------------------------------------------+

#### Returns

Array of floating-point values; the times of the detected edit points expressed in composition time.

---

### Layer.duplicate()

`app.project.item(index).layer(index).duplicate()`

#### Description

Duplicates the layer. Creates a new Layer object in which all values are the same as in this one. This has the same effect as selecting a layer in the user interface and choosing Edit > Duplicate, except the selection in the user interface does not change when you call this method.

#### Parameters

None.

#### Returns

Layer object.

---

### Layer.getGuideAsObject()

`app.project.item(index).layer(index).getGuideAsObject(guideIndex)`

!!! note
    This functionality was added in After Effects (Beta) 26.5 and is subject to change while it remains in Beta. Calling it in an earlier version raises the error "getGuideAsObject() is not available in this version of After Effects."

#### Description

Returns the guide at the specified index as a [GuideOptions](../other/guideoptions.md) object, which you can modify and pass back to [setGuide()](#layersetguide). This is a convenient way to read a guide's full state (orientation, position, position type, color, pinning).

#### Parameters

|  Parameter   |  Type   |          Description           |
| ------------ | ------- | ------------------------------ |
| `guideIndex` | Integer | The index of the guide to read. |

#### Returns

A [GuideOptions](../other/guideoptions.md) object.

#### Example

```javascript
var layer = app.project.item(1).layer(1);
var g = layer.getGuideAsObject(0);
g.color = [0, 0, 1];   // tweak just the color
layer.setGuide(0, g);   // write it back
```

---

### Layer.moveAfter()

`app.project.item(index).layer(index).moveAfter(layer)`

#### Description

Moves this layer to a position immediately after (below) the specified layer.

#### Parameters

| Parameter |           Type           |                Description                |
| --------- | ------------------------ | ----------------------------------------- |
| `layer`   | [Layer object](layer.md) | The target layer in the same composition. |


#### Returns

Nothing.

---

### Layer.moveBefore()

`app.project.item(index).layer(index).moveBefore(layer)`

#### Description

Moves this layer to a position immediately before (above) the specified layer.

#### Parameters

| Parameter |           Type           |                Description                |
| --------- | ------------------------ | ----------------------------------------- |
| `layer`   | [Layer object](layer.md) | The target layer in the same composition. |

#### Returns

Nothing.

---

### Layer.moveToBeginning()

`app.project.item(index).layer(index).moveToBeginning()`

#### Description

Moves this layer to the topmost position of the layer stack (the first layer).

#### Parameters

None.

#### Returns

Nothing.

---

### Layer.moveToEnd()

`app.project.item(index).layer(index).moveToEnd()`

#### Description

Moves this layer to the bottom position of the layer stack (the last layer).

#### Parameters

None.

#### Returns

Nothing.

---

### Layer.remove()

`app.project.item(index).layer(index).remove()`

#### Description

Deletes the specified layer from the composition.

#### Parameters

None.

#### Returns

Nothing.

---

### Layer.removeGuide()

`app.project.item(index).layer(index).removeGuide(guideIndex)`

!!! note
    This functionality was added in After Effects 16.1 (CC 2019)

#### Description

Removes an existing guide. Choose the guide based on its index inside the [Layer.guides](#layerguides) array.

#### Parameters

|  Parameter   |  Type   |              Description              |
| ------------ | ------- | ------------------------------------- |
| `guideIndex` | Integer | The index of the guide to be removed. |

#### Returns

Nothing.

#### Example

Removes the first guide on the first layer of `activeItem`.

```javascript
app.project.item(1).layer(1).removeGuide(0);
```

!!! warning
    Removing a guide will cause all higher guide indexes to shift downward.

---

### Layer.setGuide()

`app.project.item(index).layer(index).setGuide(position, guideIndex)`

`app.project.item(index).layer(index).setGuide(guideIndex, guideOptions)`

!!! note
    The `(position, guideIndex)` form was added in After Effects 16.1 (CC 2019). The `(guideIndex, guideOptions)` form was added in After Effects (Beta) 26.5 and is subject to change while it remains in Beta.

#### Description

Updates an existing guide. There are two forms, distinguished by the type of the second argument:

- **`setGuide(position, guideIndex)`** - moves the guide at `guideIndex` to a new pixel `position`. *Note the order: position first, index second.* A guide's `orientationType` may not be changed after it is created.
- **`setGuide(guideIndex, guideOptions)`** - applies the properties set on a [GuideOptions](../other/guideoptions.md) object to the guide at `guideIndex`. Only the properties you set are changed (partial update). *(After Effects (Beta) 26.5 and later.)*

!!! warning
    The two forms take their arguments in the **opposite order**: the `(position, guideIndex)` form takes the position first, while the `(guideIndex, guideOptions)` form takes the index first. After Effects decides which form you mean from the type of the second argument (a number selects the `(position, guideIndex)` form; a `GuideOptions` object selects the `(guideIndex, guideOptions)` form).

#### Parameters

|   Parameter    |         Type         |                                               Description                                               |
| -------------- | -------------------- | ------------------------------------------------------------------------------------------------------- |
| `position`     | Floating-point value | The new X or Y coordinate position of the guide in pixels. Clamped to ±100,000; non-finite values are rejected. |
| `guideIndex`   | Integer              | The index of the guide to be modified.                                                                  |
| `guideOptions` | GuideOptions object  | A [GuideOptions](../other/guideoptions.md) whose set properties are applied to the guide.               |

#### Returns

Nothing.

#### Example

```javascript
var layer = app.project.item(1).layer(1);

// (position, guideIndex) form: move guide 0 to 1200 px (position first, index second).
layer.setGuide(1200, 0);

// GuideOptions form: recolor guide 0 and switch it to a percentage position.
var opts = new GuideOptions();
opts.position = 75;
opts.positionType = GuidePositionType.PERCENTAGE;
opts.color = [0, 1, 0];
layer.setGuide(0, opts);   // index first, options second
```

---

### Layer.setParentWithJump()

`app.project.item(index).layer(index).setParentWithJump([newParent])`

#### Description

Sets the parent of this layer to the specified layer, without changing the transform values of the child layer.

There may be an apparent jump in the rotation, translation, or scale of the child layer, as this layer's transform values are combined with those of its ancestors.

If you do not want the child layer to jump, set the [parent](#layerparent) attribute directly. In this case, an offset is calculated and set in the child layer's transform fields, to prevent the jump from occurring.

#### Parameters

|  Parameter  |           Type           |                                       Description                                        |
| ----------- | ------------------------ | ---------------------------------------------------------------------------------------- |
| `newParent` | [Layer object](layer.md) | Optional. A layer in the same composition. If not specified, it sets the parent to None. |

#### Returns

Nothing.
