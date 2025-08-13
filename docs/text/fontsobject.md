# Fonts object

`app.fonts`

!!! note
    This functionality was added in After Effects 24.0

#### Description

The Fonts objects provides information about the current font ecosystem on your device.

After Effects maintains an internal font proxy to a real font which it has enumerated in the font ecosystem. As the fonts in the font ecosystem are added and removed these internal font proxies are kept in sync as well by being added and removed.

The properties we report via the proxy [Font object](fontobject.md) are the data that is available to us from the font files themselves, which of course will vary according to technology and type of font. It is not possible here to describe all the possible interesting variations and troubles that this causes us and in general it is advisable to be careful with assuming that the behavior and properties for one font type or technology are common to all other font types and technology - the answer as always is "it depends".

A [Font object](fontobject.md) is a soft reference to one of these internal font proxies and as a consequence is not sufficient to keep the internal font proxy alive. As a result if the internal font proxy is removed, the referencing [Font object](fontobject.md) will throw an invalid exception for any property reference.

On project open, and a few other situations, it may come to pass that the font which is being referenced in the persisted data cannot be found in the current font ecosystem. In these situations an internal font proxy will be created which will contain the desired properties, such as PostScript name, and will return `true` for [isSubstitute](fontobject.md#fontobjectissubstitute). There will be an underlying real font which will be selected to support this internal font proxy, but we do not reveal what it is and there is no way to influence this selection.

Continuing the open process with created substitute fonts, an attempt will be made to sync matching fonts from Creative Cloud Adobe Fonts. This is an asynchronous activity and the project will usually finish opening and be ready for use before any fonts are brought down from Adobe Fonts. Depending on how many fonts are being synced, they may be installed at different times. There is no way to disable this attempt.

After any change to the font ecosystem from installing new real fonts, the outstanding list of substitute fonts will be evaluated to see if there now exists a real font which is a valid replacement for it - currently only requiring the PostScript name to match - and if one is found automatically all the references in the project to the substitute will be replaced with the newly installed font.

---

## Attributes

### FontsObject.allFonts

`app.fonts.allFonts`

#### Description

The list of all the fonts currently available on your system.

They are grouped into what is named a family group which are Arrays of [Font object](fontobject.md).

The Family Name of the group is simply the [familyName](fontobject.md#fontobjectfamilyname) of any of the [Font objects](fontobject.md) in the group.

The Family Name in one font group is not guaranteed to have unique name compared to different font groups - the grouping is determined by a number of factors including the returned value of [FontObject.technology](fontobject.md#fontobjecttechnology) and [FontObject.writingScripts](fontobject.md#fontobjectwritingscripts).

In addition, it is perfectly acceptable to have multiple fonts with the same PostScript name, though only one will have the same (PostScript name, Technology, Primary Writing Script) tuple. In the case of true duplicates, it is undefined which will be returned and which will be suppressed.

The family groups and [Font objects](fontobject.md) in the group are sorted according to the setting in the Character Panel dropdown "Show Font Names in English". If set to `true`, the [familyName](fontobject.md#fontobjectfamilyname) and [styleName](fontobject.md#fontobjectstylename) property is used, otherwise the [nativeFamilyName](fontobject.md#fontobjectnativefamilyname) and [nativeStyleName](fontobject.md#fontobjectnativestylename) property is used.

[Font object](fontobject.md) for which [isSubstitute](fontobject.md#fontobjectissubstitute) returns `true` are always sorted to the end as individual family groups.

#### Type

Array of Arrays of [Font objects](fontobject.md); read-only.

#### Example

This example will select the first returned Font Family Array.

```javascript
// Getting the first available Font Family Group on the system
var firstFontGroup = app.fonts.allFonts[0];

// Getting the first Style for that Font Family
var firstFontFamilyName = firstFontGroup[0].familyName;
var firstFamilyStyle = firstFontGroup[0].styleName;

alert(firstFontFamilyName+" "+firstFamilyStyle);
```

---

### FontsObject.favoriteFontFamilyList

`app.fonts.favoriteFontFamilyList`

!!! note
    This functionality was added in After Effects 24.6

#### Description

Provides access to the Favorites list presented in the Character panel and Properties panel. To set the Favorites simply provide an (unsorted) array of strings based on the [familyName](fontobject.md#fontobjectfamilyname). To clear the list simply assign an empty Array.

#### Type

Array of Strings; read/write.

---

### FontsObject.fontsDuplicateByPostScriptName

`app.fonts.fontsDuplicateByPostScriptName`

!!! note
    This functionality was added in After Effects 24.6

#### Description

It is perfectly legal and common for more than one [Font object](fontobject.md) to return the same value for [postScriptName](fontobject.md#fontobjectpostscriptname) but as this can sometimes lead to confusion about what [Font object](fontobject.md) will actually be used when using [TextDocument.font](textdocument.md#textdocumentfont) or the `.font` attribute of a [CharacterRange object](characterrange.md), this property exists to both reveal what duplicates exist and also their relative order.

This returns an Array in which each element is an Array of [Font objects](fontobject.md), where the 0th element [Font object](fontobject.md) is considered the primary [Font object](fontobject.md) for the given PostScript name.

#### Type

Array of Arrays of [Font Objects](fontobject.md); read-only.

---

### FontsObject.fontServerRevision

`app.fonts.fontServerRevision`

!!! note
    This functionality was added in After Effects 24.2

#### Description

Returns an unsigned number representing the current revision of the font environment.

The revision is advanced when anything happens to the font environment which would change the contents, properties, or order of [Font objects](fontobject.md) returned from a call to [FontsObject.allFonts](#fontsobjectallfonts).

Among these are: installing or removing fonts in the font environment, opening or closing a project with substituted fonts, causing a custom Variable font instance to be created, and changing the setting in the Character Panel dropdown "Show Font Names in English".

#### Type

Floating-point value; read-only.

#### Example

```javascript
var fsRev = app.fonts.fontServerRevision;
alert(fsRev);
```

---

### FontsObject.fontsWithDefaultDesignAxes

`app.fonts.fontsWithDefaultDesignAxes`

#### Description

Returns an array of variable [Font objects](fontobject.md), each using a unique font dictionary and with default values for their design axes. This API is a convenient way to quickly filter for a unique instance of each installed variable font.

#### Type

Array of [Font objects](fontobject.md); read-only.

#### Example

```javascript
var variableFontList = app.fonts.fontsWithDefaultDesignAxes;
alert(variableFontList.length);
```

---

### FontsObject.freezeSyncSubstitutedFonts

`app.fonts.freezeSyncSubstitutedFonts`

!!! note
    This functionality was added in After Effects 24.6

#### Description

When a Project is opened and one or more fonts are not found in the local font environment, a *sync* process is initiated with Adobe Fonts to see if one or more Fonts could be activated and installed.

By default this happens automatically—this property will disable it from happening.

!!! warning
    The rules for deciding if Adobe Fonts has a matching font is entirely based on the PostScript name. With some Variable Fonts, due to ambiguity about which font has which named instance, it is possible that more than one face (Regular/Italic) may be installed during an activation. Whether the installed font is a valid replacement is controlled by the [FontsObject.substitutedFontReplacementMatchPolicy](#fontsobjectsubstitutedfontreplacementmatchpolicy).

#### Type

Boolean; read/write. One of:

- `false` is the default—sync from Adobe Fonts may be attempted.
- `true` means that no sync or install will be attempted.

---

### FontsObject.missingOrSubstitutedFonts

`app.fonts.missingOrSubstitutedFonts`

#### Description

The list of all the missing or substituted fonts of the current Project.

!!! tip
    A substituted font is a font that was already missing when the project is opened. A missing font is a font that went missing (font being uninstalled, for example) *while* the project was open.

#### Type

Array of [Font objects](fontobject.md); read-only.

---

### FontsObject.mruFontFamilyList

`app.fonts.mruFontFamilyList`

!!! note
    This functionality was added in After Effects 24.6

#### Description

Provides access to the Most Recently Used (MRU) list presented in the Character panel and Properties panel. To set the MRU simply provide an (unsorted) array of strings based on the [familyName](fontobject.md#fontobjectfamilyname). To clear the list simply assign an empty Array.

#### Type

Array of Strings; read/write.

---

### FontsObject.substitutedFontReplacementMatchPolicy

`app.fonts.substitutedFontReplacementMatchPolicy`

!!! note
    This functionality was added in After Effects 24.6

#### Description

Controls the rules which are used to determine which fonts are considered matching for automatic replacement for a substituted [Font object](fontobject.md).

#### Type

A `SubstitutedFontReplacementMatchPolicy` enumerated value; read/write. One of:

- `SubstitutedFontReplacementMatchPolicy.POSTSCRIPT_NAME` is the default; any [Font object](fontobject.md) which has the same PostScript name is a valid candidate for replacement of a substituted [Font object](fontobject.md).
- `SubstitutedFontReplacementMatchPolicy.CTFI_EQUAL` requires that the following properties of substituted [Font object](fontobject.md) must match to be considered a valid candidate:
    - [postScriptName](fontobject.md#fontobjectpostscriptname)
    - [technology](fontobject.md#fontobjecttechnology)
    - [writingScripts](fontobject.md#fontobjectwritingscripts) (primary)
    - [designVector](fontobject.md#fontobjectdesignvector)
- `SubstitutedFontReplacementMatchPolicy.DISABLED` means that no [Font object](fontobject.md) is an acceptable replacement for a the substituted [Font object](fontobject.md).

---

## Methods

### FontsObject.getCTScriptForString()

`app.fonts.getCTScriptForString(charString, preferredCTScript)`

!!! note
    This functionality was added in After Effects 25.1

#### Description

This function will return an array of generic objects describing the number of characters in the range and the `CTScript` enum assigned to them. See [FontObject.writingScripts](fontobject.md#fontobjectwritingscripts) for a full list of `CTScript` enumerated values.

If a character is deemed to be included in one or more `CTScript` values, the value specfied in the second argument `preferredCTScript` will break the tie.

```javascript
var scriptsV = app.fonts.getCTScriptForString("ABヂ", CTScript.CT_ROMAN_SCRIPT);
var str = "[0] chars:" + scriptsV[0].chars +   // 2
            " ctScript:" + getEnumAsString(scriptsV[0].ctScript) +
            "\n[1] chars:" + scriptsV[1].chars + // 1
            " ctScript:" + getEnumAsString(scriptsV[1].ctScript);
alert(str);
```

#### Parameters

|      Parameter      |      Type       |                        Description                         |
| ------------------- | --------------- | ---------------------------------------------------------- |
| `charString`        | String          | Characters to check. If empty, will return an empty array. |
| `preferredCTScript` | `CTScript` enum | CT Script to prefer                                        |

#### Returns

Array of generic objects;

- Key `chars` will be set to number of characters the in the range.
- Key `ctScript` will be set to the `CTScript` which applies to the characters in the range.

—

### FontsObject.getDefaultFontForCTScript()

`app.fonts.getDefaultFontForCTScript(ctScript)`

!!! note
    This functionality was added in After Effects 25.1

#### Description

This function will return an instance of [Font object](fontobject.md) mapped as the default font based on `CTScript`.

After Effects uses these mappings when typing or applying a font where it finds
that the font does not contain a glyph for the character.
In this situation it will attempt to map the character to a `CTScript` value
and then use this default mapping to select an alternate font which may have a
glyph for the character.

This mechanism is also used with text and fonts in Scripting thus providing a way
to expose which fonts will be used for which `CTScript` values.

There is no guarantee that what is returned will support all, or even any, of the
Unicode characters mapped to the `CTScript`.

```javascript
var font = app.fonts.getDefaultFontForCTScript(CTScript.CT_JAPANESE_SCRIPT);
```

#### Parameters

| Parameter  |      Type       |                   Description                    |
| ---------- | --------------- | ------------------------------------------------ |
| `ctScript` | `CTScript` enum | Corresponding CTScript to get default font from. |

#### Returns

[Font object](fontobject.md)

---

### FontsObject.getFontByID()

`app.fonts.getFontByID(fontID)`

!!! note
    This functionality was added in After Effects 24.2

#### Description

This function will return an instance of [Font object](fontobject.md) based on the ID of a previously found font.

If no matching font is found, it will return undefined. This can occur with an unknown ID or if the original font has been removed from the font environment.

```javascript
var font1 = app.fonts.allFonts[0][0];
var font2 = app.fonts.getFontByID(font1.fontID);
alert(font1.fontID == font2.fontID);
```

#### Parameters

| Parameter |  Type   |     Description     |
| --------- | ------- | ------------------- |
| fontID    | Integer | The ID of the font. |

#### Returns

[Font object](fontobject.md), or undefined if no font by that ID.

---

### FontsObject.getFontsByFamilyNameAndStyleName()

`app.fonts.getFontsByFamilyNameAndStyleName(familyName, styleName)`

#### Description

This function will return an array of [Font object](fontobject.md) based on the Family Name and Style Name of a font. If no suitable font is found, it will return an empty Array.

!!! tip
    The returned array length can be more than 1 if you have multiple copies of a same font.

```javascript
var fontList = app.fonts.getFontsByFamilyNameAndStyleName("Abolition", "Regular")
alert(fontList.length);
```

#### Parameters

| Parameter  |  Type  |         Description          |
| ---------- | ------ | ---------------------------- |
| FamilyName | String | The Family Name of the font. |
| StyleName  | String | The Style Name of the font.  |

#### Returns

Array of [Font objects](fontobject.md); read-only.

---

### FontsObject.getFontsByPostScriptName()

`app.fonts.getFontsByPostScriptName(postscriptName)`

#### Description

This function will return an array of [Font objects](fontobject.md) based on the PostScript name of previously found Fonts.

It is perfectly valid to have multiple [Font objects](fontobject.md) which share the same PostScript name, the order of these is determined by the order in which they were enumerated in the font environment. The entry at `[0]` will be used when setting the [TextDocument.fontObject](textdocument.md#textdocumentfontobject) property.

In addition, there is a special property of this API with regards to Variable fonts. If no [Font object](fontobject.md) matching the requested PostScript exists, but we find that there exist a variable font which matches the requested PostScript name prefix, then this Variable font instance will be requested to create a matching [Font object](fontobject.md). This is the only way that we will return an instance which did not exist prior to invoking this method.

If no matching font is found, it will return an empty Array.

```javascript
var fontList = app.fonts.getFontsByPostScriptName("Abolition")
alert(fontList.length);
```

#### Parameters

|   Parameter    |  Type  |           Description            |
| -------------- | ------ | -------------------------------- |
| postscriptName | String | The PostScript Name of the font. |

#### Returns

Array of [Font objects](fontobject.md); read-only.

---

### FontsObject.pollForAndPushNonSystemFontFoldersChanges()

`app.fonts.pollForAndPushNonSystemFontFoldersChanges()`

!!! note
    This functionality was added in After Effects 24.6

#### Description

The addition and removal of font files in what is considered the *system font folders* is recognized and handled automatically without user intervention to update the font environment. Non-system font folders are not automatically handled and so additions and removal of font files in these folders are not recognized until the After Effects is restarted.

This function will trigger a check against the known non-system font folders, and if it is recognized that there has been a change, an asynchronous update to the font environment will be scheduled to process this change.

The non-system font folders After Effects knows about are here:

```text
Windows: <systemDrive>:\Program Files\Common Files\Adobe\Fonts

Mac: /Library/Application Support/Adobe/Fonts
```

#### Returns

Boolean; One of:

- `false` if no changes to the font environment are known.
- `true` if a change in the font environment has been detected and an asynchronous update scheduled to deal with it. This state will be cleared once the update has been processed, at which time [FontsObject.fontServerRevision](#fontsobjectfontserverrevision) will return an incremented value.

—

### FontsObject.setDefaultFontForCTScript()

`app.fonts.setDefaultFontForCTScript(ctScript, font)`

!!! note
    This functionality was added in After Effects 25.1

#### Description

This function will set an instance of [Font object](fontobject.md) mapped based on `CTScript` parameter.

After Effects uses these mappings when typing or applying a font where it finds
that the font does not contain a glyph for a given character.
In this situation it will attempt to map the character to a `CTScript` value
and then use this default mapping to select an alternate font which may have a glyph
for the character.

Variable fonts are not acceptable as defaults and will result in an exception being thrown.

There is no requirement that the specfied font has glyphs for any or all of the characters
mapped to the `CTScript`.

This mechanism is also used with text and fonts in Scripting thus providing a way
to expose which fonts will be used for which `CTScript` values (see [FontsObject.getDefaultFontForCTScript()](#fontsobjectgetdefaultfontforctscript)).

The font assigned to the `CTScript.CT_ROMAN_SCRIPT` is the one which is used to re-initialize the Character Panel after resetting the character style.

To reset the default for a specific `CTScript` back to the value it had at App launch, simply pass in `null`.

```javascript
var font = app.fonts.getFontsByPostScriptName("MyriadPro-Regular")[0];
var ret = app.fonts.setDefaultFontForCTScript(CTScript.CT_ROMAN_SCRIPT, font);
alert("set:" + ret);
```

#### Parameters

| Parameter  |             Type             |                           Description                            |
| ---------- | ---------------------------- | ---------------------------------------------------------------- |
| `ctScript` | `CTScript` enum              | CTScript for font to be mapped                                   |
| `font`     | [Font object](fontobject.md) | The font to be mapped. If `null`, then current mapping is reset. |

#### Returns

Boolean; One of:

- `false` if the specfied mapping is the same the current one.
- `true` if the specified mapping is different from the current one.
