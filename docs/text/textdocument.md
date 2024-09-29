<a id="textdocument"></a>

# TextDocument object

`new TextDocument(docText)`
<br/>
`app.project.item(index).layer(index).property("Source Text").value`
<br/>

**Description**

The TextDocument object stores a value for a TextLayer’s Source Text property. Create it with the constructor, passing the string to be encapsulated.

**Examples**

This sets a value of some source text and displays an alert showing the new value.

```javascript
var myTextDocument = new TextDocument("HappyCake");
myTextLayer.property("Source Text").setValue(myTextDocument);
alert(myTextLayer.property("Source Text").value);
```

This sets keyframe values for text that show different words over time

```javascript
var textProp = myTextLayer.property("Source Text");
textProp.setValueAtTime(0, newTextDocument("Happy"));
textProp.setValueAtTime(.33, newTextDocument("cake"));
textProp.setValueAtTime(.66, newTextDocument("is"));
textProp.setValueAtTime(1, newTextDocument("yummy!"));
```

This sets various character and paragraph settings for some text

```javascript
var textProp = myTextLayer.property("Source Text");
var textDocument = textProp.value;
myString = "Happy holidays!";
textDocument.resetCharStyle();
textDocument.fontSize = 60;
textDocument.fillColor = [1, 0, 0];
textDocument.strokeColor = [0, 1, 0];
textDocument.strokeWidth = 2;
textDocument.font = "Times New Roman PSMT";
textDocument.strokeOverFill = true;
textDocument.applyStroke = true;
textDocument.applyFill = true;
textDocument.text = myString;
textDocument.justification = ParagraphJustification.CENTER_JUSTIFY;
textDocument.tracking = 50;
textProp.setValue(textDocument);
```

---

## Attributes

<a id="textdocument-allcaps"></a>

### TextDocument.allCaps

