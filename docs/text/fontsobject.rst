.. highlight:: javascript
.. _FontsObject:

Fonts object
################################################

``app.fonts``

.. note::
   This functionality was added in After Effects 24.0.

**Description**

The Fonts objects provides information about the current font ecosystem on your device.

After Effects maintains an internal font proxy to a real font which it has enumerated in the font ecosystem. As the fonts in the font ecosystem are added and removed these internal font proxies are kept in sync as well by being added and removed.

The properties we report via the proxy :ref:`fontobject` are the data that is available to us from the font files themselves, which of course will vary according to technology and type of font. It is not possible here to describe all the possible interesting variations and troubles that this causes us and in general it is advisable to be careful with assuming that the behavior and properties for one font type or technology are common to all other font types and technology - the answer as always is "it depends".


A :ref:`fontobject` is a soft reference to one of these internal font proxies and as a consequence is not sufficient to keep the internal font proxy alive. As a result if the internal font proxy is removed, the referencing :ref:`fontobject` will throw an invalid exception for any property reference.


On project open, and a few other situations, it may come to pass that the font which is being referenced in the persisted data cannot be found in the current font ecosystem. In these situations an internal font proxy will be created which will contain the desired properties, such as PostScript name, and will return true for :ref:`isSubstitute <FontObject.isSubstitute>`. There will be an underlying real font which will be selected to support this internal font proxy, but we do not reveal what it is and there is no way to influence this selection.


Continuing the open process with created substitute fonts, an attempt will be made to sync matching fonts from Creative Cloud Adobe Fonts. This is an asynchronous activity and the project will usually finish opening and be ready for use before any fonts are brought down from Adobe Fonts. Depending on how many fonts are being synced, they may be installed at different times. There is no way to disable this attempt.

After any change to the font ecosystem from installing new real fonts, the outstanding list of substitute fonts will be evaluated to see if there now exists a real font which is a valid replacement for it - currently only requiring the PostScript name to match - and if one is found automatically all the references in the project to the substitute will be replaced with the newly installed font.

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

The family groups and :ref:`Font objects <fontobject>` in the group are sorted according to the setting in the Character Panel dropdown "Show Font Names in English". If set to true, the :ref:`familyName<FontObject.familyName>` and :ref:`styleName<FontObject.styleName>` property is used, otherwise the :ref:`nativeFamilyName<FontObject.nativeFamilyName>` and :ref:`nativeStyleName<FontObject.nativeStyleName>` property is used.

:ref:`fontobject` for which :ref:`isSubstitute <FontObject.isSubstitute>` returns true are always sorted to the end as individual family groups.


**Type**

Array of Arrays of :ref:`Font objects <fontobject>`; read-only.

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

.. _FontsObject.favoriteFontFamilyList:

FontsObject.favoriteFontFamilyList
*********************************************

``app.fonts.favoriteFontFamilyList``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

Provides access to the Favorites list presented in the Character panel and Properties panel. To set the Favorites simply provide an (unsorted) array of strings based on the :ref:`familyName <FontObject.familyName>`. To clear the list simply assign an empty Array.

**Type**

Array of Strings; read/write.
    
----

.. _FontsObject.fontsDuplicateByPostScriptName:

FontsObject.fontsDuplicateByPostScriptName
*********************************************

``app.fonts.fontsDuplicateByPostScriptName``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

It is perfectly legal and common for more than one :ref:`fontobject` to return the same value for :ref:`postScriptName<FontObject.postScriptName>` but as this can sometimes lead to confusion about what :ref:`fontobject` will actually be used when using :ref:`TextDocument.font` or the ``.font`` attribute of a :ref:`CharacterRange object<CharacterRange>`, this property exists to both reveal what duplicates exist and also their relative order.

This an Array in which each element is an Array of :ref:`Font objects<FontObject>`, where the 0th element :ref:`fontobject` is considered the primary :ref:`fontobject` for the given PostScript name.

**Type**

Array of Arrays of :ref:`fontobject`; read-only.
    
----

.. _FontsObject.fontServerRevision:

FontsObject.fontServerRevision
**********************************************

