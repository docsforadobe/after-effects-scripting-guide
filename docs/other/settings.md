# Settings object

`app.settings`

#### Description

The Settings object provides an easy way to manage settings for third-party scripts. The settings are saved in the main After Effects preferences file, and are persistent between application sessions.

Settings are identified by section and key within the file, and each key name is associated with a value.

In the settings file, section names are enclosed in brackets and quotation marks, and key names are listing in quotation marks below the sectionname. All values are strings.

You can create new settings with this object, as well as accessing existing settings.

As of Version 12/CC, preferences and settings methods now take a third argument to specify the target preferences file if Section/Key is not in the main preferences file. See [Preferences object](preferences.md) for more info.

!!! tip
    - These values aren't shared between versions of AE; each new install brings new settings files, and so these prefs won't carry over.
    - Internally, all saved settings have their section name preprended with `"Settings_"`
    - If you're looking to get or set internal AE preferences, see [Preferences object](preferences.md)

---

## Methods

### Settings.getSetting()

`app.settings.getSetting(sectionName, keyName[, prefType])`

#### Description

Retrieves a script settings item value from the preferences file.

!!! warning
    If the value is greater than 1999 bytes, `getSetting` that item will throw an error (seen in AE 15.0.1)

#### Parameters

|   Parameter   |                       Type                        |               Description               |
| ------------- | ------------------------------------------------- | --------------------------------------- |
| `sectionName` | String                                            | The name of a settings section.         |
| `keyName`     | String                                            | The key name of the setting item.       |
| `prefType`    | [`PREFType` enum](./preferences.md#preftype-enum) | Optional. Which preference file to use. |


#### Returns

String.

#### Example

If you have saved a setting named with the key name "trimPrecomps" in a section called "Precomp Cropper", you can retrieve the value by:

```javascript
var trimPrecompsSetting = app.settings.getSetting("Precomp Cropper", "trimPrecomps");
alert("The setting is: " + trimPrecompsSetting);
```

---

### Settings.haveSetting()

`app.settings.haveSetting(sectionName, keyName[, prefType])`

#### Description

Returns `true` if the specified script settings item exists and has a value.

#### Parameters

|   Parameter   |                       Type                        |               Description               |
| ------------- | ------------------------------------------------- | --------------------------------------- |
| `sectionName` | String                                            | The name of a settings section.         |
| `keyName`     | String                                            | The key name of the setting item.       |
| `prefType`    | [`PREFType` enum](./preferences.md#preftype-enum) | Optional. Which preference file to use. |

#### Returns

Boolean.

---

### Settings.saveSetting()

`app.settings.saveSetting(sectionName, keyName, value[, prefType])`

#### Description

Saves a value for a script settings item.

!!! warning
    If the value is greater than 1999 bytes, `saveSetting` that item will throw an error (seen in AE 15.0.1)

#### Parameters

|   Parameter   |                       Type                        |               Description               |
| ------------- | ------------------------------------------------- | --------------------------------------- |
| `sectionName` | String                                            | The name of a settings section.         |
| `keyName`     | String                                            | The key name of the setting item.       |
| `value`       | String                                            | The new value.                          |
| `prefType`    | [`PREFType` enum](./preferences.md#preftype-enum) | Optional. Which preference file to use. |

#### Returns

Nothing.

#### Example

If you want to save a setting called "trimPrecomps" for a script named "Precomp Cropper", you could save that setting via

```javascript
var trimPrecompsSetting = true;
app.settings.saveSetting("Precomp Cropper", "trimPrecomps", trimPrecompsSetting);
```

Note that the setting will be saved as a string. You'll want to parse it into a bool later, if needed.
