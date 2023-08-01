.. highlight:: javascript
.. _TextDocument:

TextDocument object
################################################

|  ``new TextDocument(docText)``
|  ``app.project.item(index).layer(index).property("Source Text").value``

**Description**

The TextDocument object stores a value for a TextLayer's Source Text property. Create it with the constructor, passing the string to be encapsulated.

**Examples**

This sets a value of some source text and displays an alert showing the new value.

.. code:: javascript

    var myTextDocument = new TextDocument("HappyCake");
    myTextLayer.property("Source Text").setValue(myTextDocument);
    alert(myTextLayer.property("Source Text").value);

This sets keyframe values for text that show different words over time

.. code:: javascript

    var textProp = myTextLayer.property("Source Text");
    textProp.setValueAtTime(0, newTextDocument("Happy"));
    textProp.setValueAtTime(.33, newTextDocument("cake"));
    textProp.setValueAtTime(.66, newTextDocument("is"));
    textProp.setValueAtTime(1, newTextDocument("yummy!"));

This sets various character and paragraph settings for some text

.. code:: javascript

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

----

==========
Attributes
==========

.. _TextDocument.allCaps:

TextDocument.allCaps
*********************************************

``textDocument.allCaps``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a text layer has allcaps enabled; otherwise false. To set this value, use :ref:`TextDocument.fontCapsOption` added in After Effects 24.0.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

----

.. _TextDocument.applyFill:

TextDocument.applyFill
*********************************************

``textDocument.applyFill``

**Description**

When true, the text layer shows a fill. Access the ``fillColor`` attribute for the actual color. When false, only a stroke is shown.

**Type**

Boolean; read/write.

----

.. _TextDocument.applyStroke:

TextDocument.applyStroke
*********************************************

``textDocument.applyStroke``

**Description**

When true, the text layer shows a stroke. Access the ``strokeColor`` attribute for the actual color and ``strokeWidth`` for its thickness. When false, only a fill is shown.

**Type**

Boolean; read/write.

----

.. _TextDocument.autoHyphenate:

TextDocument.autoHyphenate
*********************************************

``textDocument.autoHyphenate``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's auto hyphenate paragraph option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.autoKernType:

TextDocument.autoKernType
*********************************************

``textDocument.autoKernType``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's auto kern type option.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

An ``AutoKernType`` enumerated value; read/write. One of:

-  ``AutoKernType.NO_AUTO_KERN``
-  ``AutoKernType.METRIC_KERN``
-  ``AutoKernType.OPTICAL_KERN``

----

.. _TextDocument.baselineDirection:

TextDocument.baselineDirection
*********************************************

``textDocument.baselineDirection``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's baseline direction option. This is significant for Japanese language in vertical texts. "BASELINE_VERTICAL_CROSS_STREAM" is also know as Tate-Chu-Yoko.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

A ``BaselineDirection`` enumerated value; read/write. One of:

-  ``BaselineDirection.BASELINE_WITH_STREAM``
-  ``BaselineDirection.BASELINE_VERTICAL_ROTATED``
-  ``BaselineDirection.BASELINE_VERTICAL_CROSS_STREAM``

----

.. _TextDocument.baselineLocs:

TextDocument.baselineLocs
*********************************************

``textDocument.baselineLocs``

.. note::
   This functionality was added in After Effects 13.6 (CC 2015)

**Description**

The baseline (x,y) locations for a text layer. Line wraps in a paragraph text box are treated as multiple lines.

.. note::
  If a line has no characters, the x and y values for start and end will be the maximum float value (3.402823466e+38F).

**Type**

Array of floating-point values in the form of

.. code:: javascript

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

----

.. _TextDocument.baselineShift:

TextDocument.baselineShift
*********************************************

``textDocument.baselineShift``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This text layer's baseline shift in pixels.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Floating-point value; read-only.

----

.. _TextDocument.boxText:

TextDocument.boxText
*********************************************

``textDocument.boxText``

**Description**

True if a text layer is a layer of paragraph (bounded) text; otherwise false.

**Type**

Boolean; read-only.

----

.. _TextDocument.boxTextPos:

TextDocument.boxTextPos
*********************************************

``textDocument.boxTextPos``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)
   As of After Effects 14 (CC2017), it seems this is also writeable.

**Description**

The layer coordinates from a paragraph (box) text layer's anchor point as a [width, height] array of pixel dimensions.

