# ParagraphRange object

`app.project.item(index).layer(index).text.sourceText.value.paragraphRange(paragraphIndexStart, [signedParagraphIndexEnd])`
<br/>

?> **Note:** This functionality was added in After Effects 24.3

**Description**

The ParagraphRange object is an accessor to a paragraph range of the [TextDocument object](textdocument.md#textdocument) instance it was created from.

- The [characterStart](#paragraphrange-characterstart) attribute will report the first character index of the range.
- The [characterEnd](#paragraphrange-characterend) attribute will report the (last + 1) character index of the range, such that ([characterEnd](#paragraphrange-characterend) - [characterStart](#paragraphrange-characterstart)) represents the number of characters in the range.
- The only time these two properties will equal will on an empty last paragraph of the [TextDocument object](textdocument.md#textdocument).

When accessed, the ParagraphRange object will check that effective [characterStart](#paragraphrange-characterstart) and effective [characterEnd](#paragraphrange-characterend) of the range remains valid for the current span of the related [TextDocument object](textdocument.md#textdocument). This is the same rule as applied when the ParagraphRange was created, but because the length of the related [TextDocument object](textdocument.md#textdocument) can change through the addition or removal of characters, the effective [characterStart](#paragraphrange-characterstart) and effective [characterEnd](#paragraphrange-characterend) may no longer be valid. In this situation an exception will be thrown on access, either read or write. The [isRangeValid](#paragraphrange-israngevalid) attribute will return false if the effective range is no longer valid.

Note that if the [TextDocument object](textdocument.md#textdocument) length changes, the character range could become valid again.

As a convenience, the function [ParagraphRange.characterRange()](#paragraphrange-characterrange) can be invoked which will return a [CharacterRange object](characterrange.md#characterrange) instance initialized from [characterStart](#paragraphrange-characterstart) and [characterEnd](#paragraphrange-characterend).
This instance becomes independent of the ParagraphRange instance it came from so subsequent changes to the ParagraphRange limits are not communicated to the [CharacterRange object](characterrange.md#characterrange) instance.

For performance reasons, when accessing multiple attributes it is adviseable to retrieve the [CharacterRange object](characterrange.md#characterrange) once and re-use it rather than create a new one each time.

**Examples**

This increases the font size of the first paragraph in the TextDocument, and set the rest of the paragraphs to fontSize 40.

```javascript
var textDocument = app.project.item(index).layer(index).property("Source Text").value;

var paragraphRange0 = textDocument.paragraphRange(0,1);
var characterRange0 = paragraphRange0.characterRange();
characterRange0.fontSize = characterRange0.fontSize + 5;

textDocument.paragraphRange(1,-1).characterRange().fontSize = 40;
```

---

## Attributes

### ParagraphRange.characterEnd

`ParagraphRange.characterEnd`

**Description**

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md#textdocument).

**Type**

Unsigned integer; read-only.

---

### ParagraphRange.characterStart

`ParagraphRange.characterStart`

**Description**

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md#textdocument).

**Type**

Unsigned integer; read-only.

---

### ParagraphRange.isRangeValid

`ParagraphRange.isRangeValid`

**Description**

Returns true if the current range is within the bounds of the related [TextDocument object](textdocument.md#textdocument), false otherwise.

**Type**

Boolean; read-only.

---

## Methods

### ParagraphRange.characterRange()

`ParagraphRange.characterRange()`

**Description**

Returns a [CharacterRange object](characterrange.md#characterrange) initialized from [characterStart](#paragraphrange-characterstart) and [characterEnd](#paragraphrange-characterend).

Will throw an exception if [isRangeValid](#paragraphrange-israngevalid) would return false.

The returned instance, once created, is independent of subsequent changes to the ParagraphRange it came from.

**Parameters**

None.

**Returns**

[CharacterRange object](characterrange.md#characterrange);

---

### ParagraphRange.toString()

`ParagraphRange.toString()`

**Description**

Returns a string with the parameters used to create the ParagraphRange instance, e.g. `"ParagraphRange(0,-1)"`

This may be safely called on an instance where [isRangeValid](#paragraphrange-israngevalid) returns false.

**Parameters**

None.

**Returns**

String;
