# CharacterRange object

`app.project.item(index).layer(index).text.sourceText.value.characterRange(characterIndexStart, [signedCharacterIndexEnd])`
<br/>

#### NOTE
This functionality was added in After Effects 24.3

**Description**

The CharacterRange object is an accessor to a character range of the [TextDocument object](textdocument.md#textdocument) instance it was created from.

Unlike the [TextDocument object](textdocument.md#textdocument), which looks at only the first character when returning character attributes, here the character range can span zero or more characters. As a consequence, two or more characters *may not have the same attribute value* and this mixed state will be signaled by returning `undefined`.

- The [characterStart](#characterrange-characterstart) attribute is the first character index of the range.
- The [characterEnd](#characterrange-characterend) attribue will report the (last + 1) character index of the range, such that ([characterEnd](#characterrange-characterend) - [characterStart](#characterrange-characterstart)) represents the number of characters in the range.

It is acceptable for most attributes for the effective range to be zero - otherwise known as an insertion point.

When accessed, the CharacterRange object will check that [characterStart](#characterrange-characterstart) and effective [characterEnd](#characterrange-characterend) of the range remains valid for the current span of the related [TextDocument object](textdocument.md#textdocument). This is the same rule as applied when the CharacterRange was created, but because the length of the related [TextDocument object](textdocument.md#textdocument) can change through the addition or removal of characters, the [characterStart](#characterrange-characterstart) and effective [characterEnd](#characterrange-characterend) may no longer be valid. In this situation an exception will be thrown on access, either read or write. The [isRangeValid](#characterrange-israngevalid) attribute will return false if the effective range is no longer valid.

Note that if the [TextDocument object](textdocument.md#textdocument) length changes, the [CharacterRange object](#characterrange) range could become valid again.

**Differences from TextDocument**

Because CharacterRange is an accessor of [TextDocument object](textdocument.md#textdocument), most methods and attributes of TextDocument are available when working with CharacterRange. The attributes and methods that are unique to CharacterRange or exhibit unique behaviors are included on this page.

The following attributes and methods are **not** available on instances of CharacterRange:

> | Attributes      | Methods                     |
> |-----------------|-----------------------------|
> | baselineLocs    | characterRange              |
> | boxText         | paragraphCharacterIndexesAt |
> | boxTextPos      | paragraphRange              |
> | boxTextSize     |                             |
> | lineOrientation |                             |
> | paragraphCount  |                             |
> | pointText       |                             |

**Examples**

This increases the font size of the first character in the TextDocument, and set the rest of the characters to fontSize 40.

```javascript
var textDocument = app.project.item(index).layer(index).property("Source Text").value;
var characterRange = textDocument.characterRange(0,1);

characterRange.fontSize = characterRange.fontSize + 5;
textDocument.characterRange(1,-1).fontSize = 40;
```

---

## Attributes

### CharacterRange.characterEnd

`CharacterRange.characterEnd`

**Description**

The Text layer range calculated character end value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md#textdocument).

**Type**

Unsigned integer; read-only.

---

### CharacterRange.characterStart

`CharacterRange.characterStart`

**Description**

The Text layer range calculated character start value.

Throws an exception on access if the effective value would exceed the bounds of the related [TextDocument object](textdocument.md#textdocument).

**Type**

Unsigned integer; read-only.

---

### CharacterRange.fillColor

`CharacterRange.fillColor`

**Description**

The Text layer range CharacterRange attribute Fill Color, as an array of `[r, g, b]` floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

Setting this value will also set `applyFill` to true across the affected characters.

If this attribute has a mixed value for the range of characters, it will be read as `undefined`.

#### WARNING
In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if `applyFill` is not true.

**Type**

Array `[r, g, b]` of floating-point values; read/write.

---

### CharacterRange.isRangeValid

`CharacterRange.isRangeValid`

**Description**

Returns true if the current range is within the bounds of the related [TextDocument object](textdocument.md#textdocument), false otherwise.

**Type**

Boolean; read-only.

---

### CharacterRange.kerning

`CharacterRange.kerning`

**Description**

The Text layer range character attribute kerning option.

This effectively reports the manual kerning value, and not the calculated kerning value from auto kerning.

- If [autoKernType](textdocument.md#textdocument-autokerntype) in the range is set to `AutoKernType.METRIC_KERN`, `AutoKernType.OPTICAL_KERN`, or is mixed, then this attribute will be returned as `undefined`.
- If [autoKernType](textdocument.md#textdocument-autokerntype) in the range is set to `AutoKernType.NO_AUTO_KERN`, and this attribute has a mixed value, it will be read as `undefined`.

Setting this value will also set `AutoKernType.NO_AUTO_KERN` to true across the affected characters.

**Type**

Integer value; read/write.

---

### CharacterRange.strokeColor

`CharacterRange.strokeColor`

**Description**

The Text layer CharacterRange stroke color character property, as an array of [r, g, b] floating-point values.

For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

If this attribute has a mixed value, it will be read as `undefined`.

Setting this value will also set [applyStroke](textdocument.md#textdocument-applystroke) to true across the affected characters.

#### WARNING
In contrast to the same attribute on the TextDocument API, we will *not* throw an exception on read if [applyStroke](textdocument.md#textdocument-applystroke) is not true.

**Type**

Array [r, g, b] of floating-point values; read/write.

---

### CharacterRange.strokeOverFill

`CharacterRange.strokeOverFill`

**Description**

The Text layer CharacterRange Stroke Over Fill character property.

Indicates the rendering order for the fill and stroke for characters in the range. When true, the stroke appears over the fill.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
The Text layer can override per-character attribute setting via the All Strokes First or All Fills First setting on the CharPanel.
<br/>
The value returned here represents what is applied to the characters, without regard to the possible Text layer override.
<br/>

**Type**

Boolean; read/write.

---

### CharacterRange.text

`CharacterRange.text`

**Description**

The text value for the Text layer range.

On read, the same number of characters as the span of the range will be returned. If the span is zero (an insertion point) it return an empty string.

On write, the characters in the range will be replaced with whatever string value is supplied. If an empty string, then the characters in the range will be effectively deleted.

To insert characters without deleting any existing, call [TextDocument.characterRange()](textdocument.md#textdocument-characterrange) with the same value for start as end to get an insertion point range.

**Type**

String; read/write.

---

## Methods

### CharacterRange.pasteFrom()

`CharacterRange.pasteFrom(characterRange)`

#### NOTE
This functionality was added in After Effects (Beta) 25.0 and is subject to change while it remains in Beta.

**Description**

Copies, using paste semantics, from the `characterRange` parameter to the callee [CharacterRange object](#characterrange). The two instances may be the same, and the spans may be different.

Checks will be made that both [CharacterRange object](#characterrange) instances are valid.

The internal steps of the operation are:

> - Delete the text from the target instance.
> - Paste the text from the source instance.

As the span of the [CharacterRange object](#characterrange) is not adjusted by this call, when the source [CharacterRange object](#characterrange) instance has a shorter span than the target [CharacterRange object](#characterrange) instance, the target instance may become invalid.

**Parameters**

| `characterRange`   | A [CharacterRange object](#characterrange) whose text and styling will be pasted in place of the callee [CharacterRange object](#characterrange).   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

**Returns**

None.

---

### CharacterRange.toString()

`CharacterRange.toString()`

**Description**

Returns a string with the parameters used to create the CharacterRange instance, e.g. `"CharacterRange(0,-1)"`.

This may be safely called on an instance where isRangeValid returns false.

**Parameters**

None.

**Returns**

String; read-only.
