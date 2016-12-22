.. highlight:: javascript
.. _changelog:

Changelog
################################################

What's new and changed for scripting?

----

.. _Changelog.14-0:

`After Effects 14.0 <https://forums.adobe.com/message/9108589>`_
*****************************************************************

- Scripting Access to Tools
	- Added: :ref:`Project.toolType`
- Scripting Access to Composition Markers
	- Added: :ref:`CompItem.markerProperty`
- Scripting Access to Queue in AME
	- Added: :ref:`RenderQueue.queueInAME`
- Scripting Access to Available GPU Acceleration Options
	- Added: :ref:`app.availableGPUAccelTypes`

----

.. _Changelog.13-8:

`After Effects 13.8 <https://blogs.adobe.com/creativecloud/after-effects-cc-2015-3-in-depth-gpu-accelerated-effects/>`_
************************************************************************************************************************

- Enable GPU effect rendering via scripting
	- Added: :ref:`Project.gpuAccelType`
- New Gaussian Blur effect added w/ matchname ``ADBE Gaussian Blur 2``

----

.. _Changelog.13-6:

`After Effects 13.6 <https://blogs.adobe.com/creativecloud/whats-new-and-changed-in-the-upcoming-update-to-after-effects-cc-2015/>`_
*************************************************************************************************************************************
- Scripting access to text baselines
	- Added: :ref:`baselineLocs <TextDocument.baselineLocs>`
- New scripting method to generate random numbers
	- Added: :ref:`generateRandomNumber() <generateRandomNumber>`
- Using the :ref:`copyToComp() <Layer.copyToComp>` scripting method no longer causes After Effects to crash when the layer has a parent.
- The :ref:`valueAtTime() <Property.valueAtTime>` scripting method now waits for time-intensive expressions, like ``sampleImage``, to finish evaluating before it returns the result.
- ScriptUI panels now display and resize correctly on high-DPI displays on Windows.
- After Effects no longer crashes when you click OK or Cancel buttons in a scriptUI dialog with tabbed panels.

----

.. _Changelog.13-2:

`After Effects 13.2 <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-2-13-2/>`_
********************************************************************************************

- Scripting improvements for text layers (read-only)
	- Returns boolean value:
		- Added: :ref:`fauxBold <TextDocument.fauxBold>`
		- Added: :ref:`fauxItalic <TextDocument.fauxItalic>`
		- Added: :ref:`allCaps <TextDocument.allCaps>`
		- Added: :ref:`smallCaps <TextDocument.smallCaps>`
		- Added: :ref:`superscript <TextDocument.superscript>`
		- Added: :ref:`subscript <TextDocument.subscript>`
	- Returns float:
		- Added: :ref:`verticalScale <TextDocument.verticalScale>`
		- Added: :ref:`horizontalScale <TextDocument.horizontalScale>`
		- Added: :ref:`baselineShift <TextDocument.baselineShift>`
		- Added: :ref:`tsume <TextDocument.tsume>`
	- Returns array of ([X,Y]) position coordinates (paragraph text layers only):
		- Added: :ref:`boxTextPos <TextDocument.boxTextPos>`
		- Added: :ref:`sourcePointToComp() <TextDocument.sourcePointToComp>`
		- Added: :ref:`compPointToSource() <TextDocument.compPointToSource>`

----

.. _Changelog.13-1:

`After Effects 13.1 <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-1-13-1/>`_
********************************************************************************************

- Scripting improvements for text layers (read-only)
	- returns string:
		- Added: :ref:`fontLocation <TextDocument.fontLocation>`
		- Added: :ref:`fontStyle <TextDocument.fontStyle>`
		- Added: :ref:`fontFamily <TextDocument.fontFamily>`
- "Use Legacy UI" toggle implemented

----

.. _Changelog.13-0:
`After Effects 13.0 <https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/>`_
*************************************************************************************************

- Scripting access to render settings and output module settings
	- Added: RenderQueueItem object :ref:`getSetting <RenderQueueItem.getSetting>`, :ref:`setSetting <RenderQueueItem.setSetting>` methods
	- Added: RenderQueueItem object :ref:`getSettings <RenderQueueItem.getSettings>`, :ref:`setSettings <RenderQueueItem.setSettings>` methods
	- Added: OutputModule object :ref:`getSetting <OutputModule.getSetting>`, :ref:`setSetting <OutputModule.setSetting>` methods
	- Added: OutputModule object :ref:`getSettings <OutputModule.getSettings>`, :ref:`setSettings <OutputModule.setSettings>` methods
- CEP panels implemented

----

.. _Changelog.12-0:
`After Effects 12.0 <https://blogs.adobe.com/creativecloud/scripting-changes-in-after-effects-cc-12-0-12-2/>`_
***************************************************************************************************************

- Access to effect's internal version string
	- Added: Application effects object's version attribute, see :ref:`app.effects`
- Ability to get and set preview mode
	- Added: :ref:`Viewer.fastPreview`
- Access to layer sampling method (see :ref:`samplingQuality <Layer.samplingQuality>`)
- Changed preference and settings methods (see :ref:`Settings`)
- ScriptUI is now based on the same controls as the main application.