.. _MaskPropertyGroup:

MaskPropertyGroup object
########################

``app.project.item(index).layer(index).mask``

**Description**

The MaskPropertyGroup object encapsulates mask attributes in a layer.

    MaskPropertyGroup is a subclass of :ref:`PropertyGroup`. All methods and attributes of :ref:`PropertyBase` and PropertyGroup, in addition to those listed below, are available when working with MaskPropertyGroup.

----

==========
Attributes
==========

.. _MaskPropertyGroup.color:

MaskPropertyGroup.color
*********************************************

``app.project.item(index).layer(index).mask(index).color``

**Description**

The color used to draw the mask outline as it appears in the user interface (Composition panel, Layer panel, and Timeline panel).

**Type**

Array of three floating-point values, [R, G, B], in the range ``[0.0..1.0]``; read/write.

----

.. _MaskPropertyGroup.inverted:

MaskPropertyGroup.inverted
*********************************************

``app.project.item(index).layer(index).mask(index).inverted``

**Description**

When true, the mask is inverted; otherwise false.

**Type**

Boolean; read/write.

----

.. _MaskPropertyGroup.locked:

MaskPropertyGroup.locked
*********************************************

``app.project.item(index).layer(index).mask(index).locked``

**Description**

When true, the mask is locked and cannot be edited in the user interface; otherwise, false.

**Type**

Boolean; read/write.

----

.. _MaskPropertyGroup.maskFeatherFalloff:

MaskPropertyGroup.maskFeatherFalloff
*********************************************

``app.project.item(index).layer(index).mask(index).maskFeatherFalloff``

**Description**

The feather falloff mode for the mask. Equivalent to the Layer > Mask > Feather Falloff setting.

**Type**

A ``MaskFeatherFalloff`` enumerated value; read/write. One of:

-  ``MaskFeatherFalloff.FFO_LINEAR``
-  ``MaskFeatherFalloff.FFO_SMOOTH``

----

.. _MaskPropertyGroup.maskMode:

MaskPropertyGroup.maskMode
*********************************************

``app.project.item(index).layer(index).mask(index).maskMode``

**Description**

The masking mode for this mask.

**Type**

A ``MaskMode`` enumerated value; read/write. One of:

-  ``MaskMode.NONE``
-  ``MaskMode.ADD``
-  ``MaskMode.SUBTRACT``
-  ``MaskMode.INTERSECT``
-  ``MaskMode.LIGHTEN``
-  ``MaskMode.DARKEN``
-  ``MaskMode.DIFFERENCE``

----

.. _MaskPropertyGroup.maskMotionBlur:

MaskPropertyGroup.maskMotionBlur
*********************************************

``app.project.item(index).layer(index).mask(index).maskMotionBlur``

**Description**

How motion blur is applied to this mask.

**Type**

A ``MakMotionBlur`` enumerated value; read/write. One of:

-  ``MaskMotionBlur.SAME_AS_LAYER``
-  ``MaskMotionBlur.ON``
-  ``MaskMotionBlur.OFF``

----

.. _MaskPropertyGroup.rotoBezier:

MaskPropertyGroup.rotoBezier
*********************************************

``app.project.item(index).layer(index).mask(index).rotoBezier``

**Description**

When true, the mask is a RotoBezier shape; otherwise, false.

**Type**

Boolean; read/write.
