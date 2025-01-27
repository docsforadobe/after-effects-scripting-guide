# PropertyGroup object

`app.project.item(index).layer(index).propertyGroupSpec`

#### Description

The PropertyGroup object represents a group of properties. It can contain Property objects and other PropertyGroup objects. Property groups can be nested to provide a parent-child hierarchy, with a Layer object at the top (root) down to a single Property object, such as the mask feather of the third mask. To traverse the group hierarchy, use PropertyBase methods and attributes; see [PropertyBase.propertyGroup()](propertybase.md#propertybasepropertygroup). For examples of how to access properties and property groups, see [PropertyBase object](propertybase.md).

!!! info
    PropertyGroup is a subclass of [PropertyBase](propertybase.md). All methods and attributes of PropertyBase, in addition to those listed below, are available when working with PropertyGroup.

!!! info
    PropertyGroup is a base class for [Layer](../layer/layer.md) and [MaskPropertyGroup](maskpropertygroup.md). PropertyGroup attributes and methods are available when working with layer or mask groups.

---

## Attributes

### PropertyGroup.numProperties

`app.project.item(index).layer(index).propertyGroupSpec.numProperties`

#### Description

The number of indexed properties in this group.

For layers, this method returns a value of 3, corresponding to the mask, effect, and motion tracker groups, which are the indexed groups within the layer.

However, layers also have many other properties available only by name; see [PropertyGroup.property()](#propertygroupproperty).

#### Type

Integer; read-only.

---

## Methods

### PropertyGroup.addProperty()

`app.project.item(index).layer(index).propertyGroupSpec.addProperty(name)`

#### Description

Creates and returns a PropertyBase object with the specified name, and adds it to this group.

In general, you can only add properties to an indexed group (a property group that has the type `PropertyType.INDEXED_GROUP`; see [PropertyBase.propertyType](propertybase.md#propertybasepropertytype)).
The only exception is a text animator property, which can be added to a named group (a property group that has the type `PropertyType.NAMED_GROUP`).

If this method cannot create a property with the specified name, it generates an exception.

To check that you can add a particular property to this group, call `canAddProperty` before calling this method. (See [PropertyGroup.canAddProperty()](#propertygroupcanaddproperty).)

!!! warning
    When you add a new property to an indexed group, the indexed group gets recreated from scratch, invalidating all existing references to properties.

One workaround is to store the index of the added property with property.propertyIndex.

#### Examples


This won't work, as the slider object becomes invalid once we add the Color Control property:

```javascript
var effectsProperty = layer.property("ADBE Effect Parade");
var slider = effectsProperty.addProperty("ADBE Slider Control");
var color = effectsProperty.addProperty("ADBE Color Control");

var sliderProperty = slider.property("ADBE Slider Control-0001"); // Object 'slider' is Invalid
```

This revised method will work:

```javascript
var effectsProperty = layer.property("ADBE Effect Parade");
var slider = effectsProperty.addProperty("ADBE Slider Control");
var sliderIndex = slider.propertyIndex; // Store 'slider' effect index so it can be reused later
var color = effectsProperty.addProperty("ADBE Color Control");

var sliderProperty = effectsProperty.property(sliderIndex).property("ADBE Slider Control-0001");
```

#### Parameters

| Parameter |  Type  |                                                                                                                                                                                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`    | String | The display name or match name of the property to add. (See [PropertyBase.matchName](propertybase.md#propertybasematchname)). The following names are supported:<ul><li>Any match name for a property that can be added through the user interface. For example, `"ADBE Mask Atom`", `"ADBE Paint Atom`", `"ADBE Text Position`", `"ADBE Text Anchor Point`".</li><li>When adding to an ADBE Mask Parade: `"ADBE Mask Atom`", `"Mask`".</li><li>When adding to an ADBE Effect Parade, any effect by match name, such as `"ADBE Bulge`", `"ADBE Glo2`", `"APC Vegas`".</li><li>Any effect by display name, such as `"Bulge`", `"Glow`", `"Vegas`".</li><li>For text animators, `"ADBE Text Animator`".</li><li>For selectors, Range Selector has the name `"ADBE Text Selector`", Wiggly Selector has the name `"ADBE Text Wiggly Selector`", and Expression Selector has the name `"ADBE Text Expressible Selector`".</li></ul> |

#### Returns

[PropertyBase object](propertybase.md).

---

### PropertyGroup.canAddProperty()

`app.project.item(index).layer(index).propertyGroupSpec.canAddProperty(name)`

#### Description

Returns `true` if a property with the given name can be added to this property group.

For example, you can only add mask to a mask group. The only legal input arguments are "mask" or "ADBE Mask Atom".

```javascript
maskGroup.canAddProperty("mask"); // returns `true`
maskGroup.canAddProperty("ADBE Mask Atom"); // returns `true`
maskGroup.canAddProperty("blend"); // returns false
```

#### Parameters

| Parameter |  Type  |                                                          Description                                                          |
| --------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `name`    | String | The display name or match name of the property to be checked. (See [PropertyGroup.addProperty()](#propertygroupaddproperty)). |

#### Returns

Boolean.

---

### PropertyGroup.property()

`app.project.item(index).layer(index).propertyGroupSpec.property(index)`
<br/>
`app.project.item(index).layer(index).propertyGroupSpec.property(name)`
<br/>

#### Description

Finds and returns a child property of this group, as specified by either its index or name. A name specification can use the same syntax that is available with expressions. The following are all allowed and are equivalent:

```javascript
mylayer.position;
mylayer("position");
mylayer.property("position");
mylayer(1);
mylayer.property(1);
```

Some properties of a layer, such as position and zoom, can be accessed only by name. When using the name to find a property that is multiple levels down, you must make more than one call to this method.

For example, the following call searches two levels down, and returns the first mask in the mask group: `myLayer.property("ADBE Masks").property(1)`

#### Parameters

| Parameter |                    Type                    |                                                                                                                                              Description                                                                                                                                               |
| --------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `index`   | Integer, in the range `[1..numProperties]` | The index for the child property, in this is an indexed group.                                                                                                                                                                                                                                         |
| `name`    | String                                     | The name of the child property. This can be:<ul><li>Any match name</li><li>Any name in expression "parenthesis style" syntax, meaning the display name or the compact English name</li><li>Any name in expression "intercap style" syntax.</li></ul>For supported property names, see the table below. |

#### Returns

[PropertyBase object](propertybase.md) or `null` if no child property with the specified string name is found.

#### Properties accessible by name

|                 Source                  |                                                                                                                                                                                                                                          Values                                                                                                                                                                                                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From any Layer                          | <ul><li>`"ADBE Mask Parade`", or `"Masks`"</li><li>`"ADBE Effect Parade`", or `"Effects`"</li><li>`"ADBE MTrackers`", or `"Motion Trackers`"</li></ul>                                                                                                                                                                                                                                                                                                                                   |
| From an AVLayer                         | <ul><li>`"Anchor Point`" or `"anchorPoint`"</li><li>`"Position`" or `"position`"</li><li>`"Scale`" or `"scale`"</li><li>`"Rotation`" or `"rotation`"</li><li>`"Z Rotation`" or `"zRotation`" or `"Rotation Z`" or `"rotationZ`"</li><li>`"Opacity`" or `"opacity`"</li><li>`"Marker`" or `"marker`"</li></ul>                                                                                                                                                                            |
| From an AVLayer with a non-still source | <ul><li>`"Time Remap`" or `"timeRemapEnabled`"</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| From an AVLayer with an audio component | <ul><li>`"Audio Levels`" or `"audioLevels`"</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| From a camera layer                     | <ul><li>`"Zoom`" or `"zoom`"</li><li>`"Depth of Field`" or `"depthOfField`"</li><li>`"Focus Distance`" or `"focusDistance`"</li><li>`"Aperture`" or `"aperture`"</li><li>`"Blur Level`" or `"blurLevel`"</li></ul>                                                                                                                                                                                                                                                                       |
| From a light layer                      | <ul><li>`"Intensity`" or `"intensity`"</li><li>`"Color`" or `"color`"</li><li>`"Cone Angle`" or `"coneAngle`"</li><li>`"Cone Feather`" or `"coneFeather`"</li><li>`"Shadow Darkness`" or `"shadowDarkness`"</li><li>`"Shadow Diffusion`" or `"shadowDiffusion`"</li><li>`"Casts Shadows`" or `"castsShadows`"</li></ul>                                                                                                                                                                  |
| From a 3D layer                         | <ul><li>`"Accepts Shadows`" or `"acceptsShadows`"</li><li>`"Accepts Lights`" or `"acceptsLights`"</li><li>`"Ambient`" or `"ambient`"</li><li>`"Diffuse`" or `"diffuse`"</li><li>`"Specular`" or `"specular`" (these are for the Specular Intensity property)</li><li>`"Shininess`" or `"shininess`" (these are for the Specular Shininess property)</li><li>`"Casts Shadows`" or `"castsShadows`"</li><li>`"Light Transmission`" or `"lightTransmission`"</li><li>`"Metal`" or `"metal`" |
| From a camera, light or 3D layer        | <ul><li>`"X Rotation`" or `"xRotation`" or `"Rotation X`" or `"rotationX`"</li><li>`"Y Rotation`" or `"yRotation`" or `"Rotation Y`" or `"rotationY`"</li><li>`"Orientation`" or `"orientation`"</li></ul>                                                                                                                                                                                                                                                                               |
| From a text layer                       | <ul><li>`"Source Text`" or `"source Text`" or `"Text`" or `"text`"</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                             |
| From PropertyGroup `"ADBE Mask Parade`" | <ul><li>`"ADBE Mask Atom`"</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| From PropertyGroup `"ADBE Mask Atom`"   | <ul><li>`"ADBE Mask Shape`", or `"maskShape`", or `"maskPath`"</li><li>`"ADBE Mask Feather`", or `"maskFeather`"</li><li>`"ADBE Mask Opacity`", or `"maskOpacity`"</li><li>`"ADBE Mask Offset`", or `"maskOffset"`</li></ul>                                                                                                                                                                                                                                                             |

#### Examples

If a layer named "myLayer" has a Box Blur effect, you can retrieve the effect in any of the following ways:

```javascript
myLayer.property("Effects").property("Box Blur");
myLayer.property("Effects").property("boxBlur");
myLayer.property("Effects").property("ADBE Box Blur");
```

If a layer named "myLayer" has a mask named "Mask 1" you can retrieve it as follows:

```javascript
myLayer.property("Masks").property("Mask1");
```

To get a Bulge Center value from a Bulge effect, you can use either of the following:

```javascript
myLayer.property("Effects").property("Bulge").property("Bulge Center");
myLayer.property("Effects").property("Bulge").property("bulgeCenter");
```
