# PropertyGroup object

`app.project.item(index).layer(index).propertyGroupSpec`

#### Description

The PropertyGroup object represents a group of properties. It can contain Property objects and other PropertyGroup objects. Property groups can be nested to provide a parent-child hierarchy, with a Layer object at the top (root) down to a single Property object, such as the mask feather of the third mask. To traverse the group hierarchy, use PropertyBase methods and attributes; see [PropertyBase.propertyGroup()](propertybase.md#propertybasepropertygroup). For examples of how to access properties and property groups, see [PropertyBase object](propertybase.md#propertybase).

> PropertyGroup is a subclass of [PropertyBase](propertybase.md#propertybase). All methods and attributes of PropertyBase, in addition to those listed below, are available when working with PropertyGroup.

> PropertyGroup is a base class for [Layer](../layers/layer.md#layer) and [MaskPropertyGroup](maskpropertygroup.md#maskpropertygroup). PropertyGroup attributes and methods are available when working with layer or mask groups.

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

!> **Warning:** When you add a new property to an indexed group, the indexed group gets recreated from scratch, invalidating all existing references to properties.

One workaround is to store the index of the added property with property.propertyIndex.

#### Examples

- This won't work, as the slider object becomes invalid once we add the Color Control property:
  > ```javascript
  > var effectsProperty = layer.property("ADBE Effect Parade");
  > var slider = effectsProperty.addProperty("ADBE Slider Control");
  > var color = effectsProperty.addProperty("ADBE Color Control");

  > var sliderProperty = slider.property("ADBE Slider Control-0001"); // Object 'slider' is Invalid
  > ```
- This revised method will work:
  > ```javascript
  > var effectsProperty = layer.property("ADBE Effect Parade");
  > var slider = effectsProperty.addProperty("ADBE Slider Control");
  > var sliderIndex = slider.propertyIndex; // Store 'slider' effect index so it can be reused later
  > var color = effectsProperty.addProperty("ADBE Color Control");

  > var sliderProperty = effectsProperty.property(sliderIndex).property("ADBE Slider Control-0001");
  > ```

#### Parameters

| `name`   | The display name or match name of the property to add. (See<br/>[PropertyBase.matchName](propertybase.md#propertybasematchname)). The following names are supported:<br/><br/>- Any match name for a property that can be added through the user<br/>  interface. For example, "ADBE Mask Atom", "ADBE Paint Atom", "ADBE<br/>  Text Position", "ADBE Text Anchor Point".<br/>- When adding to an ADBE Mask Parade: "ADBE Mask Atom", "Mask".<br/>- When adding to an ADBE Effect Parade, any effect by match name,<br/>  such as "ADBE Bulge", "ADBE Glo2", "APC Vegas".<br/>- Any effect by display name, such as "Bulge", "Glow", "Vegas".<br/>- For text animators, "ADBE Text Animator".<br/>- For selectors, Range Selector has the name "ADBE Text Selector",<br/>  Wiggly Selector has the name "ADBE Text Wiggly Selector", and<br/>  Expression Selector has the name "ADBE Text Expressible Selector".   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Returns

[PropertyBase object](propertybase.md#propertybase).

---

### PropertyGroup.canAddProperty()

`app.project.item(index).layer(index).propertyGroupSpec.canAddProperty(name)`

#### Description

Returns true if a property with the given name can be added to this property group.

For example, you can only add mask to a mask group. The only legal input arguments are "mask" or "ADBE Mask Atom".

```javascript
maskGroup.canAddProperty("mask"); // returns true
maskGroup.canAddProperty("ADBE Mask Atom"); // returns true
maskGroup.canAddProperty("blend"); // returns false
```

#### Parameters

| `name`   | The display name or match name of the property to be checked. (See<br/>[PropertyGroup.addProperty()](#propertygroupaddproperty).   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|

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

| `index`   | The index for the child property, in this is an indexed group. An<br/>integer in the range [1..numProperties].                                                                                                                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`    | The name of the child property. This can be:<br/><br/>- Any match name<br/>- Any name in expression "parenthesis style" syntax, meaning the<br/>  display name or the compact English name<br/>- Any name in expression "intercap style" syntax<br/><br/>For supported property names, see the table below. |

#### Returns

[PropertyBase object](propertybase.md#propertybase) or `null` if no child property with the specified string name is found.

#### Properties accessible by name

| From any Layer                          | - "ADBE Mask Parade", or "Masks"<br/>- "ADBE Effect Parade", or "Effects"<br/>- "ADBE MTrackers", or "Motion<br/>  Trackers"                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From an AVLayer                         | - "Anchor Point" or "anchorPoint"<br/>- "Position" or "position"<br/>- "Scale" or "scale"<br/>- "Rotation" or "rotation"<br/>- "Z Rotation" or "zRotation" or<br/>  "Rotation Z" or "rotationZ"<br/>- "Opacity" or "opacity"<br/>- "Marker" or "marker"                                                                                                                                                                                                            |
| From an AVLayer with a non-still source | - "Time Remap" or "timeRemapEnabled"                                                                                                                                                                                                                                                                                                                                                                                                                               |
| From an AVLayer with an audio component | - "Audio Levels" or "audioLevels"                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| From a camera layer                     | - "Zoom" or "zoom"<br/>- "Depth of Field" or "depthOfField"<br/>- "Focus Distance" or "focusDistance"<br/>- "Aperture" or "aperture"<br/>- "Blur Level" or "blurLevel"                                                                                                                                                                                                                                                                                             |
| From a light layer                      | - "Intensity" or "intensity"<br/>- "Color" or "color"<br/>- "Cone Angle" or "coneAngle"<br/>- "Cone Feather" or "coneFeather"<br/>- "Shadow Darkness" or<br/>  "shadowDarkness"<br/>- "Shadow Diffusion" or<br/>  "shadowDiffusion"<br/>- "Casts Shadows" or "castsShadows"                                                                                                                                                                                        |
| From a 3D layer                         | - "Accepts Shadows" or<br/>  "acceptsShadows"<br/>- "Accepts Lights" or "acceptsLights"<br/>- "Ambient" or "ambient"<br/>- "Diffuse" or "diffuse"<br/>- "Specular" or "specular" (these are<br/>  for the Specular Intensity<br/>  property)<br/>- "Shininess" or "shininess" (these<br/>  are for the Specular Shininess<br/>  property)<br/>- "Casts Shadows" or "castsShadows"<br/>- "Light Transmission" or<br/>  "lightTransmission"<br/>- "Metal" or "metal" |
| From a camera, light or 3D layer        | - "X Rotation" or "xRotation" or<br/>  "Rotation X" or "rotationX"<br/>- "Y Rotation" or "yRotation" or<br/>  "Rotation Y" or "rotationY"<br/>- "Orientation" or "orientation"                                                                                                                                                                                                                                                                                     |
| From a text layer                       | - "Source Text" or "source Text" or<br/>  "Text" or "text"                                                                                                                                                                                                                                                                                                                                                                                                         |
| From a PropertyGroup "ADBE Mask Parade" | - "ADBE Mask Atom"                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| From a PropertyGroup "ADBE Mask Atom"   | - "ADBE Mask Shape", or "maskShape",<br/>  or "maskPath"<br/>- "ADBE Mask Feather", or<br/>  "maskFeather"<br/>- "ADBE Mask Opacity", or<br/>  "maskOpacity"<br/>- "ADBE Mask Offset", or "maskOffset"                                                                                                                                                                                                                                                             |

#### Examples

1. If a layer named "myLayer" has a Box Blur effect, you can retrieve the effect in any of the following ways:
   > ```javascript
   > myLayer.property("Effects").property("Box Blur");
   > myLayer.property("Effects").property("boxBlur");
   > myLayer.property("Effects").property("ADBE Box Blur");
   > ```
2. If a layer named "myLayer" has a mask named "Mask 1" you can retrieve it as follows:
   > ```javascript
   > myLayer.property("Masks").property("Mask1");
   > ```
3. To get a Bulge Center value from a Bulge effect, you can use either of the following:
   > ```javascript
   > myLayer.property("Effects").property("Bulge").property("Bulge Center");
   > myLayer.property("Effects").property("Bulge").property("bulgeCenter");
   > ```
