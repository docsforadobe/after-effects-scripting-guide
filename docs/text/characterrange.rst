.. _CharacterRange:

CharacterRange object
################################################

|  ``app.project.item(index).layer(index).text.sourceText.value.characterRange(characterIndexStart, [signedCharacterIndexEnd])``

.. note::
   This functionality was added in After Effects (Beta) 24.2 and is subject to change while it remains in Beta.

**Description**

The CharacterRange object is an accessor to a character range of the :ref:`TextDocument` instance it was created from.

Unlike the :ref:`TextDocument`, which looks at only the first character when returning character attributes, here the character range can span zero or more characters. As a consequence, two or more characters *may not have the same attribute value* and this mixed state will be signaled by returning ``undefined``.

- The :ref:`characterStart<CharacterRange.characterStart>` attribute is the first character index of the range.
- The :ref:`characterEnd<CharacterRange.characterEnd>` attribue will report the (last + 1) character index of the range, such that (:ref:`characterEnd<CharacterRange.characterEnd>` - :ref:`characterStart<CharacterRange.characterStart>`) represents the number of characters in the range.

It is acceptable for most attributes for the effective range to be zero - otherwise known as an insertion point.

When accessed, the CharacterRange object will check that :ref:`characterStart<CharacterRange.characterStart>` and effective :ref:`characterEnd<CharacterRange.characterEnd>` of the range remains valid for the current span of the related :ref:`TextDocument`. This is the same rule as applied when the CharacterRange was created, but because the length of the related :ref:`TextDocument` can change through the addition or removal of characters, the :ref:`characterStart<CharacterRange.characterStart>` and effective :ref:`characterEnd<CharacterRange.characterEnd>` may no longer be valid. In this situation an exception will be thrown on access, either read or write. The :ref:`isRangeValid<CharacterRange.isRangeValid>` attribute will return false if the effective range is no longer valid.

Note that if the :ref:`TextDocument` length changes, the :ref:`CharacterRange` range could become valid again.

**Differences from TextDocument**

Because CharacterRange is an accessor of :ref:`TextDocument`, most methods and attributes of TextDocument are available when working with CharacterRange. The attributes and methods that are unique to CharacterRange or exhibit unique behaviors are included on this page.

The following attributes and methods are **not** available on instances of CharacterRange:

 =================================== ============================= 
  Attributes                          Methods                      
 =================================== ============================= 
  `baselineLocs`                     `characterRange`              
  `boxText`                          `paragraphCharacterIndexesAt` 
  `boxTextPos`                       `paragraphRange`              
  `boxTextSize`                                                    
  `lineOrientation`                                                
  `paragraphCount`                                                 
  `pointText`                                                      
 =================================== ============================= 



**Examples**

This increases the font size of the first character in the TextDocument, and set the rest of the characters to fontSize 40.

.. code:: javascript

   var textDocument = app.project.item(index).layer(index).property("Source Text").value;
   var characterRange = textDocument.characterRange(0,1);

   characterRange.fontSize = characterRange.fontSize + 5;
   textDocument.characterRange(1,-1).fontSize = 40;

----

==========
Attributes
==========

.. _CharacterRange.characterEnd:

CharacterRange.characterEnd
*********************************************

``CharacterRange.characterEnd``

**Description**

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _CharacterRange.characterStart:

CharacterRange.characterStart
*********************************************

``CharacterRange.characterStart``

**Description**

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _CharacterRange.fillColor:

CharacterRange.fillColor
*********************************************

``CharacterRange.fillColor``

**Description**

The Text layer range CharacterRange attribute Fill Color, as an array of ``[r, g, b]`` floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

Setting this value will also set ``applyFill`` to true across the affected characters.

If this attribute has a mixed value for the range of characters, it will be read as ``undefined``.

.. warning::
   In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if ``applyFill`` is not true.

**Type**

Array ``[r, g, b]`` of floating-point values; read/write.

----

.. _CharacterRange.isRangeValid:

CharacterRange.isRangeValid
*********************************************

``CharacterRange.isRangeValid``

**Description**

Returns true if the current range is within the bounds of the related :ref:`TextDocument`, false otherwise.

**Type**

Boolean; read-only.

----

.. _CharacterRange.kerning:

CharacterRange.kerning
*********************************************

``CharacterRange.kerning``

**Description**

The Text layer range character attribute kerning option.

This effectively reports the manual kerning value, and not the calculated kerning value from auto kerning.

- If :ref:`autoKernType<TextDocument.autoKernType>` in the range is set to ``AutoKernType.METRIC_KERN``, ``AutoKernType.OPTICAL_KERN``, or is mixed, then this attribute will be returned as ``undefined``.
- If :ref:`autoKernType<TextDocument.autoKernType>` in the range is set to ``AutoKernType.NO_AUTO_KERN``, and this attribute has a mixed value, it will be read as ``undefined``.

Setting this value will also set ``AutoKernType.NO_AUTO_KERN`` to true across the affected characters.

**Type**

Integer value; read/write.

----

.. _CharacterRange.strokeColor:

CharacterRange.strokeColor
*********************************************

``CharacterRange.strokeColor``

**Description**

The Text layer CharacterRange stroke color character property, as an array of [r, g, b] floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

If this attribute has a mixed value, it will be read as ``undefined``.

Setting this value will also set :ref:`applyStroke<TextDocument.applyStroke>` to true across the affected characters.

.. warning::
   In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if :ref:`applyStroke<TextDocument.applyStroke>` is not true.

**Type**

Array [r, g, b] of floating-point values; read/write.

----

.. _CharacterRange.strokeOverFill:

CharacterRange.strokeOverFill
*********************************************

``CharacterRange.strokeOverFill``

**Description**

The Text layer CharacterRange Stroke Over Fill character property.

Indicates the rendering order for the fill and stroke for characters in the range. When true, the stroke appears over the fill.

If this attribute has a mixed value, it will be read as ``undefined``.

.. warning::
   | The Text layer can override per-character attribute setting via the All Strokes First or All Fills First setting on the CharPanel.
   | The value returned here represents what is applied to the characters, without regard to the possible Text layer override.

**Type**

Boolean; read/write.

----

.. _CharacterRange.text:

CharacterRange.text
*********************************************

``CharacterRange.text``

**Description**

The text value for the Text layer range.

On read, the same number of characters as the span of the range will be returned. If the span is zero (an insertion point) it return an empty string.

On write, the characters in the range will be replaced with whatever string value is supplied. If an empty string, then the characters in the range will be effectively deleted.

To insert characters without deleting any existing, call :ref:`TextDocument.characterRange` with the same value for start as end to get an insertion point range.

**Type**

String; read/write.

----

=======
Methods
=======

.. _CharacterRange.toString:

CharacterRange.toString()
*********************************************

``CharacterRange.toString()``

**Description**

Returns a string with the parameters used to create the `CharacterRange` instance, e.g. ``"CharacterRange(0,-1)"``.

This may be safely called on an instance where `isRangeValid` returns false.

**Parameters**

None.

**Returns**

String;
