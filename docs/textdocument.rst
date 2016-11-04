.. highlight:: javascript
.. _TextDocument:

TextDocument object
################################################

|  ``new TextDocument(docText)``
|  ``app.project.item(index).layer(index).property("SourceText").value``

**Description**

The TextDocument object stores a value for a TextLayer's Source Text property. Create it with the constructor, passing the string to be encapsulated.

**Examples**

This sets a value of some source text and displays an alert showing the new value::

    var myTextDocument = newTextDocument("HappyCake");
    myTextLayer.property("SourceText").setValue(myTextDocument);
    alert(myTextLayer.property("SourceText").value);

This sets keyframe values for text that show different words over time::

    var textProp = myTextLayer.property("Source Text");
    textProp.setValueAtTime(0, newTextDocument("Happy"));
    textProp.setValueAtTime(.33, newTextDocument("cake"));
    textProp.setValueAtTime(.66, newTextDocument("is"));
    textProp.setValueAtTime(1, newTextDocument("yummy!"));

This sets various character and paragraph settings for some text::

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

.. _TextDocument.boxText:

TextDocument.boxText
*********************************************

``textDocument.boxText``

**Description**

True if a text layer is a layer of paragraph (bounded) text; otherwise false.

**Type**

Boolean; read-only.

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

.. _TextDocument.fillColor:

TextDocument.fillColor
*********************************************

``textDocument.fillColor``

**Description**

The text layer’s fill color, as an array of ``[r, g, b]`` floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

.. note:: If the text layer has different fill color settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Array ``[r, g, b]`` of floating-point values; read/write.

----

.. _TextDocument.font:

TextDocument.font
*********************************************

``textDocument.font``

**Description**

The text layer’s font specified by its PostScript name.

.. note:: If the text layer has different font settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

String; read/write.

----

.. _TextDocument.fontSize:

TextDocument.fontSize
*********************************************

``textDocument.fontSize``

**Description**

The text layer’s font size in pixels.

.. note:: If the text layer has different font size settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value (0.1 to 1296, inclusive); read/write.

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

.. _TextDocument.pointText:

TextDocument.pointText
*********************************************

``textDocument.pointText``

**Description**

True if a text layer is a layer of point (unbounded) text; otherwise false.

**Type**

Boolean; read-only.

----

.. _TextDocument.strokeColor:

TextDocument.strokeColor
*********************************************

``textDocument.strokeColor``

**Description**

The text layer’s stroke color, as an array of [r, g, b] floating-point values. For example, in an 8-bpc project, a red value of 255 would be 1.0, and in a 32-bpc project, an overbright blue value can be something like 3.2.

.. note:: If the text layer has different stroke color settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Array [r, g, b] of floating-point values; read/write.

----

.. _TextDocument.strokeOverFill:

TextDocument.strokeOverFill
*********************************************

``textDocument.strokeOverFill``

**Description**

Indicates the rendering order for the fill and stroke of a text layer. When true, the stroke appears over the fill.

.. note:: If the text layer has different fill/stroke rendering order settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Boolean; read/write.

----

.. _TextDocument.strokeWidth:

TextDocument.strokeWidth
*********************************************

``textDocument.strokeWidth``

**Description**

The text layer’s stroke thickness in pixels.

.. note:: If the text layer has different stroke width settings for each character, this attribute returns the setting forthe first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value (0 to 1000, inclusive); read/write.

----

.. _TextDocument.text:

TextDocument.text
*********************************************

``textDocument.text``

**Description**

The text value for the text layer’s Source Text property.

**Type**

String; read/write.

----

.. _TextDocument.tracking:

TextDocument.tracking
*********************************************

``textDocument.tracking``

**Description**

The text layer’s spacing between characters.

.. note:: If the text layer has different tracking settings for each character, this attribute returns the setting for the first character. Also, if you change the value, it resets all characters in the text layer to the specified setting.

**Type**

Floating-point value; read/write.

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