.. warning::
  This attribute only works on paragraph text layers.
  This value only reflects the first character in the text layer at the current time.

**Type**

Array of ([X,Y]) position coordinates; read/write.

**Example**

.. code:: javascript

    // For a paragraph text layer returns [x, y] position from layer anchor point in layer coordinates.
    // e.g. approximately [0, -25] with default character panel settings.
    var boxTextLayerPos = myTextLayer.sourceText.value.boxTextPos;

----

.. _TextDocument.boxTextSize:

TextDocument.boxTextSize
*********************************************

``textDocument.boxTextSize``

**Description**

The size of a paragraph (box) text layer as a [width, height] array of pixel dimensions.

**Type**

Array of two integers (minimum value of 1); read/write.

----

.. _TextDocument.digitSet:

TextDocument.digitSet
*********************************************

``textDocument.digitSet``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's digit set option.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

A ``DigitSet`` enumerated value; read/write. One of:

-  ``DigitSet.DEFAULT_DIGITS``
-  ``DigitSet.ARABIC_DIGITS``
-  ``DigitSet.HINDI_DIGITS``
-  ``DigitSet.FARSI_DIGITS``
-  ``DigitSet.ARABIC_DIGITS_RTL``

----

.. _TextDocument.direction:

TextDocument.direction
*********************************************

``textDocument.direction``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph direction option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

A ``ParagraphDirection`` enumerated value; read/write. One of:

-  ``ParagraphDirection.DIRECTION_LEFT_TO_RIGHT``
-  ``ParagraphDirection.DIRECTION_RIGHT_TO_LEFT``

----

.. _TextDocument.endIndent:

TextDocument.endIndent
*********************************************

``textDocument.endIndent``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph end indent option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.everyLineComposer:

TextDocument.everyLineComposer
*********************************************

``textDocument.everyLineComposer``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's Every-Line Composer paragraph option. If set to false, the TextDocument will use the Single-Line Composer.
   
If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.fauxBold:

TextDocument.fauxBold
*********************************************

``textDocument.fauxBold``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)
   The write functionality was added in After Effects 24.0

**Description**

True if a text layer has faux bold enabled; otherwise false.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read/write.

**Example**

.. code:: javascript

    var isFauxBold = myTextLayer.sourceText.value.fauxBold;

----

.. _TextDocument.fauxItalic:

TextDocument.fauxItalic
*********************************************

``textDocument.fauxItalic``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)
   The write functionality was added in After Effects 24.0

**Description**

True if a text layer has faux italic enabled; otherwise false.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read/write.

----

.. _TextDocument.fillColor:

TextDocument.fillColor
*********************************************

``textDocument.fillColor``

**Description**

The text layer's fill color, as an array of ``[r, g, b]`` floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Array ``[r, g, b]`` of floating-point values; read/write.

----

.. _TextDocument.firstLineIndent:

TextDocument.firstLineIndent
*********************************************

``textDocument.firstLineIndent``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph first line indent option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.font:

TextDocument.font
*********************************************

``textDocument.font``

**Description**

The text layer's font specified by its PostScript name. This is just a string, you should use the :ref:`fontObject` property for precise control.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

String; read/write.

----

.. _TextDocument.fontBaselineOption:

TextDocument.fontBaselineOption
*********************************************

``textDocument.fontBaselineOption``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's font baseline option. This is for setting a textDocument to superscript or subscript. 

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

A ``FontBaselineOption`` enumerated value; read/write. One of:

-  ``FontBaselineOption.FONT_NORMAL_BASELINE``
-  ``FontBaselineOption.FONT_FAUXED_SUPERSCRIPT``
-  ``FontBaselineOption.FONT_FAUXED_SUBSCRIPT``

----

.. _TextDocument.fontCapsOption:

TextDocument.fontCapsOption
*********************************************

``textDocument.fontCapsOption``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's font caps option.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

A ``FontCapsOption`` enumerated value; read/write. One of:

-  ``FontCapsOption.FONT_NORMAL_CAPS``
-  ``FontCapsOption.FONT_SMALL_CAPS``
-  ``FontCapsOption.FONT_ALL_CAPS``
-  ``FontCapsOption.FONT_ALL_SMALL_CAPS``

----

.. _TextDocument.fontFamily:

TextDocument.fontFamily
*********************************************

