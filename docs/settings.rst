.. highlight:: javascript
.. _Settings:

Settings object
################################################

``app.settings``

**Description**

The Settings object provides an easy way to manage settings for scripts. The settings are saved in the After Effects preferences file and are persistent between application sessions. Settings are identified by section and key within the file, and each key name is associated with a value. In the preferences file, section names are enclosed in brackets and quotation marks, and key names are listing in quotation marks below the sectionname. All values are strings. You can create new settings with this object, as well as accessing existing settings.

.. note::
	For AE12.0+, preferences and settings methods now take a third argument to specify the target preferences file if Section/Key is not in “Adobe After Effects $versionNumber.x Prefs.txt”. If the third argument is not passed, default value (``PREFType.PREF_Type_MACHINE_SPECIFIC``) is used and After Effects tries to save/get from the “Adobe After Effects $versionNumber.x Prefs.txt” preferences file. The third argument is enum ``PREFType`` value.

You can now pass the preference type with a script with new ``PREFType`` enum:

- ``PREF_Type_MACHINE_SPECIFIC``: Adobe After Effects $versionNumber.x Prefs.txt
- ``PREF_Type_MACHINE_INDEPENDENT``: Adobe After Effects $versionNumber.x Prefs-indep-general.txt
- ``PREF_Type_MACHINE_INDEPENDENT_RENDER``: Adobe After Effects $versionNumber.x Prefs-indep-render.txt
- ``PREF_Type_MACHINE_INDEPENDENT_OUTPUT``: Adobe After Effects $versionNumber.x Prefs-indep-output.txt
- ``PREF_Type_MACHINE_INDEPENDENT_COMPOSITION``: Adobe After Effects $versionNumber.x Prefs-indep-composition.txt
- ``PREF_Type_MACHINE_SPECIFIC_TEXT``: Adobe After Effects $versionNumber.x Prefs-text.txt
- ``PREF_Type_MACHINE_SPECIFIC_PAINT``: Adobe After Effects $versionNumber.x Prefs-paint.txt


----

=======
Methods
=======

.. _Settings.getSetting:

Settings.getSetting()
*********************

``app.settings.getSetting(sectionName, keyName)``

**Description**

Retrieves a scripting preferences item value from the preferences file.

**Parameters**

===============	==============================================================
``sectionName``	A string containing the name of a settings section
``keyName``		A string containing the key name of the setting item.
===============	==============================================================

**Returns**

String.

**Example**

If you have saved a setting named with the key name "Aligned Clone" in the "Eraser - Paint Settings" section,you can retrieve the value with this script::

	var n = app.settings.getSetting("Eraser-PaintSettings", "AlignedClone");
	alert("The setting is" + n);

----

.. _Settings.haveSetting:

Settings.haveSetting()
**********************

``app.settings.haveSetting(sectionName, keyName)``

**Description**

Returns true if the specified scripting preferences item exists and has a value.

**Parameters**

===============	==============================================================
``sectionName``	A string containing the name of a settings section
``keyName``		A string containing the key name of the setting item.
===============	==============================================================

**Returns**

Boolean.

----

.. _Settings.saveSetting:

Settings.saveSetting()
**********************

``app.settings.saveSetting(sectionName, keyName, value)``

**Description**

Saves a default value for a scripting preferences item.

**Parameters**

===============	==============================================================
``sectionName``	A string containing the name of a settings section
``keyName``		A string containing the key name of the setting item.
``value``		A string containing the new value.
===============	==============================================================

**Returns**

Nothing.
