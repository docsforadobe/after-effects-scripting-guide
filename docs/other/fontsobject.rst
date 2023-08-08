.. highlight:: javascript
.. _FontsObject:

Fonts object
################################################

``app.fonts``

**Description**

The Fonts objects provides information about the current font ecosystem on your device. It will allow you to retreive all the available fonts and iterate them.

.. note::
   | This functionality was added in After Effects 24.0.
   | This functionality is currently in Beta and is subject to change.

----

==========
Attributes
==========

.. _FontsObject.allFonts:

FontsObject.allFonts
*********************************************

``app.fonts.allFonts``

**Description**

The list of all the fonts currently available on your system.

They are grouped into what is named a family group which are Arrays of :ref:`fontobject`.

.. Naming and ordering::

The Family Name of the group is simply the :ref:`familyName <FontObject.familyName>` of any of the :ref:`Font objects<fontobject>` in the group.

The Family Name in one font group is not guaranteed to have unique name compared to different font groups - the grouping is determined by a number of factors including the returned value of :ref:`FontObject.technology` and :ref:`FontObject.writingScripts`.

In addition, it is perfectly acceptable to have multiple fonts with the same PostScript name, though only one will have the same (PostScript name, Technology, Primary Writing Script) tuple. In the case of true duplicates, it is undefined which will be returned and which will be suppressed.

The family groups and :ref:`Font objects <fontobject>` in the group are sorted accordingly to the setting in the Character Panel dropdown "Show Font Names in English". If set to true, the :ref:`familyName<FontObject.familyName>` and :ref:`styleName<FontObject.styleName>` property is used, otherwise the :ref:`nativeFamilyName<FontObject.nativeFamilyName>` and :ref:`nativeStyleName<FontObject.nativeStyleName>` property is used.

:ref:`fontobject` for which ``Font.isSubstitute`` returns true are always sorted to the end as individual family groups.


**Type**

Array of Arrays of :ref:`fontobject`; read-only.

**Example**

This example will select the first returned Font Family Array.

.. code:: javascript

   // Getting the first available Font Family Group on the system
   var firstFontGroup = app.fonts.allFonts[0];

   // Getting the first Style for that Font Family
   var firstFontFamilyName = firstFontGroup[0].familyName;
   var firstFamilyStyle = firstFontGroup[0].styleName;

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

Array of :ref:`fontobject`; read-only.

----

=======
Methods
=======

.. _FontsObject.getFontsByFamilyNameAndStyleName:

FontsObject.getFontsByFamilyNameAndStyleName()
**********************************************

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

An array of :ref:`fontobject`.

----

.. _FontsObject.getFontsByPostScriptName:

FontsObject.getFontsByPostScriptName()
**************************************

``app.fonts.getFontsByPostScriptName(postscriptName)``

**Description**

This function will return an array of :ref:`fontobject` based on the PostScript name of previously found Fonts. 

It is perfectly valid to have multiple :ref:`fontobject` which share the same PostScript name, the order of these is determined by the order in which they were enumerated in the font environment. It is the entry at ``[0]`` which is used when setting the :ref::`TextDocument` ``font`` property.

In addition, there is a special property of this API with regards to Variable fonts. If no :ref:`fontobject` matching the requested PostScript exists, but we find that there exist a Variable font which matches the requested PostScript name prefix, then this Variable font instance will be requested to create a matching :ref:`fontobject`. This is the only way that we will return an instance which did not exist prior to invoking this method.

If no matching Font is found, it will return an empty Array.

.. code:: javascript

   var fontList = app.fonts.getFontsByPostScriptName("Abolition")
   alert(fontList.length);

**Parameters**

====================  ========================================================
postscriptName          A string containing the PostScript Name of the font.
====================  ========================================================

**Returns**

An array of :ref:`fontobject`.