``textDocument.fontFamily``

.. note::
   This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

String with with the name of the font family.

.. warning::
  This value only reflects the first character in the text layer at the current time.

**Type**

String; read-only.

----

.. _TextDocument.fontLocation:

TextDocument.fontLocation
*********************************************

``textDocument.fontLocation``

.. note::
   This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

Path of font file, providing its location on disk.

.. warning::
  Not guaranteed to be returned for all font types; return value may be empty string for some kinds of fonts.

.. warning::
  This value only reflects the first character in the text layer at the current time.

**Type**

String; read-only.

----

.. _TextDocument.fontObject:

TextDocument.fontObject
*********************************************

``textDocument.fontObject``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's :ref:`fontObject` specified by its PostScript name.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

:ref:`fontObject`; read/write.

----

.. _TextDocument.fontSize:

TextDocument.fontSize
*********************************************

``textDocument.fontSize``

**Description**

The text layer's font size in pixels.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value (0.1 to 1296, inclusive); read/write.

----

.. _TextDocument.fontStyle:

TextDocument.fontStyle
*********************************************

``textDocument.fontStyle``

.. note::
   This functionality was added in After Effects 13.1 (CC 2014.1)

**Description**

String with style information, e.g., "bold", "italic"

.. warning::
  This value only reflects the first character in the text layer at the current time.

**Type**

String; read-only.

----

.. _TextDocument.hangingRoman:

TextDocument.hangingRoman
*********************************************

``textDocument.hangingRoman``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's Roman Hanging Punctuation paragraph option. This is only applicable to box text layers—it allows punctuation to fit outside the box rather than flow to the next line.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.horizontalScale:

TextDocument.horizontalScale
*********************************************

``textDocument.horizontalScale``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This text layer's horizontal scale in pixels.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Floating-point value; read-only.

**Example**

.. code:: javascript

    var valOfHScale = myTextLayer.sourceText.value.horizontalScale;

----

.. _TextDocument.justification:

TextDocument.justification
*********************************************

``textDocument.justification``

**Description**

The paragraph justification for the text layer.

**Type**

A ``ParagraphJustification`` enumerated value; read/write. One of:

-  ``ParagraphJustification.LEFT_JUSTIFY``
-  ``ParagraphJustification.RIGHT_JUSTIFY``
-  ``ParagraphJustification.CENTER_JUSTIFY``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_LEFT``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_RIGHT``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_CENTER``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_FULL``
-  ``ParagraphJustification.MULTIPLE_JUSTIFICATIONS``

Text layers with mixed justification values will be read as ``ParagraphJustification.MULTIPLE_JUSTIFICATIONS``, but setting a TextDocument to use this value will result in ``ParagraphJustification.CENTER_JUSTIFY`` instead.

----

.. _TextDocument.kerning:

TextDocument.kerning
*********************************************

``textDocument.kerning``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's kerning option.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Integer value; read/write.

----

.. _TextDocument.leading:

TextDocument.leading
*********************************************

``textDocument.leading``

.. note::
   This functionality was added in After Effects 14.2 (CC 2017.1)

**Description**

The text layer's spacing between lines.

.. warning::
   If the text layer has different leading settings for each line, this attribute returns the setting for the first line.
   Also, if you change the value, it resets all lines in the text layer to the specified setting..

**Type**

Floating-point value; read/write.

**Example**

.. code:: javascript

    // This creates a text layer and sets the leading to 100

    var composition = app.project.activeItem;
    var myTextLayer = comp.layers.addText("Spring\nSummer\nAutumn\nWinter");
    var myTextSource = myTextLayer.sourceText;
    var myTextDocument = myTextSource.value;
    myTextDocument.leading = 100;
    myTextSource.setValue(myTextDocument);

----

.. _TextDocument.leadingType:

TextDocument.leadingType
*********************************************

``textDocument.leadingType``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph leading type option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

A ``LeadingType`` enumerated value; read/write. One of:

-  ``LeadingType.ROMAN_LEADING_TYPE``
-  ``LeadingType.JAPANESE_LEADING_TYPE``

----

.. _TextDocument.ligature:

TextDocument.ligature
*********************************************

``textDocument.ligature``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's ligature option.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.lineJoinType:

TextDocument.lineJoinType
*********************************************

``textDocument.lineJoinType``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's line join type option for Stroke.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