`textDocument.allCaps`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a Text layer has All Caps enabled; otherwise false. To set this value, use [fontCapsOption](#textdocument-fontcapsoption) added in After Effects 24.0.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

Boolean; read-only.

---

<a id="textdocument-applyfill"></a>

### TextDocument.applyFill

`textDocument.applyFill`

**Description**

When true, the Text layer shows a fill. Access the [fillColor](#textdocument-fillcolor) attribute for the actual color. When false, only a stroke is shown.

**Type**

Boolean; read/write.

---

<a id="textdocument-applystroke"></a>

### TextDocument.applyStroke

`textDocument.applyStroke`

**Description**

When true, the Text layer shows a stroke. Access the [strokeColor](#textdocument-strokecolor) attribute for the actual color and [strokeWidth](#textdocument-strokewidth) for its thickness. When false, only a fill is shown.

**Type**

Boolean; read/write.

---

<a id="textdocument-autohyphenate"></a>

### TextDocument.autoHyphenate

`textDocument.autoHyphenate`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s auto hyphenate paragraph option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-autoleading"></a>

### TextDocument.autoLeading

`textDocument.autoLeading`

**Description**

The Text layer’s auto leading character option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-autokerntype"></a>

### TextDocument.autoKernType

`textDocument.autoKernType`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s auto kern type option.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

An `AutoKernType` enumerated value; read/write. One of:

- `AutoKernType.NO_AUTO_KERN`
- `AutoKernType.METRIC_KERN`
- `AutoKernType.OPTICAL_KERN`

---

<a id="textdocument-baselinedirection"></a>

### TextDocument.baselineDirection

`textDocument.baselineDirection`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s baseline direction option. This is significant for Japanese language in vertical texts. “BASELINE_VERTICAL_CROSS_STREAM” is also know as Tate-Chu-Yoko.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

A `BaselineDirection` enumerated value; read/write. One of:

- `BaselineDirection.BASELINE_WITH_STREAM`
- `BaselineDirection.BASELINE_VERTICAL_ROTATED`
- `BaselineDirection.BASELINE_VERTICAL_CROSS_STREAM`

---

<a id="textdocument-baselinelocs"></a>

### TextDocument.baselineLocs

`textDocument.baselineLocs`

#### NOTE
This functionality was added in After Effects 13.6 (CC 2015)

**Description**

The baseline (x,y) locations for a Text layer. Line wraps in a paragraph text box are treated as multiple lines.

#### NOTE
If a line has no characters, the x and y values for start and end will be the maximum float value (3.402823466e+38F).

**Type**

Array of floating-point values in the form of

```javascript
[
  line0.start_x,
  line0.start_y,
  line0.end_x,
  line0.end_y,
  line1.start_x,
  line1.start_y,
  line1.end_x,
  line1.end_y,
  ...
  lineN-1.start_x,
  lineN-1.start_y,
  lineN-1.end_x,
  lineN-1.end_y
]
```

---

<a id="textdocument-baselineshift"></a>

### TextDocument.baselineShift

`textDocument.baselineShift`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This Text layer’s baseline shift in pixels.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Floating-point value; read-write.

---

<a id="textdocument-boxautofitpolicy"></a>

### TextDocument.boxAutoFitPolicy

`textDocument.boxAutoFitPolicy`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Enables the automated change of the box height to fit the text content in the box.
The box only grows down.

Defaults to `BoxAutoFitPolicy.NONE`.

Will be disabled if [TextDocument.boxVerticalAlignment](#textdocument-boxverticalalignment) is anything other than `BoxVerticalAlignment.TOP`.

**Type**

A `BoxAutoFitPolicy` enumerated value; read-write. One of:

- `BoxAutoFitPolicy.NONE`
- `BoxAutoFitPolicy.HEIGHT_CURSOR`
- `BoxAutoFitPolicy.HEIGHT_PRECISE_BOUNDS`
- `BoxAutoFitPolicy.HEIGHT_BASELINE`

---

<a id="textdocument-boxfirstbaselinealignment"></a>

### TextDocument.boxFirstBaselineAlignment

`textDocument.boxFirstBaselineAlignment`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Controls the position of the first line of composed text relative to the top of the box.

Disabled if [TextDocument.boxFirstBaselineAlignmentMinimum](#textdocument-boxfirstbaselinealignmentminimum) is anything other than zero.

Defaults to `BoxFirstBaselineAlignment.ASCENT`.

**Type**

A `BoxFirstBaselineAlignment` enumerated value; read-write. One of:

- `BoxFirstBaselineAlignment.ASCENT`
- `BoxFirstBaselineAlignment.CAP_HEIGHT`
- `BoxFirstBaselineAlignment.EM_BOX`
- `BoxFirstBaselineAlignment.LEADING`
- `BoxFirstBaselineAlignment.LEGACY_METRIC`
- `BoxFirstBaselineAlignment.MINIMUM_VALUE_ASIAN`
- `BoxFirstBaselineAlignment.MINIMUM_VALUE_ROMAN`
- `BoxFirstBaselineAlignment.TYPO_ASCENT`
- `BoxFirstBaselineAlignment.X_HEIGHT`

---

<a id="textdocument-boxfirstbaselinealignmentminimum"></a>

### TextDocument.boxFirstBaselineAlignmentMinimum

`textDocument.boxFirstBaselineAlignmentMinimum`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Manually controls the position of the first line of composed text relative to the top of the box.

A value set here other than zero will override the effect of the [TextDocument.boxFirstBaselineAlignment](#textdocument-boxfirstbaselinealignment) value.

Defaults to zero.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-boxinsetspacing"></a>

### TextDocument.boxInsetSpacing

`textDocument.boxInsetSpacing`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Controls the inner space between the box bounds and where the composable text box begins. The same value is applied to all four sides of the box.

Defaults to zero.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-boxoverflow"></a>

### TextDocument.boxOverflow

`textDocument.boxOverflow`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Returns true if some part of the text did not compose into the box.

**Type**

Boolean; read-only.

---

<a id="textdocument-boxtext"></a>

### TextDocument.boxText

`textDocument.boxText`

**Description**

True if a Text layer is a layer of paragraph (bounded) text; otherwise false.

**Type**

Boolean; read-only.

---

<a id="textdocument-boxtextpos"></a>

### TextDocument.boxTextPos

`textDocument.boxTextPos`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)
As of After Effects 14 (CC2017), it seems this is also writeable.

**Description**

The layer coordinates from a paragraph (box) Text layer’s anchor point as a [width, height] array of pixel dimensions.

#### WARNING
Throws an exception if [boxText](#textdocument-boxtext) does not return true for the Text layer.

**Type**

Array of ([X,Y]) position coordinates; read/write.

**Example**

```javascript
// For a paragraph Text layer returns [x, y] position from layer anchor point in layer coordinates.
// e.g. approximately [0, -25] with default character panel settings.
var boxTextLayerPos = myTextLayer.sourceText.value.boxTextPos;
```

---

<a id="textdocument-boxtextsize"></a>

### TextDocument.boxTextSize

`textDocument.boxTextSize`

**Description**

The size of a paragraph (box) Text layer as a [width, height] array of pixel dimensions.

#### WARNING
Throws an exception if [boxText](#textdocument-boxtext) does not return true for the Text layer.

**Type**

Array of two integers (minimum value of 1); read/write.

---

<a id="textdocument-boxverticalalignment"></a>

### TextDocument.boxVerticalAlignment

`textDocument.boxVerticalAlignment`

#### NOTE
This functionality was added in After Effects 24.6

**Description**

Enables the automated vertical alignment of the composed text in the box.

Defaults to `BoxVerticalAlignment.TOP`

**Type**

A `BoxVerticalAlignment` enumerated value; read-write. One of:

- `BoxVerticalAlignment.TOP`
- `BoxVerticalAlignment.CENTER`
- `BoxVerticalAlignment.BOTTOM`
- `BoxVerticalAlignment.JUSTIFY`

---

<a id="textdocument-composedlinecount"></a>

### TextDocument.composedLineCount

`textDocument.composedLineCount`

**Description**

Returns the number of composed lines in the Text layer, may be zero if all text is overset.

The [TextDocument object](#textdocument) instance is initialized from the composed state and subsequent changes to the [TextDocument object](#textdocument) instance does not cause recomposition.

Even if you remove all the text from the [TextDocument object](#textdocument) instance, the value returned here remains unchanged.

**Type**

Number; read-only.

---

<a id="textdocument-composerengine"></a>

### TextDocument.composerEngine

`textDocument.composerEngine`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph composer engine option. By default new Text layers will use the `ComposerEngine.UNIVERSAL_TYPE_ENGINE`; the other enum value will only be encountered in projects created before the Universal Type Engine engine (formerly known as the South Asian and Middle Eastern engine) became the default in [After Effects 22.1.1](https://helpx.adobe.com/after-effects/using/whats-new/2022-1.html).

If this attribute has a mixed value, it will be read as `undefined`.

This attrribute is read-write, but an exception will be thrown if any enum value other than `ComposerEngine.UNIVERSAL_TYPE_ENGINE` is written.

In effect, you can change an older document from `ComposerEngine.LATIN_CJK_ENGINE` to `ComposerEngine.UNIVERSAL_TYPE_ENGINE`, but not the reverse.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

A `ComposerEngine` enumerated value; read-write. One of:

- `ComposerEngine.LATIN_CJK_ENGINE`
- `ComposerEngine.UNIVERSAL_TYPE_ENGINE`

---

<a id="textdocument-digitset"></a>

### TextDocument.digitSet

`textDocument.digitSet`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s digit set option.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

A `DigitSet` enumerated value; read/write. One of:

- `DigitSet.DEFAULT_DIGITS`
- `DigitSet.ARABIC_DIGITS`
- `DigitSet.HINDI_DIGITS`
- `DigitSet.FARSI_DIGITS`
- `DigitSet.ARABIC_DIGITS_RTL`

---

<a id="textdocument-direction"></a>

### TextDocument.direction

`textDocument.direction`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph direction option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

A `ParagraphDirection` enumerated value; read/write. One of:

- `ParagraphDirection.DIRECTION_LEFT_TO_RIGHT`
- `ParagraphDirection.DIRECTION_RIGHT_TO_LEFT`

---

<a id="textdocument-endindent"></a>

### TextDocument.endIndent

`textDocument.endIndent`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph end indent option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-everylinecomposer"></a>

### TextDocument.everyLineComposer

`textDocument.everyLineComposer`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s Every-Line Composer paragraph option. If set to false, the TextDocument will use the Single-Line Composer.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-fauxbold"></a>

### TextDocument.fauxBold

`textDocument.fauxBold`

#### NOTE
The read functionality was added in After Effects 13.2 (CC 2014.2).
<br/>
The write functionality was added in After Effects 24.0
<br/>

**Description**

True if a Text layer has faux bold enabled; otherwise false.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Boolean; read/write.

**Example**

```javascript
var isFauxBold = myTextLayer.sourceText.value.fauxBold;
```

---

<a id="textdocument-fauxitalic"></a>

### TextDocument.fauxItalic

`textDocument.fauxItalic`

#### NOTE
The read functionality was added in After Effects 13.2 (CC 2014.2).
<br/>
The write functionality was added in After Effects 24.0
<br/>

**Description**

True if a Text layer has faux italic enabled; otherwise false.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-fillcolor"></a>

### TextDocument.fillColor

`textDocument.fillColor`

**Description**

The Text layer’s fill color, as an array of `[r, g, b]` floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

Throws an exception on read if [applyFill](#textdocument-applyfill) is not true.

Setting this value will also set [applyFill](#textdocument-applyfill) to true across the affected characters.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Array `[r, g, b]` of floating-point values; read/write.

---

<a id="textdocument-firstlineindent"></a>

### TextDocument.firstLineIndent

`textDocument.firstLineIndent`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph first line indent option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-font"></a>

### TextDocument.font

`textDocument.font`

**Description**

The Text layer’s font specified by its PostScript name.

On write, there are very few resrictions on what can be supplied - if the underlying font management system does not have a matching [Font object](fontobject.md#fontobject) instance matching the supplied PostScript name a substitute instance will be created.
The Font instance returned in the case of duplicate PostScript names will be the 0th element of the array returned from [FontsObject.getFontsByPostScriptName()](fontsobject.md#fontsobject-getfontsbypostscriptname).

You should use the [Font object](fontobject.md#fontobject) attribute for precise control.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

String; read/write.

---

<a id="textdocument-fontbaselineoption"></a>

### TextDocument.fontBaselineOption

`textDocument.fontBaselineOption`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s font baseline option. This is for setting a textDocument to superscript or subscript.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

A `FontBaselineOption` enumerated value; read/write. One of:

- `FontBaselineOption.FONT_NORMAL_BASELINE`
- `FontBaselineOption.FONT_FAUXED_SUPERSCRIPT`
- `FontBaselineOption.FONT_FAUXED_SUBSCRIPT`

---

<a id="textdocument-fontcapsoption"></a>

### TextDocument.fontCapsOption

`textDocument.fontCapsOption`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s font caps option.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

A `FontCapsOption` enumerated value; read/write. One of:

- `FontCapsOption.FONT_NORMAL_CAPS`
- `FontCapsOption.FONT_SMALL_CAPS`
- `FontCapsOption.FONT_ALL_CAPS`
- `FontCapsOption.FONT_ALL_SMALL_CAPS`

---

<a id="textdocument-fontfamily"></a>

### TextDocument.fontFamily

`textDocument.fontFamily`

#### NOTE
This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

String with with the name of the font family.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

String; read-only.

---

<a id="textdocument-fontlocation"></a>

### TextDocument.fontLocation

`textDocument.fontLocation`

#### NOTE
This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

Path of font file, providing its location on disk.

#### WARNING
Not guaranteed to be returned for all font types; return value may be empty string for some kinds of fonts.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

String; read-only.

---

<a id="textdocument-fontobject"></a>

### TextDocument.fontObject

`textDocument.fontObject`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s [Font object](fontobject.md#fontobject) specified by its PostScript name.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

[Font object](fontobject.md#fontobject); read/write.

---

<a id="textdocument-fontsize"></a>

### TextDocument.fontSize

`textDocument.fontSize`

**Description**

The Text layer’s font size in pixels.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Floating-point value (0.1 to 1296, inclusive); read/write.

---

<a id="textdocument-fontstyle"></a>

### TextDocument.fontStyle

`textDocument.fontStyle`

#### NOTE
This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

String with style information, e.g., “bold”, “italic”

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

String; read-only.

---

<a id="textdocument-hangingroman"></a>

### TextDocument.hangingRoman

`textDocument.hangingRoman`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s Roman Hanging Punctuation paragraph option. This is only meaningful to box Text layers—it allows punctuation to fit outside the box rather than flow to the next line.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-horizontalscale"></a>

### TextDocument.horizontalScale

`textDocument.horizontalScale`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This Text layer’s horizontal scale in pixels.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Floating-point value; read-write.

**Example**

```javascript
var valOfHScale = myTextLayer.sourceText.value.horizontalScale;
```

---

<a id="textdocument-justification"></a>

### TextDocument.justification

`textDocument.justification`

**Description**

The paragraph justification for the Text layer.

**Type**

A `ParagraphJustification` enumerated value; read/write. One of:

- `ParagraphJustification.LEFT_JUSTIFY`
- `ParagraphJustification.RIGHT_JUSTIFY`
- `ParagraphJustification.CENTER_JUSTIFY`
- `ParagraphJustification.FULL_JUSTIFY_LASTLINE_LEFT`
- `ParagraphJustification.FULL_JUSTIFY_LASTLINE_RIGHT`
- `ParagraphJustification.FULL_JUSTIFY_LASTLINE_CENTER`
- `ParagraphJustification.FULL_JUSTIFY_LASTLINE_FULL`
- `ParagraphJustification.MULTIPLE_JUSTIFICATIONS`

Text layers with mixed justification values will be read as `ParagraphJustification.MULTIPLE_JUSTIFICATIONS`.

Setting a TextDocument to use `ParagraphJustification.MULTIPLE_JUSTIFICATIONS` will result in `ParagraphJustification.CENTER_JUSTIFY` instead.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

---

<a id="textdocument-kerning"></a>

### TextDocument.kerning

`textDocument.kerning`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s kerning option.

Returns zero for `AutoKernType.METRIC_KERN` and `AutoKernType.OPTICAL_KERN`.

Setting this value will also set `AutoKernType.NO_AUTO_KERN` to true across the affected characters.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Integer value; read/write.

---

<a id="textdocument-leading"></a>

### TextDocument.leading

`textDocument.leading`

#### NOTE
This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

The Text layer’s spacing between lines.

Returns zero if [TextDocument.autoLeading](#textdocument-autoleading) is true.

Setting this value will also set [TextDocument.autoLeading](#textdocument-autoleading) to true across the affected characters.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

The minimum accepted value to set is 0, but this will be silently clipped to 0.01.

**Type**

Floating-point value; read/write.

**Example**

```javascript
// This creates a Text layer and sets the leading to 100

var composition = app.project.activeItem;
var myTextLayer = comp.layers.addText("Spring\nSummer\nAutumn\nWinter");
var myTextSource = myTextLayer.sourceText;
var myTextDocument = myTextSource.value;
myTextDocument.leading = 100;
myTextSource.setValue(myTextDocument);
```

---

<a id="textdocument-leadingtype"></a>

### TextDocument.leadingType

`textDocument.leadingType`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph leading type option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

A `LeadingType` enumerated value; read/write. One of:

- `LeadingType.ROMAN_LEADING_TYPE`
- `LeadingType.JAPANESE_LEADING_TYPE`

---

<a id="textdocument-ligature"></a>

### TextDocument.ligature

`textDocument.ligature`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s ligature option.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-linejointype"></a>

### TextDocument.lineJoinType

`textDocument.lineJoinType`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s line join type option for Stroke.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

A `LineJoinType` enumerated value; read/write. One of:

- `LineJoinType.LINE_JOIN_MITER`
- `LineJoinType.LINE_JOIN_ROUND`
- `LineJoinType.LINE_JOIN_BEVEL`

---

<a id="textdocument-lineorientation"></a>

### TextDocument.lineOrientation

`textDocument.lineOrientation`

#### NOTE
This functionality was added in After Effects 24.2

**Description**

The Text layer’s line orientation, in general horizontal vs vertical, which affects how all text in the layer is composed.

**Type**

A `LineOrientation` enumerated value; read/write. One of:

- `LineOrientation.HORIZONTAL`
- `LineOrientation.VERTICAL_RIGHT_TO_LEFT`
- `LineOrientation.VERTICAL_LEFT_TO_RIGHT`

---

<a id="textdocument-nobreak"></a>

### TextDocument.noBreak

`textDocument.noBreak`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s no break attribute.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-paragraphcount"></a>

### TextDocument.paragraphCount

`textDocument.paragraphCount`

**Description**

Returns the number of paragraphs in the text layer, always greater than or equal to 1.

**Type**

Number; read-only.

---

<a id="textdocument-pointtext"></a>

### TextDocument.pointText

`textDocument.pointText`

**Description**

True if a Text layer is a layer of point (unbounded) text; otherwise false.

**Type**

Boolean; read-only.

---

<a id="textdocument-smallcaps"></a>

### TextDocument.smallCaps

`textDocument.smallCaps`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a Text layer has small caps enabled; otherwise false. To set this value, use [TextDocument.fontCapsOption](#textdocument-fontcapsoption) added in After Effects 24.0.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

Boolean; read-only.

---

<a id="textdocument-spaceafter"></a>

### TextDocument.spaceAfter

`textDocument.spaceAfter`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph space after option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-spacebefore"></a>

### TextDocument.spaceBefore

`textDocument.spaceBefore`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph space before option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-startindent"></a>

### TextDocument.startIndent

`textDocument.startIndent`

#### NOTE
This functionality was added in After Effects 24.0

**Description**

The Text layer’s paragraph start indent option.

If this attribute has a mixed value, it will be read as `undefined`.

#### WARNING
This value reflects all paragraphs in the Text layer.
If you change this value, it will set all paragraphs in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-strokecolor"></a>

### TextDocument.strokeColor

`textDocument.strokeColor`

**Description**

The Text layer’s stroke color, as an array of [r, g, b] floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

Throws an exception on read if [applyStroke](#textdocument-applystroke) is not true.

Setting this value will also set [applyStroke](#textdocument-applystroke) to true across the affected characters.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Array [r, g, b] of floating-point values; read/write.

---

<a id="textdocument-strokeoverfill"></a>

### TextDocument.strokeOverFill

`textDocument.strokeOverFill`

**Description**

Indicates the rendering order for the fill and stroke of a Text layer. When true, the stroke appears over the fill.

The Text layer can override the per-character attribute setting if the Text layer is set to use All Strokes Over All Fills or All Fills Over All Strokes in the Character Panel. Thus the value returned here might be different than the actual attribute value set on the character. It is possible to set the Fill/Stroke render order via the “Fill & Stroke” property under More Options on the Text layer using TextLayer.text(“ADBE Text More Options”)(“ADBE Text Render Order”).

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Boolean; read/write.

---

<a id="textdocument-strokewidth"></a>

### TextDocument.strokeWidth

`textDocument.strokeWidth`

**Description**

The Text layer’s stroke thickness in pixels.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

The minimum accepted value to set is 0, but this will be silently clipped to 0.01.

**Type**

Floating-point value (0 to 1000, inclusive); read/write.

---

<a id="textdocument-subscript"></a>

### TextDocument.subscript

`textDocument.subscript`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a Text layer has subscript enabled; otherwise false. To set this value, use [TextDocument.fontBaselineOption](#textdocument-fontbaselineoption) added in After Effects 24.0.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

Boolean; read-only.

---

<a id="textdocument-superscript"></a>

### TextDocument.superscript

`textDocument.superscript`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a Text layer has superscript enabled; otherwise false. To set this value, use [TextDocument.fontBaselineOption](#textdocument-fontbaselineoption) added in After Effects 24.0.

#### WARNING
This value only reflects the first character in the Text layer.

**Type**

Boolean; read-only.

---

<a id="textdocument-text"></a>

### TextDocument.text

`textDocument.text`

**Description**

The text value for the Text layer’s Source Text property.

**Type**

String; read/write.

---

<a id="textdocument-tracking"></a>

### TextDocument.tracking

`textDocument.tracking`

**Description**

The Text layer’s spacing between characters.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

---

<a id="textdocument-tsume"></a>

### TextDocument.tsume

`textDocument.tsume`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This Text layer’s tsume value as a normalized percentage, from 0.0 -> 1.0.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

This attribute accepts values from 0.0 -> 100.0, however the value IS expecting a normalized value from 0.0 -> 1.0. Using a value higher than 1.0 will produce unexpected results; AE’s Character Panel will clamp the value at 100%, despite the higher value set by scripting (ie `TextDocument.tsume = 100` \_really_ sets a value of 10,000%)

**Type**

Floating-point value; read-write.

---

<a id="textdocument-verticalscale"></a>

### TextDocument.verticalScale

`textDocument.verticalScale`

#### NOTE
This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This Text layer’s vertical scale in pixels.

#### WARNING
This value only reflects the first character in the Text layer.
If you change this value, it will set all characters in the Text layer to the specified setting.

**Type**

Floating-point value; read-write.

---

## Methods

<a id="textdocument-characterrange"></a>

### TextDocument.characterRange()

`textDocument.characterRange(characterStart, [signedCharacterEnd])`

#### NOTE
This functionality was added in After Effects 24.3

**Description**

Returns an instance of the Text layer range accessor CharacterRange.

The instance will remember the parameters passed in the constructor - they remain constant and changes to the [TextDocument](#textdocument) length may cause the instance to throw exceptions on access until the [TextDocument](#textdocument) length is changed to a length which makes the range valid again.

Use toString() to find out what the constructed parameters were.

**Parameters**

| `characterStart`     | Unsigned integer. Starts at zero, must be the less<br/>than or equal to the (text) length of the [TextDocument object](#textdocument).                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `signedCharacterEnd` | Optional signed integer. If not specified, will be computed at (characterStart + 1).<br/><br/><br/>If set to -1, then the [CharacterRange object](characterrange.md#characterrange) will dynamically calculate this on access to be equal to the (text) length of the [TextDocument object](#textdocument).<br/><br/><br/>signedCharacterEnd must be greater than or equal to characterStart, and less than or equal to the (text) length of the [TextDocument object](#textdocument).<br/><br/> |

Throws an exception if the parameters would result in an invalid range.

It is not possible to create a [CharacterRange object](characterrange.md#characterrange) which spans the final carriage return in the [TextDocument object](#textdocument).

**Returns**

An instance of [CharacterRange object](characterrange.md#characterrange)

---

<a id="textdocument-composedlinecharacterindexesat"></a>

### TextDocument.composedLineCharacterIndexesAt()

`textDocument.composedLineCharacterIndexesAt(characterIndex)`

#### NOTE
This functionality was added in After Effects 24.3

**Description**

Returns the character index bounds of a [ComposedLineRange object](composedlinerange.md#composedlinerange) in the Text layer.

**Parameters**

| `characterIndex`   | Unsigned integer. A text index in the Text layer, which will be mapped to the composed line it intersects.   |
|--------------------|--------------------------------------------------------------------------------------------------------------|

**Returns**

Generic object;
Key `start` will be set to text index of the start of the composed line (greater than or equal to zero).
Key `end` will be set to text index of the end of the composed line (greater than start, or equal to start if it is the last composed line).

Will throw an exception if the computed start and end are outside of the current [TextDocument object](#textdocument)
Remember that the composed lines are static and subsequent changes to the [TextDocument object](#textdocument) instance which changes its length may render the composed line data invalid.

---

<a id="textdocument-composedlinerange"></a>

### TextDocument.composedLineRange()

`textDocument.composedLineRange(composedLineIndexStart, [signedComposedLineIndexEnd])`

#### NOTE
This functionality was added in After Effects 24.3

**Description**

Returns an instance of the Text layer range accessor [ComposedLineRange object](composedlinerange.md#composedlinerange).

The instance will remember the parameters passed in the constructor - they remain constant and changes to the [TextDocument](#textdocument) contents may cause the instance to throw exceptions on access until the [TextDocument](#textdocument) contents are changed which makes the range valid again.

Use [ComposedLineRange.toString()](composedlinerange.md#composedlinerange-tostring) to find out what the constructed parameters were.

**Parameters**

| `composedLineIndexStart`     | Unsigned integer. Starts at zero, must be the less than the number of composed lines in the [TextDocument object](#textdocument).                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `signedComposedLineIndexEnd` | Optional signed integer. If not specified, will be computed at (composedLineIndexStart + 1).<br/><br/><br/>If set to -1, then the [ComposedLineRange object](composedlinerange.md#composedlinerange) will dynamically calculate this on access to the last composed line of the [TextDocument object](#textdocument).<br/><br/><br/>signedComposedLineIndexEnd must be greater than composedLineIndexStart, and less than or equal to the number of composed lines in the [TextDocument object](#textdocument).<br/><br/> |

Throws an exception if the parameters would result in an invalid range.

Remember that the composed lines are static and subsequent changes to the [TextDocument object](#textdocument) instance which changes its length may render the composed line data invalid.

**Returns**

An instance of [ComposedLineRange object](composedlinerange.md#composedlinerange)

---

<a id="textdocument-paragraphcharacterindexesat"></a>

### TextDocument.paragraphCharacterIndexesAt()

`textDocument.paragraphCharacterIndexesAt(characterIndex)`

#### NOTE
This functionality was added in After Effects 24.3

**Description**

Returns the character index bounds of a paragraph in the Text layer.

**Parameters**

| `characterIndex`   | Unsigned integer. A text index in the Text layer, which will be mapped to the paragraph it intersects.   |
|--------------------|----------------------------------------------------------------------------------------------------------|

**Returns**

Generic object;
Key `start` will be set to text index of the start of the paragraph (greater than or equal to zero).
Key `end` will be set to text index of the end of the paragraph (greater than start, or equal to start if it is the last paragraph).

---

<a id="textdocument-paragraphrange"></a>

### TextDocument.paragraphRange()

`textDocument.paragraphRange(paragraphIndexStart, [signedParagraphIndexEnd])`

#### NOTE
This functionality was added in After Effects 24.3

**Description**

Returns an instance of the Text layer range accessor [ParagraphRange object](paragraphrange.md#paragraphrange).

The instance will remember the parameters passed in the constructor - they remain constant and changes to the [TextDocument](#textdocument) contents may cause the instance to throw exceptions on access until the [TextDocument](#textdocument) contents are changed which makes the range valid again.

Use [ParagraphRange.toString()](paragraphrange.md#paragraphrange-tostring) to find out what the constructed parameters were.

**Parameters**

| `paragraphIndexStart`     | Unsigned integer. Starts at zero, must be the less than the number of paragraphs in the [TextDocument object](#textdocument).                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `signedParagraphIndexEnd` | Optional signed integer. If not specified, will be computed at (paragraphIndexStart + 1).<br/><br/><br/>If set to -1, then the [ParagraphRange object](paragraphrange.md#paragraphrange) will dynamically calculate this on access to the last paragraph of the [TextDocument object](#textdocument).<br/><br/><br/>signedParagraphIndexEnd must be greater than paragraphIndexStart, and less than or equal to the number of paragraphs in the [TextDocument object](#textdocument).<br/><br/> |

Throws an exception if the parameters would result in an invalid range.

**Returns**

An instance of [ParagraphRange object](paragraphrange.md#paragraphrange)

---

<a id="textdocument-resetcharstyle"></a>

### TextDocument.resetCharStyle()

`textDocument.resetCharStyle()`

**Description**

Restores all characters in the Text layer to the default text character characteristics in the Character panel.

**Parameters**

None.

**Returns**

Nothing.

---

<a id="textdocument-resetparagraphstyle"></a>

### TextDocument.resetParagraphStyle()

`textDocument.resetParagraphStyle()`

**Description**

Restores all paragraphs in the Text layer to the default text paragraph characteristics in the Paragraph panel.

**Parameters**

None.

**Returns**

Nothing.
