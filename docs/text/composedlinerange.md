# ComposedLineRange object

`app.project.item(index).layer(index).text.sourceText.value.composedLineRange(composedLineIndexStart, [signedComposedLineIndexEnd])`

!!! note
    This functionality was added in After Effects 24.3

#### Description

The ComposedLineRange object is an accessor to a composed line range of the [TextDocument object](textdocument.md) instance it was created from.

Composed lines are initialized in the [TextDocument object](textdocument.md) when it is created and remain unchanged while the [TextDocument object](textdocument.md) is changed.
It is important to note that the [TextDocument object](textdocument.md) instance is not recomposed when changes are made to it - that only occurs when the instance is applied back to a [TextLayer object](../layer/textlayer.md).
So if you delete all the text in the [TextDocument object](textdocument.md) instance the number of composed lines will remain constant.

- The [characterStart](#composedlinerangecharacterstart) attribute will report the first character index of the range.
- The [characterEnd](#composedlinerangecharacterend) attribute will report the (last + 1) character index of the range, such that ([characterEnd](#composedlinerangecharacterend) - [characterStart](#composedlinerangecharacterstart)) represents the number of characters in the range.
- A composed line always has some length.

When accessed, the ComposedLineRange object will check that effective [characterStart](#composedlinerangecharacterstart) and effective [characterEnd](#composedlinerangecharacterend) of the range remains valid for the current span of the related [TextDocument object](textdocument.md). This is the same rule as applied when the ComposedLineRange was created, but because the length of the related [TextDocument object](textdocument.md) can change through the addition or removal of characters, the effective [characterStart](#composedlinerangecharacterstart) and effective [characterEnd](#composedlinerangecharacterend) may no longer be valid. In this situation an exception will be thrown on access, either read or write. The property [isRangeValid](#composedlinerangeisrangevalid) will return `false` if the effective range is no longer valid.

Note that if the [TextDocument object](textdocument.md) length changes, the character range could become valid again.

As a convenience, the function [ComposedLineRange.characterRange()](#composedlinerangecharacterrange) can be invoked which will return a [CharacterRange object](characterrange.md) instance initialized from [characterStart](#composedlinerangecharacterstart) and [characterEnd](#composedlinerangecharacterend).
This instance becomes independent of the ComposedLineRange instance it came from so subsequent changes to the ComposedLineRange limits are not communicated to the [CharacterRange object](characterrange.md) instance.

For performance reasons, when accessing multiple attributes it is adviseable to retrieve the [CharacterRange object](characterrange.md) once and re-use it rather than create a new one each time.

#### Examples

This changes the fill color to red of the first composed line in the TextDocument, and set the rest of the lines to color blue.

```javascript
var textDocument = app.project.item(index).layer(index).property("Source Text").value;

var composedLineRange0 = textDocument.composedLineRange(0,1);
var characterRange0 = composedLineRange0.characterRange();
characterRange0.fillColor = [1.0, 0, 0];

textDocument.composedLineRange(1,-1).characterRange().fillColor = [0, 0, 1.0];
```

---

## Attributes

### ComposedLineRange.characterEnd

`ComposedLineRange.characterEnd`

#### Description

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md).

#### Type

Unsigned integer; read-only.

---

### ComposedLineRange.characterStart

`ComposedLineRange.characterStart`

#### Description

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md).

#### Type

Unsigned integer; read-only.

---

### ComposedLineRange.isRangeValid

`ComposedLineRange.isRangeValid`

#### Description

Returns `true` if the current range is within the bounds of the related [TextDocument object](textdocument.md), otherwise `false`.

#### Type

Boolean; read-only.

---

## Methods

### ComposedLineRange.characterRange()

`ComposedLineRange.characterRange()`

#### Description

Returns a [CharacterRange object](characterrange.md) initialized from [characterStart](#composedlinerangecharacterstart) and [characterEnd](#composedlinerangecharacterend).

Will throw an exception if isRangeValid would return `false`.

The returned instance, once created, is independent of subsequent changes to the ComposedLineRange it came from.

#### Parameters

None.

#### Returns

[CharacterRange object](characterrange.md);

---

### ComposedLineRange.toString()

`ComposedLineRange.toString()`

#### Description

Returns a string with the parameters used to create the ComposedLineRange instance, e.g. `"ComposedLineRange(0,-1)"`

This may be safely called on an instance where isRangeValid returns `false`.

#### Parameters

None.

#### Returns

String;
