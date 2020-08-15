.. highlight:: javascript
.. _Settings:

Settings object
################################################

``app.settings``

**Description**

The Settings object provides an easy way to manage settings for third-party scripts. The settings are saved in the main After Effects preferences file, and are persistent between application sessions.

Settings are identified by section and key within the file, and each key name is associated with a value.

In the settings file, section names are enclosed in brackets and quotation marks, and key names are listing in quotation marks below the sectionname. All values are strings.

You can create new settings with this object, as well as accessing existing settings.

As of Version 12/CC, preferences and settings methods now take a third argument to specify the target preferences file if Section/Key is not in the main preferences file. See :ref:`Preferences` for more info.

.. note::
  - These values aren't shared between versions of AE; each new install brings new settings files, and so these prefs won't carry over.
  - Internally, all saved settings have their section name preprended with ``"Settings_"``
  - If you're looking to get or set internal AE preferences, see :ref:`Preferences`

.. tip::
  - It's best practice to use one ``sectionName`` per script; this keeps your settings organized and easy to find & work with.
  - There isn't really any benefit in saving your settings to a specific preferences file; omitting the third argument and using the default is likely all you'll need.

----

=======
Methods
=======

.. _Settings.getSetting:

Settings.getSetting()
*********************

``app.settings.getSetting(sectionName, keyName[, prefType])``

**Description**

Retrieves a script settings item value from the preferences file.

.. warning::
   If the value is greater than 1999 bytes, ``getSetting`` that item will throw an error (seen in AE 15.0.1)

**Parameters**

===============  ==============================================================
``sectionName``  A string containing the name of a settings section.
``keyName``      A string containing the key name of the setting item.
``prefType``     Optional, an enum indicating which preference file to use.
===============  ==============================================================

**Returns**

String.

**Example**

If you have saved a setting named with the key name "trimPrecomps" in a section called "Precomp Cropper", you can retrieve the value by:

.. code:: javascript

    var trimPrecompsSetting = app.settings.getSetting("Precomp Cropper", "trimPrecomps");
    alert("The setting is: " + trimPrecompsSetting);

----

.. _Settings.haveSetting:

Settings.haveSetting()
**********************

``app.settings.haveSetting(sectionName, keyName[, prefType])``

**Description**

Returns true if the specified script settings item exists and has a value.

**Parameters**

===============  ==============================================================
``sectionName``  A string containing the name of a settings section.
``keyName``      A string containing the key name of the setting item.
``prefType``     Optional, an enum indicating which preference file to use.
===============  ==============================================================

**Returns**

Boolean.

----

.. _Settings.saveSetting:

Settings.saveSetting()
**********************

``app.settings.saveSetting(sectionName, keyName, value[, prefType])``

**Description**

Saves a value for a script settings item.

.. warning::
   If the value is greater than 1999 bytes, ``saveSetting`` that item will throw an error (seen in AE 15.0.1)

**Parameters**

===============  ==============================================================
``sectionName``  A string containing the name of a settings section.
``keyName``      A string containing the key name of the setting item.
``value``        A string containing the new value.
``prefType``     Optional, an enum indicating which preference file to use.
===============  ==============================================================

**Returns**

Nothing.

**Example**

If you want to save a setting called "trimPrecomps" for a script named "Precomp Cropper", you could save that setting via

.. code:: javascript

    var trimPrecompsSetting = true;
    app.settings.saveSetting("Precomp Cropper", "trimPrecomps", trimPrecompsSetting);

Note that the setting will be saved as a string. You'll want to parse it into a bool later, if needed.
