.. highlight:: javascript
.. _FontObject:

Font object
################################################

.. note::
   This functionality was added in After Effects 24.0.

**Description**

The Font object provides information about a specific font, along with the font technology used, helping disambiguate when multiple fonts sharing the same Postscript name are installed on the system.

Most of these APIs simply return information which is contained in the Font data file itself, seek more information there.

----

==========
Attributes
==========

.. _FontObject.designAxesData:

FontObject.designAxesData
*********************************************

``app.fonts.allFonts[0][0].designAxesData``

**Description**

Returns an Array of Objects, containing the design axes data from the font. 
Each object is composed of the axis ``name``, ``tag``, ``min`` value and ``max`` value.

.. note::
  Will return undefined for non-variable fonts.

**Example**

This example will select the first returned Font Family Array.

.. code:: javascript

   // Getting the first available Variable Font on the system
   var firstVariableFont = fontsWithDefaultDesignAxes[0];
   var axesData = firstVariableFont.designAxesData;

   // Getting the first design axis for that Font 
   var firstAxis = axesData[0];

   alert(firstAxis.name+"\n"+firstAxis.tag+"\n"+firstAxis.min+"\n"+firstAxis.max);

**Type**

Array of Objects; read-only.

----

.. _FontObject.designVector:

FontObject.designVector
*********************************************

``app.fonts.fontsWithDefaultDesignAxes[0].designVector``

**Description**

For Variable fonts will return an ordered array with a length matching the number of design axes defined by the font.

.. note::
  Will return undefined for non-variable fonts. 

**Type**

Array of floating-point values; read-only.

----



.. _FontObject.familyName:

FontObject.familyName
*********************************************

``app.fonts.allFonts[0][0].familyName``

**Description**

The family name of the font, in the ASCII character set.

**Type**

String; read-only.

----

.. _FontObject.familyPrefix:

FontObject.familyPrefix
*********************************************

``app.fonts.fontsWithDefaultDesignAxes[0].familyPrefix``

**Description**

The family prefix of the variable font. For example, the family of the PostScript name "SFPro-Bold" is "SFPro".

.. note::
  Will return undefined for non-variable fonts.

**Type**

String; read-only.

----

.. _FontObject.fontID:

FontObject.fontID
*********************************************

``app.fonts.allFonts[0][0].fontID``

.. note::
   This functionality was added in After Effects 24.2.

**Description**

A unique number assigned to the FontObject instance when it is created, value is greater than or equal to 1. It never changes during the application session but may be different in subsequent launches of the application. 

Can be used to compare two FontObject instances to see if they refer to the same underlying native font instance.

FontObjects can be looked up by fontID with :ref:`getFontByID<FontsObject.getFontByID>` .

**Type**

Number; read-only.

----

.. _FontObject.fullName:

FontObject.fullName
*********************************************

``app.fonts.allFonts[0][0].fullName``

**Description**

The full name of the font, in the ASCII character set. Usually composed of the family name and the style name. 

**Type**

String; read-only.

----

.. _FontObject.hasDesignAxes:

FontObject.hasDesignAxes
*********************************************

``app.fonts.allFonts[0][0].hasDesignAxes``

**Description**

Returns true if the font is a variable font.

**Type**

Boolean; read-only.

----

.. _FontObject.isFromAdobeFonts:

FontObject.isFromAdobeFonts
*********************************************

``app.fonts.allFonts[0][0].isFromAdobeFonts``

**Description**

Returns true if the font is from Adobe Fonts.

**Type**

Boolean; read-only.

----

.. _FontObject.isSubstitute:

FontObject.isSubstitute
*********************************************

``app.fonts.allFonts[0][0].isSubstitute``

**Description**

Returns true when this font instance represents a font reference which was missing on project open.

**Type**

Boolean; read-only.

----

.. _FontObject.location:

FontObject.location
*********************************************

``app.fonts.allFonts[0][0].location``

**Description**

The location of the font file on your system.

.. warning::
  Not guaranteed to be returned for all font types; return value may be empty string for some kinds of fonts.

**Type**

String; read-only.

----

.. _FontObject.nativeFamilyName:

FontObject.nativeFamilyName
*********************************************

``app.fonts.allFonts[0][0].nativeFamilyName``

**Description**

The native family name of the font in full 16 bit Unicode. Often different than what is returned by :ref:`FontObject.familyName` for non-Latin fonts.

**Type**

String; read-only.

----

.. _FontObject.nativeFullName:

FontObject.nativeFullName
*********************************************

``app.fonts.allFonts[0][0].nativeFullName``

**Description**

The native full name of the font in full 16 bit Unicode. Often different than what is returned by :ref:`FontObject.fullName` for non-Latin fonts.

**Type**

String; read-only.

----

.. _FontObject.nativeStyleName:

FontObject.nativeStyleName
*********************************************

``app.fonts.allFonts[0][0].nativeStyleName``

**Description**

The native style name of the font in full 16 bit Unicode. Often different than what is returned by :ref:`FontObject.styleName` for non-Latin fonts.

