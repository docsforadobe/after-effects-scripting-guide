<a id="preferences"></a>

# Preferences object

`app.preferences`

**Description**

The Preferences object provides an easy way to manage internal AE preferences, such as you’d find in AE’s Preferences menu. These are saved in the After Effects preference files, and are persistent between application sessions.

Preferences are identified by section and key within the file, and each key name is associated with a value.

In the preferences file, section names are enclosed in brackets and quotation marks, and key names are listing in quotation marks below the sectionname. All values are strings.

You can create new preferences with this object, as well as accessing existing preferences.

As of Version 12/CC, preferences and settings methods now take a third argument to specify the target preferences file if Section/Key is not in “Adobe After Effects $versionNumber.x Prefs.txt”.

If the third argument is not passed, default value (`PREFType.PREF_Type_MACHINE_SPECIFIC`) is used and After Effects tries to save/get from the “Adobe After Effects $versionNumber.x Prefs.txt” preferences file.

The third argument is enum `PREFType` value, one of:

- `PREF_Type_MACHINE_SPECIFIC`: Adobe After Effects $versionNumber.x Prefs.txt
- `PREF_Type_MACHINE_INDEPENDENT`: Adobe After Effects $versionNumber.x Prefs-indep-general.txt
- `PREF_Type_MACHINE_INDEPENDENT_RENDER`: Adobe After Effects $versionNumber.x Prefs-indep-render.txt
- `PREF_Type_MACHINE_INDEPENDENT_OUTPUT`: Adobe After Effects $versionNumber.x Prefs-indep-output.txt
- `PREF_Type_MACHINE_INDEPENDENT_COMPOSITION`: Adobe After Effects $versionNumber.x Prefs-indep-composition.txt
- `PREF_Type_MACHINE_SPECIFIC_TEXT`: Adobe After Effects $versionNumber.x Prefs-text.txt
- `PREF_Type_MACHINE_SPECIFIC_PAINT`: Adobe After Effects $versionNumber.x Prefs-paint.txt

---

## Methods

<a id="preferences-deletepref"></a>

### Preferences.deletePref()

`app.preferences.deletePref(sectionName, keyName[, prefType])`

**Description**

Deletes a preference from the preference file.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Nothing.

**Example**

If you have saved a setting named with the key name “trimPrecomps” in a section called “Precomp Cropper”, you can delete the setting by:

```javascript
app.preferences.deletePref("Settings_Precomp Cropper", "trimPrecomps");
```

---

<a id="preferences-getprefasbool"></a>

### Preferences.getPrefAsBool()

`app.preferences.getPrefAsBool(sectionName, keyName[, prefType])`

**Description**

Retrieves a preference value from the preferences file, and parses it as a boolean.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Boolean.

**Example**

To retrieve the value of the Flow Chart “Expand Flowchart Comps by Default” preference:

```javascript
var expandByDefault = app.preferences.getPrefAsBool("Flowchart Settings", "Expand Flowchart Comps by Default");
alert("The setting is: " + expandByDefault);
```

To retrieve the value of the main preference “Javascript Debugger Enabled”:

```javascript
var debuggerEnabled = app.preferences.getPrefAsBool("Main Pref Section v2", "Pref_JAVASCRIPT_DEBUGGER", PREFType.PREF_Type_MACHINE_INDEPENDENT);
alert("The setting is: " + debuggerEnabled);
```

---

<a id="preferences-getprefasfloat"></a>

### Preferences.getPrefAsFloat()

`app.preferences.getPrefAsFloat(sectionName, keyName[, prefType])`

**Description**

Retrieves a preference value from the preferences file, and parses it as a float.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Float.

---

<a id="preferences-getprefaslong"></a>

### Preferences.getPrefAsLong()

`app.preferences.getPrefAsLong(sectionName, keyName[, prefType])`

**Description**

Retrieves a preference value from the preferences file, and parses it as a long (number).

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Long.

---

<a id="preferences-getprefasstring"></a>

### Preferences.getPrefAsString()

`app.preferences.getPrefAsString(sectionName, keyName[, prefType])`

**Description**

Retrieves a preference value from the preferences file, and parses it as a string.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

String.

---

<a id="preferences-havepref"></a>

### Preferences.havePref()

`app.preferences.havePref(sectionName, keyName[, prefType])`

**Description**

Returns true if the specified preference item exists and has a value.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Boolean.

---

<a id="preferences-reload"></a>

### Preferences.reload()

`app.preferences.reload()`

**Description**

Reloads the preferences file manually. Otherwise, changes to preferences will only be accessible by scripting after an application restart.

**Parameters**

None.

**Returns**

Nothing.

---

<a id="preferences-saveprefasbool"></a>

### Preferences.savePrefAsBool()

`app.preferences.savePrefAsBool(sectionName, keyName, value[, prefType])`

**Description**

Saves a preference item as a boolean.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `value`         | A boolean containing the new value                        |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Nothing.

---

<a id="preferences-saveprefasfloat"></a>

### Preferences.savePrefAsFloat()

`app.preferences.savePrefAsFloat(sectionName, keyName, value[, prefType])`

**Description**

Saves a preference item as a float.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `value`         | A float containing the new value                          |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Nothing.

---

<a id="preferences-saveprefaslong"></a>

### Preferences.savePrefAsLong()

`app.preferences.savePrefAsLong(sectionName, keyName, value[, prefType])`

**Description**

Saves a preference item as a long.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `value`         | A long containing the new value                           |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Nothing.

---

<a id="preferences-saveprefasstring"></a>

### Preferences.savePrefAsString()

`app.preferences.savePrefAsString(sectionName, keyName, value[, prefType])`

**Description**

Saves a preference item as a string.

**Parameters**

| `sectionName`   | A string containing the name of a preferences section     |
|-----------------|-----------------------------------------------------------|
| `keyName`       | A string containing the key name of the preference        |
| `value`         | A string containing the new value                         |
| `prefType`      | Optional, an enum indicating which preference file to use |

**Returns**

Nothing.

---

<a id="preferences-savetodisk"></a>

### Preferences.saveToDisk()

`app.preferences.saveToDisk()`

**Description**

Saves the preferences to disk manually. Otherwise, changes to preferences will only be accessible by scripting after an application restart.

**Parameters**

None.

**Returns**

Nothing.
