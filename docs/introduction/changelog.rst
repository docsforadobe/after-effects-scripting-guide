.. highlight:: javascript
.. _changelog:

Changelog
#########

What's new and changed for scripting?

----

.. _Changelog.15-1:

`After Effects 15.1`_
************************************************************************************************************************************

- :ref:`Project.autoFixExpressions` will now fix expression name references in single quotes (ex., ('Effect Name')), as well as double quotes.
- Fixes :ref:`CompItem.exportAsMotionGraphicsTemplate` not returning a boolean as expected

----

.. _Changelog.15-0:

`After Effects 15.0 (CC 2018) <https://forums.adobe.com/docs/DOC-8872>`_
************************************************************************************************************************************

- Scripting Access to motion graphics templates
	- Added: :ref:`CompItem.motionGraphicsTemplateName`
	- Added: :ref:`CompItem.exportAsMotionGraphicsTemplate`
	- Added: :ref:`CompItem.openInEssentialGraphics`
	- Added: :ref:`Property.addToMotionGraphicsTemplate`
	- Added: :ref:`CompItem.canAddToMotionGraphicsTemplate`

----

.. _Changelog.14-2-1:

`After Effects 14.2.1 (CC 2017.2) <https://blogs.adobe.com/creativecloud/a-june-2017-update-to-after-effects-cc-is-now-available/>`_
************************************************************************************************************************************

- Buttons in ScriptUI panels have been reverted to the rectangular appearance seen in After Effects 14.1 and previous releases.
- The :ref:`AVItem.setProxyToNone` scripting method no longer fails with an error message, “After Effects error: AEGP trying to add invalid footage”.
- The :ref:`System.callSystem` scripting method now waits for all tasks called by the command to complete, instead of failing when the command takes a long time to complete.

----

.. _Changelog.14-2:

`After Effects 14.2 (CC 2017.1) <https://blogs.adobe.com/creativecloud/after-effects-cc-april-2017-in-depth-scripting-improvements/>`_
**************************************************************************************************************************************

- Scripting Access to text leading
	- Added: :ref:`TextDocument.leading`
- Scripting Access to Team Projects (Beta)
	- Added: :ref:`Project.newTeamProject`
	- Added: :ref:`Project.openTeamProject`
	- Added: :ref:`Project.shareTeamProject`
	- Added: :ref:`Project.syncTeamProject`
	- Added: :ref:`Project.closeTeamProject`
	- Added: :ref:`Project.convertTeamProjectToProject`
	- Added: :ref:`Project.listTeamProjects`
	- Added: :ref:`Project.isTeamProjectOpen`
	- Added: :ref:`Project.isAnyTeamProjectOpen`
	- Added: :ref:`Project.isTeamProjectEnabled`
	- Added: :ref:`Project.isLoggedInToTeamProject`
	- Added: :ref:`Project.isSyncCommandEnabled`
	- Added: :ref:`Project.isShareCommandEnabled`
	- Added: :ref:`Project.isResolveCommandEnabled`
	- Added: :ref:`Project.resolveConflict`

- Drop-down menus in ScriptUI panels are no longer clipped on HiDPI displays on Windows.
- The appearance of buttons, sliders, disclosure triangles (“twirly arrow”), scroll bar, progress bar, radio buttons, and checkboxes in ScriptUI embedded panels have been updated to match the appearance of After Effects native controls.
- After Effects no longer crashes when the :ref:`TextDocument.compPointToSource` scripting method is used with a 3D text layer.
- The match name of the Fast Box Blur effect is “ADBE Box Blur2”. The older match name “ADBE Box Blur” will continue to work: when used to add the effect, “ADBE Box Blur” will apply the Fast Box Blur effect, but with the older name “Box Blur”; the Iterations parameter will be set to the new default of 3.

----

.. _Changelog.14-0:

`After Effects 14.0 (CC 2017) <https://forums.adobe.com/message/9108589>`_
**************************************************************************

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

`After Effects 13.8 (CC 2015.3) <https://blogs.adobe.com/creativecloud/after-effects-cc-2015-3-in-depth-gpu-accelerated-effects/>`_
***********************************************************************************************************************************

- Enable GPU effect rendering via scripting
	- Added: :ref:`Project.gpuAccelType`
- New Gaussian Blur effect added w/ matchname ``ADBE Gaussian Blur 2``

----

.. _Changelog.13-6:

`After Effects 13.6 (CC 2015) <https://blogs.adobe.com/creativecloud/whats-new-and-changed-in-the-upcoming-update-to-after-effects-cc-2015/>`_
**********************************************************************************************************************************************
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

`After Effects 13.2 (CC 2014.2) <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-2-13-2/>`_
*******************************************************************************************************

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

`After Effects 13.1 (CC 2014.1) <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-1-13-1/>`_
*******************************************************************************************************

- Scripting improvements for text layers (read-only)
	- returns string:
		- Added: :ref:`fontLocation <TextDocument.fontLocation>`
		- Added: :ref:`fontStyle <TextDocument.fontStyle>`
		- Added: :ref:`fontFamily <TextDocument.fontFamily>`
- "Use Legacy UI" toggle implemented

----

.. _Changelog.13-0:

`After Effects 13.0 (CC 2014) <https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/>`_
***********************************************************************************************************

- Scripting access to render settings and output module settings
	- Added: RenderQueueItem object :ref:`getSetting <RenderQueueItem.getSetting>`, :ref:`setSetting <RenderQueueItem.setSetting>` methods
	- Added: RenderQueueItem object :ref:`getSettings <RenderQueueItem.getSettings>`, :ref:`setSettings <RenderQueueItem.setSettings>` methods
	- Added: OutputModule object :ref:`getSetting <OutputModule.getSetting>`, :ref:`setSetting <OutputModule.setSetting>` methods
	- Added: OutputModule object :ref:`getSettings <OutputModule.getSettings>`, :ref:`setSettings <OutputModule.setSettings>` methods
- Fetch project item by id: :ref:`Project.itemByID`
- CEP panels implemented

----

.. _Changelog.12-0:

`After Effects 12.0 (CC) <https://blogs.adobe.com/creativecloud/scripting-changes-in-after-effects-cc-12-0-12-2/>`_
*******************************************************************************************************************

- Access to effect's internal version string
	- Added: Application effects object's version attribute, see :ref:`app.effects`
- Ability to get and set preview mode
	- Added: :ref:`Viewer.fastPreview`
- Access to layer sampling method (see :ref:`samplingQuality <Layer.samplingQuality>`)
- Changed preference and settings methods (see :ref:`Settings`)
- ScriptUI is now based on the same controls as the main application.
