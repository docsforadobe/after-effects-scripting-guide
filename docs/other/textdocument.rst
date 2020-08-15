.. highlight:: javascript
.. _TextDocument:

TextDocument object
################################################

|  ``new TextDocument(docText)``
|  ``app.project.item(index).layer(index).property("Source Text").value``

**Description**

The TextDocument object stores a value for a TextLayer's Source Text property. Create it with the constructor, passing the string to be encapsulated.

**Examples**

This sets a value of some source text and displays an alert showing the new value

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

True if a text layer has allcaps enabled; otherwise false.

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

Array of ([X,Y]) position coordinates; read-only.

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

.. _TextDocument.fauxBold:

TextDocument.fauxBold
*********************************************

``textDocument.fauxBold``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

True if a text layer has faux bold enabled; otherwise false.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

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

**Description**

True if a text layer has faux italic enabled; otherwise false.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

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

.. _TextDocument.font:

TextDocument.font
*********************************************

``textDocument.font``

**Description**

The text layer's font specified by its PostScript name.

.. warning::
   This value only reflects the first character in the text layer at the current time.
   If you change this value, it resets all characters in the text layer to the specified setting.

**Type**

String; read/write.

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

A ``ParagraphJustification`` enumerated value; read-only. One of:

-  ``ParagraphJustification.LEFT_JUSTIFY``
-  ``ParagraphJustification.RIGHT_JUSTIFY``
-  ``ParagraphJustification.CENTER_JUSTIFY``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_LEFT``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_RIGHT``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_CENTER``
-  ``ParagraphJustification.FULL_JUSTIFY_LASTLINE_FULL``

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

True if a text layer has small caps enabled; otherwise false.

.. warning::
   This value only reflects the first character in the text layer at the current time.

**Type**

Boolean; read-only.

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

True if a text layer has subscript enabled; otherwise false.

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

True if a text layer has superscript enabled; otherwise false.

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

This text layer's tsume value.

.. warning::
   This value only reflects the first character in the text layer at the current time.

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

.. _TextDocument.compPointToSource:

TextDocument.compPointToSource()
*********************************************

``textDocument.compPointToSource()``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

Converts composition coordinates, such as ``sourcePointToComp``, to layer coordinates.

.. warning::
  This method only works on paragraph text layers.
  This value only reflects the first character in the text layer at the current time.

**Parameters**

=====================  =====================================================================
``sourcePointToComp``  A position array of composition coordinates in ([X, Y]) format.
=====================  =====================================================================

**Returns**

Array of ([X,Y]) position coordinates; read-only.

----

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

----

.. _TextDocument.sourcePointToComp:

TextDocument.sourcePointToComp()
*********************************************

``textDocument.sourcePointToComp()``

.. note::
   This functionality was added in After Effects 13.2 (CC 2014.2)

**Description**

Converts layer coordinates, such as ``boxTextPos``, to composition coordinates.

.. warning::
  This method only works on paragraph text layers.
  This value only reflects the first character in the text layer at the current time.

**Parameters**

==============  =====================================================================
``boxTextPos``  A position array of layer coordinates in ([X, Y]) format.
==============  =====================================================================

**Returns**

Array of ([X,Y]) position coordinates; read-only.

**Example**

.. code:: javascript

    // For a paragraph text layer.
    // Converts position in layer coordinates to comp coordinates.
    var boxTextCompPos = myTextLayer.sourcePointToComp(boxTextLayerPos);
