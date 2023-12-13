.. _ParagraphRange:

ParagraphRange object
################################################

|  ``app.project.item(index).layer(index).text.sourceText.value.paragraphRange(paragraphIndexStart, [signedParagraphIndexEnd])``

.. note::
   This functionality was added in After Effects (Beta) 24.2 and is subject to change while it remains in Beta.

**Description**

The ParagraphRange object is an accessor to a paragraph range of the :ref:`TextDocument` instance it was created from.

- The property ``characterStart`` will report the first character index of the range.
- The property ``characterEnd`` will report the (last + 1) character index of the range, such that (``characterEnd`` - ``characterStart``) represents the number of characters in the range.
- It is acceptable for most properties for the effective range to be zero - otherwise known as an insertion point.

Unlike the :ref:`TextDocument`, which looks at only the first character when returning character attributes, here the range can span zero or more characters.
As a consequence, two or more characters may not have the same attribute value and this mixed state will be signaled by returning ``undefined``.

When accessed, the ParagraphRange object will check that effective ``characterStart`` and effective ``characterEnd`` of the range remains valid for the current span of the related :ref:`TextDocument`. This is the same rule as applied when the ParagraphRange was created, but because the length of the related :ref:`TextDocument` can change through the addition or removal of characters, the effective ``characterStart`` and effective ``characterEnd`` may no longer be valid. In this situation an exception will be thrown on access, either read or write. The property ``isRangeValid`` will return false if the effective range is no longer valid.

Note that if the :ref:`TextDocument` length changes, the character range could become valid again.

**Differences from TextDocument**

Because ParagraphRange is an accessor of :ref:`TextDocument`, most methods and attributes of TextDocument are available when working with ParagraphRange. The attributes and methods that are unique to ParagraphRange or exhibit unique behaviors are included on this page.

The following attributes and methods are **not** available on instances of ParagraphRange:

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

This increases the font size of the first paragraph in the TextDocument, and set the rest of the paragraphs to fontSize 40.

.. code:: javascript

   var textDocument = app.project.item(index).layer(index).property("Source Text").value;
   var paragraphRange = textDocument.paragraphRange(0,1);

   paragraphRange.fontSize = paragraphRange.fontSize + 5;
   textDocument.paragraphRange(1,-1).fontSize = 40;

----

==========
Attributes
==========

.. _ParagraphRange.characterEnd:

ParagraphRange.characterEnd
*********************************************

``ParagraphRange.characterEnd``

**Description**

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _ParagraphRange.characterStart:

ParagraphRange.characterStart
*********************************************

``ParagraphRange.characterStart``

**Description**

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _ParagraphRange.fillColor:

ParagraphRange.fillColor
*********************************************

``ParagraphRange.fillColor``

**Description**

The Text layer range ParagraphRange attribute Fill Color, as an array of ``[r, g, b]`` floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

Setting this value will also set ``applyFill`` to true across the affected characters.

If this attribute has a mixed value for the range of characters, it will be read as ``undefined``.

.. warning::
   In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if ``applyFill`` is not true.

**Type**

Array ``[r, g, b]`` of floating-point values; read/write.

----

.. _ParagraphRange.isRangeValid:

ParagraphRange.isRangeValid
*********************************************

``ParagraphRange.isRangeValid``

**Description**

Returns true if the current range is within the bounds of the related :ref:`TextDocument`, false otherwise.

**Type**

Boolean; read-only.

----

.. _ParagraphRange.kerning:

ParagraphRange.kerning
*********************************************

``ParagraphRange.kerning``

**Description**

The Text layer range character attribute kerning option.

This effectively reports the manual kerning value, and not the calculated kerning value from auto kerning.

- If ``autoKernType`` in the range is set to ``AutoKernType.METRIC_KERN``, ``AutoKernType.OPTICAL_KERN``, or is mixed, then this property will be returned as ``undefined``.
- If ``autoKernType`` in the range is set to ``AutoKernType.NO_AUTO_KERN``, and this attribute has a mixed value, it will be read as ``undefined``.

Setting this value will also set ``AutoKernType.NO_AUTO_KERN`` to true across the affected characters.

**Type**

Integer value; read/write.

----

.. _ParagraphRange.strokeColor:

ParagraphRange.strokeColor
*********************************************

``ParagraphRange.strokeColor``

**Description**

The Text layer ParagraphRange Stroke Color character property, as an array of [r, g, b] floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

If this attribute has a mixed value, it will be read as ``undefined``.

Setting this value will also set ``applyStroke`` to true across the affected characters.

.. warning::
   In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if ``applyStroke`` is not true.

**Type**

Array [r, g, b] of floating-point values; read/write.

----

.. _ParagraphRange.strokeOverFill:

ParagraphRange.strokeOverFill
*********************************************

``ParagraphRange.strokeOverFill``

**Description**

The Text layer ParagraphRange Stroke Over Fill character property.

Indicates the rendering order for the fill and stroke for characters in the range. When true, the stroke appears over the fill.

If this attribute has a mixed value, it will be read as ``undefined``.

.. warning::
   | The Text layer can override per-character attribute setting via the All Strokes First or All Fills First setting on the CharPanel.
   | The value returned here represents what is applied to the characters, without regard to the possible Text layer override.

**Type**

Boolean; read/write.

----

.. _ParagraphRange.text:

ParagraphRange.text
*********************************************

``ParagraphRange.text``

**Description**

The text value for the Text layer ParagraphRange.

On read, the same number of characters as the span of the range will be returned. If the span is zero (an insertion point) it return an empty string.

On write, the characters in the range will be replaced with whatever string value is supplied. If an empty string, then the characters in the range will be effectively deleted.

**Type**

String; read/write.

----

=======
Methods
=======

.. _ParagraphRange.toString:

ParagraphRange.toString()
*********************************************

``ParagraphRange.toString()``

**Description**

Returns a string with the parameters used to create the `ParagraphRange` instance, e.g. ``"ParagraphRange(0,-1)"``

This may be safely called on an instance where `isRangeValid` returns false.

**Parameters**

None.

**Returns**

String;
