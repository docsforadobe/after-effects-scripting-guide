# GuideOptions object

`new GuideOptions()`

!!! note
    This functionality was added in After Effects (Beta) 26.5 and is subject to change while it remains in Beta.

#### Description

A configuration object passed to [Item.addGuide()](../item/item.md#itemaddguide), [Item.setGuide()](../item/item.md#itemsetguide), and the corresponding [Layer](../layer/layer.md) methods, and returned by [Item.getGuideAsObject()](../item/item.md#itemgetguideasobject). Every property is optional; when used with `setGuide`, only the properties you set are changed, enabling partial updates.

#### Example

```javascript
var opts = new GuideOptions();
opts.orientation = GuideOrientationType.VERTICAL;
opts.position = 50;
opts.positionType = GuidePositionType.PERCENTAGE;
opts.color = [1.0, 0.0, 1.0];   // magenta
opts.pinned = true;
app.project.item(1).addGuide(opts);
```

---

## Attributes

### GuideOptions.orientation

`guideOptions.orientation`

#### Description

The guide's orientation: [GuideOrientationType.HORIZONTAL](#guideorientationtype) or [GuideOrientationType.VERTICAL](#guideorientationtype).

#### Type

A `GuideOrientationType` enumerated value; read/write.

---

### GuideOptions.position

`guideOptions.position`

#### Description

The guide's position, in pixels or percent depending on `positionType`. Clamped to ±100,000 px or ±300%; non-finite values are rejected.

#### Type

Floating-point value; read/write.

---

### GuideOptions.positionType

`guideOptions.positionType`

#### Description

How `position` is interpreted: [GuidePositionType.PIXEL](#guidepositiontype) or [GuidePositionType.PERCENTAGE](#guidepositiontype).

#### Type

A `GuidePositionType` enumerated value; read/write.

---

### GuideOptions.color

`guideOptions.color`

#### Description

The guide's color as an array of three floats, `[R, G, B]`, each in the range `0.0`-`1.0`.

#### Type

Array of 3 floating-point values; read/write.

---

### GuideOptions.pinned

`guideOptions.pinned`

#### Description

When `true`, the guide is pinned to the opposite edge (bottom for horizontal guides, right for vertical guides).

#### Type

Boolean; read/write.

---

## GuideOrientationType

The orientation of a guide, used by [GuideOptions.orientation](#guideoptionsorientation) and the [Item.guides](../item/item.md#itemguides) / [Layer.guides](../layer/layer.md#layerguides) properties.

| Value                             | Description          |
| --------------------------------- | -------------------- |
| `GuideOrientationType.HORIZONTAL` | A horizontal guide.  |
| `GuideOrientationType.VERTICAL`   | A vertical guide.    |

!!! note
    These enumerated constants were added in After Effects (Beta) 26.5 and are subject to change while they remain in Beta. Always compare `orientationType` against these constants rather than raw integers, because the underlying integer values differ between versions of After Effects. In the non-beta application the constants are unavailable and [Item.guides](../item/item.md#itemguides) / [Layer.guides](../layer/layer.md#layerguides) report `orientationType` as a plain integer (`0` for horizontal, `1` for vertical).

---

## GuidePositionType

How a guide's `position` value is interpreted, used by [GuideOptions.positionType](#guideoptionspositiontype) and the [Item.guides](../item/item.md#itemguides) / [Layer.guides](../layer/layer.md#layerguides) properties.

| Value                          | Description                                          |
| ------------------------------ | ---------------------------------------------------- |
| `GuidePositionType.PIXEL`      | `position` is measured in pixels.                    |
| `GuidePositionType.PERCENTAGE` | `position` is measured as a percentage of the frame. |

!!! note
    These enumerated constants were added in After Effects (Beta) 26.5 and are subject to change while they remain in Beta. Always compare `positionType` against these constants rather than raw integers, because the underlying integer values differ between versions of After Effects. In the non-beta application the constants are unavailable and [Item.guides](../item/item.md#itemguides) / [Layer.guides](../layer/layer.md#layerguides) report `positionType` as a plain integer (always `0`, pixels).
