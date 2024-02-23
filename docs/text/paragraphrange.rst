.. _ParagraphRange:

ParagraphRange object
################################################

|  ``app.project.item(index).layer(index).text.sourceText.value.paragraphRange(paragraphIndexStart, [signedParagraphIndexEnd])``

.. note::
   This functionality was added in After Effects (Beta) 24.2 and is subject to change while it remains in Beta.

**Description**

The ParagraphRange object is an accessor to a paragraph range of the :ref:`TextDocument` instance it was created from.

- The :ref:`characterStart<ParagraphRange.characterStart>` attribute will report the first character index of the range.
- The :ref:`characterEnd<ParagraphRange.characterEnd>` attribute will report the (last + 1) character index of the range, such that (:ref:`characterEnd<ParagraphRange.characterEnd>` - :ref:`characterStart<ParagraphRange.characterStart>`) represents the number of characters in the range.
- The only time these two properties will equal will on an empty last paragraph of the :ref:`TextDocument`.

When accessed, the ParagraphRange object will check that effective :ref:`characterStart<ParagraphRange.characterStart>` and effective :ref:`characterEnd<ParagraphRange.characterEnd>` of the range remains valid for the current span of the related :ref:`TextDocument`. This is the same rule as applied when the ParagraphRange was created, but because the length of the related :ref:`TextDocument` can change through the addition or removal of characters, the effective :ref:`characterStart<ParagraphRange.characterStart>` and effective :ref:`characterEnd<ParagraphRange.characterEnd>` may no longer be valid. In this situation an exception will be thrown on access, either read or write. The :ref:`isRangeValid<ParagraphRange.isRangeValid>` attribute will return false if the effective range is no longer valid.

Note that if the :ref:`TextDocument` length changes, the character range could become valid again.

As a convenience, the function :ref:`ParagraphRange.characterRange` can be invoked which will return a :ref:`CharacterRange` instance initialized from :ref:`characterStart<ParagraphRange.characterStart>` and :ref:`characterEnd<ParagraphRange.characterEnd>`.
This instance becomes independent of the ParagraphRange instance it came from so subsequent changes to the ParagraphRange limits are not communicated to the :ref:`CharacterRange` instance.

For performance reasons, when accessing multiple attributes it is adviseable to retrieve the :ref:`CharacterRange` once and re-use it rather than create a new one each time.

**Examples**

This increases the font size of the first paragraph in the TextDocument, and set the rest of the paragraphs to fontSize 40.

.. code:: javascript

   var textDocument = app.project.item(index).layer(index).property("Source Text").value;

   var paragraphRange0 = textDocument.paragraphRange(0,1);
   var characterRange0 = paragraphRange0.characterRange();
   characterRange0.fontSize = characterRange0.fontSize + 5;

   textDocument.paragraphRange(1,-1).characterRange().fontSize = 40;

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

.. _ParagraphRange.isRangeValid:

ParagraphRange.isRangeValid
*********************************************

``ParagraphRange.isRangeValid``

**Description**

Returns true if the current range is within the bounds of the related :ref:`TextDocument`, false otherwise.

**Type**

Boolean; read-only.

----

=======
Methods
=======

.. _ParagraphRange.characterRange:

ParagraphRange.characterRange()
*********************************************

``ParagraphRange.characterRange()``

**Description**

Returns a :ref:`CharacterRange` initialized from :ref:`characterStart<ParagraphRange.characterStart>` and :ref:`characterEnd<ParagraphRange.characterEnd>`.

Will throw an exception if :ref:`isRangeValid<ParagraphRange.isRangeValid>` would return false.

The returned instance, once created, is independent of subsequent changes to the ParagraphRange it came from.

**Parameters**

None.

**Returns**

:ref:`CharacterRange`;

----

.. _ParagraphRange.toString:

ParagraphRange.toString()
*********************************************

``ParagraphRange.toString()``

**Description**

Returns a string with the parameters used to create the `ParagraphRange` instance, e.g. ``"ParagraphRange(0,-1)"``

This may be safely called on an instance where :ref:`isRangeValid<ParagraphRange.isRangeValid>` returns false.

**Parameters**

None.

**Returns**

String;
