.. _ComposedLineRange:

ComposedLineRange object
################################################

|  ``app.project.item(index).layer(index).text.sourceText.value.composedLineRange(composedLineIndexStart, [signedComposedLineIndexEnd])``

.. note::
   This functionality was added in After Effects (Beta) 24.3 and is subject to change while it remains in Beta.

**Description**

The `ComposedLineRange` object is an accessor to a composed line range of the :ref:`TextDocument` instance it was created from.

Composed lines are initialized in the :ref:`TextDocument` when it is created and remain unchanged while the :ref:`TextDocument` is changed.
It is important to note that the :ref:`TextDocument` instance is not re-composed when changes are made to it - that only occurs when the instance is applied back to a :ref:`TextLayer`.
So if you delete all the text in the :ref:`TextDocument` instance the number of composed lines will remain constant.

- The :ref:`characterStart<ComposedLineRange.characterStart>` attribute will report the first character index of the range.
- The :ref:`characterEnd<ComposedLineRange.characterEnd>` attribute will report the (last + 1) character index of the range, such that (:ref:`characterEnd<ComposedLineRange.characterEnd>` - :ref:`characterStart<ComposedLineRange.characterStart>`) represents the number of characters in the range.
- A composed line always has some length.

When accessed, the `ComposedLineRange` object will check that effective :ref:`characterStart<ComposedLineRange.characterStart>` and effective :ref:`characterEnd<ComposedLineRange.characterEnd>` of the range remains valid for the current span of the related :ref:`TextDocument`. This is the same rule as applied when the `ComposedLineRange` was created, but because the length of the related :ref:`TextDocument` can change through the addition or removal of characters, the effective :ref:`characterStart<ComposedLineRange.characterStart>` and effective :ref:`characterEnd<ComposedLineRange.characterEnd>` may no longer be valid. In this situation an exception will be thrown on access, either read or write. The property :ref:`isRangeValid<ComposedLineRange.isRangeValid>` will return false if the effective range is no longer valid.

Note that if the :ref:`TextDocument` length changes, the character range could become valid again.

As a convenience, the function :ref:`ComposedLineRange.characterRange` can be invoked which will return a :ref:`CharacterRange` instance initialized from :ref:`characterStart<ComposedLineRange.characterStart>` and :ref:`characterEnd<ComposedLineRange.characterEnd>`.
This instance becomes independent of the `ComposedLineRange` instance it came from so subsequent changes to the `ComposedLineRange` limits are not communicated to the :ref:`CharacterRange` instance.

For performance reasons, when accessing multiple attributes it is adviseable to retrieve the :ref:`CharacterRange` once and re-use it rather than create a new one each time.

**Examples**

This changes the fill color to red of the first composed line in the TextDocument, and set the rest of the lines to color blue.

.. code:: javascript

   var textDocument = app.project.item(index).layer(index).property("Source Text").value;

   var composedLineRange0 = textDocument.composedLineRange(0,1);
   var characterRange0 = composedLineRange0.characterRange();
   characterRange0.fillColor = [1.0, 0, 0];

   textDocument.composedLineRange(1,-1).characterRange().fillColor = [0, 0, 1.0];

----

==========
Attributes
==========

.. _ComposedLineRange.characterEnd:

ComposedLineRange.characterEnd
*********************************************

``ComposedLineRange.characterEnd``

**Description**

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _ComposedLineRange.characterStart:

ComposedLineRange.characterStart
*********************************************

``ComposedLineRange.characterStart``

**Description**

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related :ref:`TextDocument`.

**Type**

Unsigned integer; read-only.

----

.. _ComposedLineRange.isRangeValid:

ComposedLineRange.isRangeValid
*********************************************

``ComposedLineRange.isRangeValid``

**Description**

Returns true if the current range is within the bounds of the related :ref:`TextDocument`, false otherwise.

**Type**

Boolean; read-only.

----

=======
Methods
=======

.. _ComposedLineRange.characterRange:

ComposedLineRange.characterRange()
*********************************************

``ComposedLineRange.characterRange()``

**Description**

Returns a :ref:`CharacterRange` initialized from :ref:`characterStart<ComposedLineRange.characterStart>` and :ref:`characterEnd<ComposedLineRange.characterEnd>`.


Will throw an exception if `isRangeValid` would return false.

The returned instance, once created, is independent of subsequent changes to the `ComposedLineRange` it came from.

**Parameters**

None.

**Returns**

:ref:`CharacterRange`;

----

.. _ComposedLineRange.toString:

ComposedLineRange.toString()
*********************************************

``ComposedLineRange.toString()``

**Description**

Returns a string with the parameters used to create the `ComposedLineRange` instance, e.g. ``"ComposedLineRange(0,-1)"``

This may be safely called on an instance where `isRangeValid` returns false.

**Parameters**

None.

**Returns**

String;
