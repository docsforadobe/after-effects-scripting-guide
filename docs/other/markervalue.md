# MarkerValue object

`new MarkerValue(comment, chapter, url, frameTarget, cuePointName, params)`

#### Description

The MarkerValue object represents a layer or composition marker, which associates a comment, and optionally a chapter reference point, Web-page link, or Flash Video cue point with a particular point in a layer.

Create it with the constructor; all arguments except `comment` are optional.

All arguments are strings that set in the corresponding attributes of the returned MarkerValue object, except `params`; this is an array containing key-value pairs, which can then be accessed with the [getParameters()](#markervaluegetparameters) and [setParameters()](#markervaluesetparameters) methods.

A script can set any number of parameter pairs; the order does not reflect the order displayed in the application.

To associate a marker with a layer, set the MarkerValue object in the [Layer.marker](../layer/layer.md#layermarker) property of the layer: `layerObject.property("Marker").setValueAtTime(time, markerValueObject);`

To associate a marker with a composition, set the MarkerValue object in the [CompItem.markerProperty](../item/compitem.md#compitemmarkerproperty) property of the comp: `compObject.markerProperty.setValueAtTime(time, markerValueObject);`

For information on the usage of markers see "Using markers" in After Effects Help.

#### Examples

- To set a **layer** marker that says "Fade Up" at the 2 second mark:
    ```javascript
    var myMarker = new MarkerValue("FadeUp");
    myLayer.property("Marker").setValueAtTime(2, myMarker);
    // or
    myLayer.marker.setValueAtTime(2, myMarker);
    ```

- To set a **comp** marker that says "Fade Up" at the 2 second mark:
    ```javascript
    var myMarker = new MarkerValue("FadeUp");
    comp.markerProperty.setValueAtTime(2, myMarker);
    ```

- To get comment values from a particular marker:
    ```javascript
    var layer = app.project.item(1).layer(1);
    var markerProperty = layer.marker;

    var commentOfFirstMarker = markerProperty.keyValue(1).comment;

    // or
    var commentOfMarkerAtTime4 = markerProperty.valueAtTime(4.0, true).comment;

    // or
    var markerValueAtTimeClosestToTime4 = markerProperty.keyValue(markerProperty.nearestKeyIndex(4.0));
    var commentOfMarkerClosestToTime4 = markerValueAtTimeClosestToTime4.comment;
    ```

---

## Attributes

### MarkerValue.chapter

`app.project.item(index).layer(index).property("Marker").keyValue(index).chapter`

#### Description

A text chapter link for this marker. Chapter links initiate a jump to a chapter in a QuickTime movie or in other formats that support chapter marks.

#### Type

String; read/write.

---

### MarkerValue.comment

`app.project.item(index).layer(index).property("Marker").keyValue(index).comment`

#### Description

A text comment for this marker. This comment appears in the Timeline panel next to the layer marker.

#### Type

String; read/write.

---

### MarkerValue.cuePointName

`app.project.item(index).layer(index).property("Marker").keyValue(index).cuePointName`

#### Description

The Flash Video cue point name, as shown in the Marker dialog box.

#### Type

String; read/write.

---

### MarkerValue.duration

`app.project.item(index).layer(index).property("Marker").keyValue(index).duration`

#### Description

The marker's duration, in seconds. The duration appears in the Timeline panel as a short bar extending from the marker location.

#### Type

Floating-point value; read/write.

---

### MarkerValue.eventCuePoint

`app.project.item(index).layer(index).property("Marker").keyValue(index).eventCuePoint`

#### Description

When `true`, the FlashVideo cue point is for an event; otherwise, it is for navigation.

#### Type

Boolean; read/write.

---

### MarkerValue.frameTarget

`app.project.item(index).layer(index).property("Marker").keyValue(index).frameTarget`

#### Description

A text frame target for this marker. Together with the URL value, this targets a specific frame within a Web page.

#### Type

String; read/write.

---

### MarkerValue.url

`app.project.item(index).layer(index).property("Marker").keyValue(index).url`

#### Description

A URL for this marker. This URL is an automatic link to a Web page.

#### Type

String; read/write.

---

### MarkerValue.label

`app.project.item(index).layer(index).property("Marker").keyValue(index).label`

#### Description

The label color for a composition or layer marker. Colors are represented by their number (0 for None, or 1 to 16 for one of the preset colors in the Labels preferences). Custom label colors cannot be set programmatically.

Available in After Effects 16.0 or later.

#### Type

Integer (0 to 16); read/write.

---

### MarkerValue.protectedRegion

`app.project.item(index).markerProperty.keyValue(index).protectedRegion`

#### Description

State of the Protected Region option in the Composition Marker dialog box. When `true`, the composition marker behaves as a protected region. Will also return `true` for protected region markers on nested composition layers, but is otherwise not applicable to layer markers.

Available in After Effects 16.0 or later.

#### Type

Boolean; read/write.

---

## Methods

### MarkerValue.getParameters()

`app.project.item(index).layer(index).property("Marker").keyValue(index).getParameters()`

#### Description

Returns the key-value pairs for Flash Video cue-point parameters, for a cue point associated with this marker value.

#### Parameters

None.

#### Returns

An object with an attribute matching each parameter name, containing that parameter's value.

---

### MarkerValue.setParameters()

`app.project.item(index).layer(index).property("Marker").keyValue(index).setParameters(keyValuePairs)`

#### Description

Associates a set of key-value pairs for Flash Video cue-point parameters, for a cue point associated with this marker value. A cue point can have any number of parameters, but you can add only three through the user interface; use this method to add more than three parameters.

#### Parameters

|    Parameter    |         Type          |                                                                                Description                                                                                |
| --------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keyValuePairs` | Key-value pair object | Object containing the key-value pairs as attributes and values. The object's `toString()` method is called to assign the string value of each attribute to the named key. |

#### Returns

Nothing.

#### Example

```javascript
var mv = new MarkerValue("MyMarker");
var parms = {};
parms.timeToBlink = 1;
parms.assignMe = "A string"
mv.setParameters(parms);
myLayer.property("Marker").setValueAtTime(2, mv);
```
