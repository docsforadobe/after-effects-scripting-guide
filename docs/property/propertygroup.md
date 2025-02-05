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

+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                                Description                                                                                                |
+===========+========+===========================================================================================================================================================================================================+
| `name`    | String | The display name or [matchName](propertybase.md#propertybasematchname) of the property to add. The following names are supported:                                                                         |
|           |        |                                                                                                                                                                                                           |
|           |        | - Any match name for a property that can be added through the user interface. For example, `"ADBE Mask Atom`", `"ADBE Paint Atom`", `"ADBE Text Position`", `"ADBE Text Anchor Point`".                   |
|           |        | - When adding to an ADBE Mask Parade: `"ADBE Mask Atom`", `"Mask`".                                                                                                                                       |
|           |        | - When adding to an ADBE Effect Parade, any effect by match name, such as `"ADBE Bulge`", `"ADBE Glo2`", `"APC Vegas`".                                                                                   |
|           |        | - Any effect by display name, such as `"Bulge`", `"Glow`", `"Vegas`".                                                                                                                                     |
|           |        | - For text animators, `"ADBE Text Animator`".                                                                                                                                                             |
|           |        | - For selectors, Range Selector has the name `"ADBE Text Selector`", Wiggly Selector has the name `"ADBE Text Wiggly Selector`", and Expression Selector has the name `"ADBE Text Expressible Selector`". |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

`app.project.item(index).layer(index).propertyGroupSpec.property(name)`


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

+-----------+---------+-----------------------------------------------------------------------------------------------------------+
| Parameter |  Type   |                                                Description                                                |
+===========+=========+===========================================================================================================+
| `index`   | Integer | The index for the child property, in the range `[1..numProperties]`, if this is an indexed group.         |
+-----------+---------+-----------------------------------------------------------------------------------------------------------+
| `name`    | String  | The name of the child property. This can be:                                                              |
|           |         |                                                                                                           |
|           |         | - Any match name                                                                                          |
|           |         | - Any name in expression "parenthesis style" syntax, meaning the display name or the compact English name |
|           |         | - Any name in expression "intercap style" syntax.                                                         |
|           |         |                                                                                                           |
|           |         | For supported property names, see the table below.                                                        |
+-----------+---------+-----------------------------------------------------------------------------------------------------------+

#### Returns

[PropertyBase object](propertybase.md) or `null` if no child property with the specified string name is found.

#### Properties accessible by name

+-----------------------------------------+----------------------------------------------------------------------------------+
|                 Source                  |                                      Values                                      |
+=========================================+==================================================================================+
| From any Layer                          | - `"ADBE Mask Parade`", or `"Masks`"                                             |
|                                         | - `"ADBE Effect Parade`", or `"Effects`"                                         |
|                                         | - `"ADBE MTrackers`", or `"Motion Trackers`"                                     |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From an AVLayer                         | - `"Anchor Point`" or `"anchorPoint`"                                            |
|                                         | - `"Position`" or `"position`"                                                   |
|                                         | - `"Scale`" or `"scale`"                                                         |
|                                         | - `"Rotation`" or `"rotation`"                                                   |
|                                         | - `"Z Rotation`" or `"zRotation`" or `"Rotation Z`" or `"rotationZ`"             |
|                                         | - `"Opacity`" or `"opacity`"                                                     |
|                                         | - `"Marker`" or `"marker`"                                                       |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From an AVLayer with a non-still source | - `"Time Remap`" or `"timeRemapEnabled`"                                         |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From an AVLayer with an audio component | - `"Audio Levels`" or `"audioLevels`"                                            |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From a camera layer                     | - `"Zoom`" or `"zoom`"                                                           |
|                                         | - `"Depth of Field`" or `"depthOfField`"                                         |
|                                         | - `"Focus Distance`" or `"focusDistance`"                                        |
|                                         | - `"Aperture`" or `"aperture`"                                                   |
|                                         | - `"Blur Level`" or `"blurLevel`"                                                |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From a light layer                      | - `"Intensity`" or `"intensity`"                                                 |
|                                         | - `"Color`" or `"color`"                                                         |
|                                         | - `"Cone Angle`" or `"coneAngle`"                                                |
|                                         | - `"Cone Feather`" or `"coneFeather`"                                            |
|                                         | - `"Shadow Darkness`" or `"shadowDarkness`"                                      |
|                                         | - `"Shadow Diffusion`" or `"shadowDiffusion`"                                    |
|                                         | - `"Casts Shadows`" or `"castsShadows`"                                          |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From a 3D layer                         | - `"Accepts Shadows`" or `"acceptsShadows`"                                      |
|                                         | - `"Accepts Lights`" or `"acceptsLights`"                                        |
|                                         | - `"Ambient`" or `"ambient`"                                                     |
|                                         | - `"Diffuse`" or `"diffuse`"                                                     |
|                                         | - `"Specular`" or `"specular`" (these are for the Specular Intensity property)   |
|                                         | - `"Shininess`" or `"shininess`" (these are for the Specular Shininess property) |
|                                         | - `"Casts Shadows`" or `"castsShadows`"                                          |
|                                         | - `"Light Transmission`" or `"lightTransmission`"                                |
|                                         | - `"Metal`" or `"metal`"                                                         |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From a camera, light or 3D layer        | - `"X Rotation`" or `"xRotation`" or `"Rotation X`" or `"rotationX`"             |
|                                         | - `"Y Rotation`" or `"yRotation`" or `"Rotation Y`" or `"rotationY`"             |
|                                         | - `"Orientation`" or `"orientation`"                                             |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From a text layer                       | - `"Source Text`" or `"source Text`" or `"Text`" or `"text`"                     |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From PropertyGroup `"ADBE Mask Parade`" | - `"ADBE Mask Atom`"                                                             |
+-----------------------------------------+----------------------------------------------------------------------------------+
| From PropertyGroup `"ADBE Mask Atom`"   | - `"ADBE Mask Shape`", or `"maskShape`", or `"maskPath`"                         |
|                                         | - `"ADBE Mask Feather`", or `"maskFeather`"                                      |
|                                         | - `"ADBE Mask Opacity`", or `"maskOpacity`"                                      |
|                                         | - `"ADBE Mask Offset`", or `"maskOffset"`                                        |
+-----------------------------------------+----------------------------------------------------------------------------------+

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