``app.fonts.fontServerRevision``

.. note::
   This functionality was added in After Effects 24.2.

**Description**

Returns an unsigned number representing the current revision of the font environment.

The revision is advanced when anything happens to the font environment which would change the contents, properties, or order of :ref:`Font objects<FontObject>` returned from a call to :ref:`FontsObject.allFonts`.

Among these are: installing or removing fonts in the font environment, opening or closing a project with substituted fonts, causing a custom Variable font instance to be created, and changing the setting in the Character Panel dropdown "Show Font Names in English".

**Type**

Number; read-only.

**Example**

.. code:: javascript

   var fsRev = app.fonts.fontServerRevision;
   alert(fsRev);

----

.. _FontsObject.fontsWithDefaultDesignAxes:

FontsObject.fontsWithDefaultDesignAxes
**********************************************

``app.fonts.fontsWithDefaultDesignAxes``

**Description**

Returns an array of variable :ref:`Font objects<FontObject>`, each using a unique font dictionary and with default values for their design axes. This API is a convenient way to quickly filter for a unique instance of each installed variable font.

**Type**

Array of :ref:`Font objects<FontObject>`; read-only.

**Example**

.. code:: javascript

   var variableFontList = app.fonts.fontsWithDefaultDesignAxes;
   alert(variableFontList.length);

----

.. _FontsObject.freezeSyncSubstitutedFonts:

FontsObject.freezeSyncSubstitutedFonts
*********************************************

``app.fonts.freezeSyncSubstitutedFonts``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

When a Project is opened and one or more fonts are not found in the local font environment, a *sync* process is initiated with Adobe Fonts to see if one or more Fonts could be activated and installed.

By default this happens automatically—this property will disable it from happening.

.. warning::
   The rules for deciding if Adobe Fonts has a matching font is entirely based on the PostScript name. With some Variable Fonts, due to ambiguity about which font has which named instance, it is possible that more than one face (Regular/Italic) may be installed during an activation. Whether the installed font is a valid replacement is controlled by the :ref:`FontsObject.substitutedFontReplacementMatchPolicy`.

**Type**

Boolean; read/write. One of:

   - ``false`` is the default—sync from Adobe Fonts may be attempted.
   - ``true`` means that no sync or install will be attempted.

----

.. _FontsObject.missingOrSubstitutedFonts:

FontsObject.missingOrSubstitutedFonts
*********************************************

``app.fonts.missingOrSubstitutedFonts``

**Description**

The list of all the missing or substituted fonts of the current Project.

.. note::
   A substituted font is a font that was already missing when the project is opened. A missing font is a font that went missing (font being uninstalled, for example) *while* the project was open.


**Type**

Array of :ref:`Font objects<fontobject>`; read-only.

----

.. _FontsObject.mruFontFamilyList:

FontsObject.mruFontFamilyList
*****************************

``app.fonts.mruFontFamilyList``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

Provides access to the Most Recently Used (MRU) list presented in the Character panel and Properties panel. To set the MRU simply provide an (unsorted) array of strings based on the :ref:`familyName <FontObject.familyName>`. To clear the list simply assign an empty Array.

**Type**

Array of Strings; read/write. 
    
----

.. _FontsObject.substitutedFontReplacementMatchPolicy:

FontsObject.substitutedFontReplacementMatchPolicy
*************************************************

``app.fonts.substitutedFontReplacementMatchPolicy``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

Controls the rules which are used to determine which fonts are considered matching for automatic replacement for a substituted :ref:`fontobject`.

**Type**

A ``SubstitutedFontReplacementMatchPolicy`` enumerated value; read/write. One of:
    
- ``SubstitutedFontReplacementMatchPolicy.POSTSCRIPT_NAME`` is the default; any :ref:`fontobject` which has the same PostScript name is a valid candidate for replacement of a substituted :ref:`fontobject`.
- ``SubstitutedFontReplacementMatchPolicy.CTFI_EQUAL`` requires that the following properties of substituted :ref:`fontobject` must match to be considered a valid candidate:

   - :ref:`postScriptName<FontObject.postScriptName>`
   - :ref:`technology<FontObject.technology>`
   - :ref:`writingScripts<FontObject.writingScripts>` (primary)
   - :ref:`designVector<FontObject.designVector>`
