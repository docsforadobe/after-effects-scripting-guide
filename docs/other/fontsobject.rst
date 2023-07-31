.. highlight:: javascript
.. _FontsObject:

Fonts object
################################################

``app.fonts``

**Description**

The Fonts objects provides information about the current font ecosystem on your device. It will allow you to retreive all the available fonts and iterate them.

.. note::
   This functionality was added in After Effects 24.0
   This functionality is currently in Beta and is subject to change.

----

==========
Attributes
==========

.. _FontsObject.allFonts:

FontsObject.allFonts
*********************************************

``app.fonts.allFonts``

**Description**

The list of all the fonts currently available on your system, sorted by Font Family.

**Type**

Array of Arrays; read-only.

**Example**

This example will select the first returned Font Family Array.

.. code:: javascript

   // Getting the first available Font Family on the system
   var firstFont = app.fonts.allFonts[0];

   // Getting the first Style for that Font Family
   var firstFontFamilyName = firstFont[0].familyName;
   var firstFamilyStyle = firstFont[0].styleName;

   alert(firstFontFamilyName+" "+firstFamilyStyle);


----

.. _FontsObject.missingOrSubstituedFonts:

FontsObject.missingOrSubstitutedFonts
*********************************************

``app.fonts.missingOrSubstitutedFonts``

**Description**

The list of all the missing or substituted fonts of the current Project.

.. note::
   A substituted font is a font that was already missing when the project is opened.
   A missing font is a font that went missing (font being uninstalled, for example) while to project was open


**Type**

Array of fontObjects; read-only.

----

=======
Methods
=======

.. _FontsObject.getFontsByFamilyNameAndStyleName:

FontsObject.getFontsByFamilyNameAndStyleName()
*******************

``app.fonts.getFontsByFamilyNameAndStyleName(familyName, styleName)``

**Description**

This function will return an array of :ref:`fontobject` based on the Family Name and Style Name of a Font. If no suitable Font is found, it will return an empty Array.

.. note::
   The returned array length can be more than 1 if you have multiple copies of a same font.

.. code:: javascript

   var fontList = app.fonts.getFontsByFamilyNameAndStyleName("Abolition", "Regular")
   alert(fontList.length);

**Parameters**

====================  ========================================================
FamilyName              A string containing the Family Name of the font.
StyleName               A string containing the Style Name of the font.
====================  ========================================================

**Returns**

An array of fontObjects.

----

.. _FontsObject.getFontsByPostScriptName:

FontsObject.getFontsByPostScriptName()
*******************

``app.fonts.getFontsByPostScriptName(postscriptName)``

**Description**

This function will return an array of :ref:`fontobject` based on the Postscript name of a Font. If no suitable Font is found, it will return an empty Array.

.. note::
   The returned array length can be more than 1 if you have multiple copies of a same font.

.. code:: javascript

   var fontList = app.fonts.getFontsByPostScriptName("Abolition")
   alert(fontList.length);

**Parameters**

====================  ========================================================
postscriptName          A string containing the Postscript Name of the font.
====================  ========================================================

**Returns**

An array of fontObjects.