**Type**

String; read-only.

----

.. _FontObject.postScriptName:

FontObject.postScriptName
*********************************************

``app.fonts.allFonts[0][0].postScriptName``

**Description**

The postscript name of the font.

**Type**

String; read-only.

----

.. _FontObject.styleName:

FontObject.styleName
*********************************************

``app.fonts.allFonts[0][0].styleName``

**Description**

The style name of the font, in the ASCII character set.

**Type**

String; read-only.

----

.. _FontObject.technology:

FontObject.technology
*********************************************

``app.fonts.allFonts[0][0].technology``

**Description**

The technology used by the font.

**Type**

An ``CTFontTechnology`` enumerated value; read-only. One of:

-  ``CTFontTechnology.CT_TYPE1_FONT``
-  ``CTFontTechnology.CT_TRUETYPE_FONT``
-  ``CTFontTechnology.CT_CID_FONT``
-  ``CTFontTechnology.CT_BITMAP_FONT``
-  ``CTFontTechnology.CT_ATC_FONT``
-  ``CTFontTechnology.CT_TYPE3_FONT``
-  ``CTFontTechnology.CT_SVG_FONT``
-  ``CTFontTechnology.CT_ANYTECHNOLOGY``

----

.. _FontObject.type:

FontObject.type
*********************************************

``app.fonts.allFonts[0][0].type``

**Description**

The internal type of the font.

**Type**

An ``CTFontType`` enumerated value; read-only. One of:

-  ``CTFontType.CT_TYPE1_FONTTYPE``
-  ``CTFontType.CT_TRUETYPE_FONTTYPE``
-  ``CTFontType.CT_CID_FONTTYPE``
-  ``CTFontType.CT_ATC_FONTTYPE``
-  ``CTFontType.CT_BITMAP_FONTTYPE``
-  ``CTFontType.CT_OPENTYPE_CFF_FONTTYPE``
-  ``CTFontType.CT_OPENTYPE_CID_FONTTYPE``
-  ``CTFontType.CT_OPENTYPE_TT_FONTTYPE``
-  ``CTFontType.CT_TYPE3_FONTTYPE``
-  ``CTFontType.CT_SVG_FONTTYPE``

----

.. _FontObject.version:

FontObject.version
*********************************************

``app.fonts.allFonts[0][0].version``

**Description**

The version number of the font.

**Type**

String; read-only.

----

.. _FontObject.writingScripts:

FontObject.writingScripts
*********************************************

``app.fonts.allFonts[0][0].writingScripts``

**Description**

The supported character sets of the font.

**Type**

An array of ``CTScript`` enumerated value; read-only. One or more of:

-  ``CTScript.CT_ROMAN_SCRIPT``
-  ``CTScript.CT_JAPANESE_SCRIPT``
-  ``CTScript.CT_TRADITIONALCHINESE_SCRIPT``
-  ``CTScript.CT_KOREAN_SCRIPT``
-  ``CTScript.CT_ARABIC_SCRIPT``
-  ``CTScript.CT_HEBREW_SCRIPT``
-  ``CTScript.CT_GREEK_SCRIPT``
-  ``CTScript.CT_CYRILLIC_SCRIPT``
-  ``CTScript.CT_RIGHTLEFT_SCRIPT``
-  ``CTScript.CT_DEVANAGARI_SCRIPT``
-  ``CTScript.CT_GURMUKHI_SCRIPT``
-  ``CTScript.CT_GUJARATI_SCRIPT``
-  ``CTScript.CT_ORIYA_SCRIPT``
-  ``CTScript.CT_BENGALI_SCRIPT``
-  ``CTScript.CT_TAMIL_SCRIPT``
-  ``CTScript.CT_TELUGU_SCRIPT``
-  ``CTScript.CT_KANNADA_SCRIPT``
-  ``CTScript.CT_MALAYALAM_SCRIPT``
-  ``CTScript.CT_SINHALESE_SCRIPT``
-  ``CTScript.CT_BURMESE_SCRIPT``
-  ``CTScript.CT_KHMER_SCRIPT``
-  ``CTScript.CT_THAI_SCRIPT``
-  ``CTScript.CT_LAOTIAN_SCRIPT``
-  ``CTScript.CT_GEORGIAN_SCRIPT``
-  ``CTScript.CT_ARMENIAN_SCRIPT``
-  ``CTScript.CT_SIMPLIFIEDCHINESE_SCRIPT``
-  ``CTScript.CT_TIBETAN_SCRIPT``
-  ``CTScript.CT_MONGOLIAN_SCRIPT``
-  ``CTScript.CT_GEEZ_SCRIPT``
-  ``CTScript.CT_EASTEUROPEANROMAN_SCRIPT``
-  ``CTScript.CT_VIETNAMESE_SCRIPT``
-  ``CTScript.CT_EXTENDEDARABIC_SCRIPT``
-  ``CTScript.CT_KLINGON_SCRIPT``
-  ``CTScript.CT_EMOJI_SCRIPT``
-  ``CTScript.CT_ROHINGYA_SCRIPT``
-  ``CTScript.CT_JAVANESE_SCRIPT``
-  ``CTScript.CT_SUNDANESE_SCRIPT``
-  ``CTScript.CT_LONTARA_SCRIPT``
-  ``CTScript.CT_SYRIAC_SCRIPT``
-  ``CTScript.CT_TAITHAM_SCRIPT``
-  ``CTScript.CT_BUGINESE_SCRIPT``
-  ``CTScript.CT_BALINESE_SCRIPT``
-  ``CTScript.CT_CHEROKEE_SCRIPT``
-  ``CTScript.CT_MANDAIC_SCRIPT``
-  ``CTScript.CT_VAI_SCRIPT``
-  ``CTScript.CT_THAANA_SCRIPT``
-  ``CTScript.CT_BRAVANESE_SCRIPT``
-  ``CTScript.CT_BRAHMI_SCRIPT``
-  ``CTScript.CT_CARIAN_SCRIPT``
-  ``CTScript.CT_CYPRIOT_SCRIPT``
-  ``CTScript.CT_EGYPTIAN_SCRIPT``
-  ``CTScript.CT_IMPERIALARAMAIC_SCRIPT``
-  ``CTScript.CT_PAHLAVI_SCRIPT``
-  ``CTScript.CT_PARTHIAN_SCRIPT``
-  ``CTScript.CT_KHAROSHTHI_SCRIPT``
-  ``CTScript.CT_LYCIAN_SCRIPT``
-  ``CTScript.CT_LYDIAN_SCRIPT``
-  ``CTScript.CT_PHOENICIAN_SCRIPT``
-  ``CTScript.CT_PERSIAN_SCRIPT``
-  ``CTScript.CT_SHAVIAN_SCRIPT``
-  ``CTScript.CT_SUMAKKCUNEIFORM_SCRIPT``
-  ``CTScript.CT_UGARITIC_SCRIPT``
-  ``CTScript.CT_GLAGOLITIC_SCRIPT``
-  ``CTScript.CT_GOTHIC_SCRIPT``
-  ``CTScript.CT_OGHAM_SCRIPT``
-  ``CTScript.CT_OLDITALIC_SCRIPT``
-  ``CTScript.CT_ORKHON_SCRIPT``
-  ``CTScript.CT_RUNIC_SCRIPT``
-  ``CTScript.CT_MEROITICCURSIVE_SCRIPT``
-  ``CTScript.CT_COPTIC_SCRIPT``
-  ``CTScript.CT_OLCHIKI_SCRIPT``
-  ``CTScript.CT_SORASOMPENG_SCRIPT``
-  ``CTScript.CT_OLDHANGUL_SCRIPT``
-  ``CTScript.CT_LISU_SCRIPT``
-  ``CTScript.CT_NKO_SCRIPT``
-  ``CTScript.CT_ADLAM_SCRIPT``
-  ``CTScript.CT_BAMUM_SCRIPT``
-  ``CTScript.CT_BASSAVAH_SCRIPT``
-  ``CTScript.CT_NEWA_SCRIPT``
-  ``CTScript.CT_NEWTAILU_SCRIPT``
-  ``CTScript.CT_SCRIPT``
-  ``CTScript.CT_OSAGE_SCRIPT``
-  ``CTScript.CT_UCAS_SCRIPT``
-  ``CTScript.CT_TIFINAGH_SCRIPT``
-  ``CTScript.CT_KAYAHLI_SCRIPT``
-  ``CTScript.CT_LAO_SCRIPT``
-  ``CTScript.CT_TAILE_SCRIPT``
-  ``CTScript.CT_TAIVIET_SCRIPT``
-  ``CTScript.CT_DONTKNOW_SCRIPT``

=======
Methods
=======

.. _FontObject.hasSameDict:

FontObject.hasSameDict()
**********************************************

``app.fonts.fontsWithDefaultDesignAxes[0].hasSameDict(fontObject)``

**Description**

This function will true if the :ref:`FontObject` passed as an argument shares the same variable font dictionnary as the :ref:`FontObject` the function is called on.

.. note::
  Can only return true when called on a variable :ref:`FontObject` with the argument also being a :ref:`FontObject` of a variable font.

**Parameters**

====================  ========================================================
fontObject            A :ref:`FontObject`
====================  ========================================================

**Returns**

A Boolean.

----

.. _FontObject.postScriptNameForDesignVector:

FontObject.postScriptNameForDesignVector()
**********************************************

``app.fonts.fontsWithDefaultDesignAxes[0].postScriptNameForDesignVector([...vectorValues])``

**Description**

This function will return the postscript name of the variable font for the specific design vectors passed as the argument.

**Parameters**

====================  ===============================================================================================================
vectorValues          An array of float values that matches the length of :ref:`FontObject.designVector` for the given variable font.
====================  ===============================================================================================================

**Returns**

A String.