A ``LineJoinType`` enumerated value; read/write. One of:

-  ``LineJoinType.LINE_JOIN_MITER``
-  ``LineJoinType.LINE_JOIN_ROUND``
-  ``LineJoinType.LINE_JOIN_BEVEL``

----

.. _TextDocument.noBreak:

TextDocument.noBreak
*********************************************

``textDocument.noBreak``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's no break attribute.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.pointText:

TextDocument.pointText
*********************************************

``textDocument.pointText``

**Description**

True if a text layer is a layer of point (unbounded) text; otherwise false.

**Type**

Boolean; read-only.

----

.. _TextDocument.smallCaps:

TextDocument.smallCaps
*********************************************

``textDocument.smallCaps``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a text layer has small caps enabled; otherwise false. To set this value, use :ref:`TextDocument.fontCapsOption` added in After Effects 24.0.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

----

.. _TextDocument.spaceAfter:

TextDocument.spaceAfter
*********************************************

``textDocument.spaceAfter``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph space after option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.spaceBefore:

TextDocument.spaceBefore
*********************************************

``textDocument.spaceBefore``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph space before option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.startIndent:

TextDocument.startIndent
*********************************************

``textDocument.startIndent``

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

**Description**

The text layer's paragraph start indent option.

If this attribute has a mixed value on a TextDocument, it will be read as ``undefined``.

.. warning::
   If you change this value, it will reset all lines in the Text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.strokeColor:

TextDocument.strokeColor
*********************************************

``textDocument.strokeColor``

**Description**

The text layer's stroke color, as an array of [r, g, b] floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Array [r, g, b] of floating-point values; read/write.

----

.. _TextDocument.strokeOverFill:

TextDocument.strokeOverFill
*********************************************

``textDocument.strokeOverFill``

**Description**

Indicates the rendering order for the fill and stroke of a text layer. When true, the stroke appears over the fill.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.strokeWidth:

TextDocument.strokeWidth
*********************************************

``textDocument.strokeWidth``

**Description**

The text layer's stroke thickness in pixels.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value (0 to 1000, inclusive); read/write.

----

.. _TextDocument.subscript:

TextDocument.subscript
*********************************************

``textDocument.subscript``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a text layer has subscript enabled; otherwise false. To set this value, use :ref:`TextDocument.fontBaselineOption` added in After Effects 24.0.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

----

.. _TextDocument.superscript:

TextDocument.superscript
*********************************************

``textDocument.superscript``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a text layer has superscript enabled; otherwise false. To set this value, use :ref:`TextDocument.fontBaselineOption` added in After Effects 24.0.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

----

.. _TextDocument.text:

TextDocument.text
*********************************************

``textDocument.text``

**Description**

The text value for the text layer's Source Text property.

**Type**

String; read/write.

----

.. _TextDocument.tracking:

TextDocument.tracking
*********************************************

``textDocument.tracking``

**Description**

The text layer's spacing between characters.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value; read/write.

----

.. _TextDocument.tsume:

TextDocument.tsume
*********************************************

``textDocument.tsume``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This text layer's tsume value as a normalized percentage, from 0.0 -> 1.0.

.. warning::
   This value only reflects the first character in the text layer at the current time.

   This property accepts values from 0.0 -> 100.0, however the value IS expecting a normalized value from 0.0 -> 1.0. Using a value higher than 1.0 will produce unexpected results; AE's Character Panel will clamp the value at 100%, despite the higher value set by scripting (ie ``TextDocument.tsume = 100`` _really_ sets a value of 10,000%)

**Type**

Floating-point value; read-only.

----

.. _TextDocument.verticalScale:

TextDocument.verticalScale
*********************************************

``textDocument.verticalScale``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

This text layer's vertical scale in pixels.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Floating-point value; read-only.

----

=======
Methods
=======

.. _TextDocument.resetCharStyle:

TextDocument.resetCharStyle()
*********************************************

``textDocument.resetCharStyle()``

**Description**

Restores the default text character characteristics in the Character panel.

**Parameters**

None.

**Returns**

Nothing.

----

.. _TextDocument.resetParagraphStyle:

TextDocument.resetParagraphStyle()
*********************************************

``textDocument.resetParagraphStyle()``

**Description**

Restores the default text paragraph characteristics in the Paragraph panel.

**Parameters**

None.

**Returns**

Nothing.