- ``SubstitutedFontReplacementMatchPolicy.DISABLED`` means that no :ref:`fontobject` is an acceptable replacement for a the substituted :ref:`fontobject`.

----

=======
Methods
=======

.. _FontsObject.getFontByID:

FontsObject.getFontByID()
**************************************

``app.fonts.getFontByID(fontID)``

.. note::
   This functionality was added in After Effects 24.2.

**Description**

This function will return an instance of :ref:`Font object<fontobject>` based on the ID of a previously found font. 

If no matching font is found, it will return undefined. This can occur with an unknown ID or if the original font has been removed from the font environment.

.. code:: javascript

   var font1 = app.fonts.allFonts[0][0];
   var font2 = app.fonts.getFontByID(font1.fontID);
   alert(font1.fontID == font2.fontID);

**Parameters**

====================  ========================================================
fontID                  A number containing the ID of the font.
====================  ========================================================

**Returns**

:ref:`Font object<fontobject>`, or undefined if no font by that ID.

-----

.. _FontsObject.getFontsByFamilyNameAndStyleName:

FontsObject.getFontsByFamilyNameAndStyleName()
**********************************************

``app.fonts.getFontsByFamilyNameAndStyleName(familyName, styleName)``

**Description**

This function will return an array of :ref:`fontobject` based on the Family Name and Style Name of a font. If no suitable font is found, it will return an empty Array.

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

Array of :ref:`Font objects<fontobject>`; read-only.

----

.. _FontsObject.getFontsByPostScriptName:

FontsObject.getFontsByPostScriptName()
**************************************

``app.fonts.getFontsByPostScriptName(postscriptName)``

**Description**

This function will return an array of :ref:`Font objects<fontobject>` based on the PostScript name of previously found Fonts. 

It is perfectly valid to have multiple :ref:`Font objects<fontobject>` which share the same PostScript name, the order of these is determined by the order in which they were enumerated in the font environment. The entry at ``[0]`` will be used when setting the :ref:`TextDocument.fontObject` property.

In addition, there is a special property of this API with regards to Variable fonts. If no :ref:`fontobject` matching the requested PostScript exists, but we find that there exist a variable font which matches the requested PostScript name prefix, then this Variable font instance will be requested to create a matching :ref:`fontobject`. This is the only way that we will return an instance which did not exist prior to invoking this method.

If no matching font is found, it will return an empty Array.

.. code:: javascript

   var fontList = app.fonts.getFontsByPostScriptName("Abolition")
   alert(fontList.length);

**Parameters**

====================  ========================================================
postscriptName          A string containing the PostScript Name of the font.
====================  ========================================================

**Returns**

Array of :ref:`Font objects<fontobject>`; read-only.

----

.. _FontsObject.pollForAndPushNonSystemFontFoldersChanges:

FontsObject.pollForAndPushNonSystemFontFoldersChanges()
*******************************************************

``app.fonts.pollForAndPushNonSystemFontFoldersChanges()``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and subject to change while it remains in Beta.

**Description**

The addition and removal of font files in what is considered the *system font folders* is recognized and handled automatically without user intervention to update the font environment. Non-system font folders are not automatically handled and so additions and removal of font files in these folders are not recognized until the After Effects is restarted.

This function will trigger a check against the known non-system font folders, and if it is recognized that there has been a change, an asynchronous update to the font environment will be scheduled to process this change.

The non-system font folders After Effects knows about are here:

.. code-block:: text

   Windows: <systemDrive>:\Program Files\Common Files\Adobe\Fonts

   Mac: /Library/Application Support/Adobe/Fonts

**Returns**

Boolean; One of:

- ``false`` if no changes to the font environment are known.

- ``true`` if a change in the font environment has been detected and an asynchronous update scheduled to deal with it. This state will be cleared once the update has been processed, at which time :ref:`FontsObject.fontServerRevision` will return an incremented value.
