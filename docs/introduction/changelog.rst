.. highlight:: javascript
.. _changelog:

Changelog
#########

What's new and changed for scripting?

----

.. _Changelog.24.4:

`After Effects 24.4 Beta build 25 <https://community.adobe.com/t5/after-effects-beta-discussions/scripting-new-api-for-3d-model-layers/td-p/14580044>`_ (March 2024)
********************************************************************************************************************************************************************************************

	- Added: :ref:`ThreeDModelLayer`

`After Effects 24.4 Beta build 24 <https://community.adobe.com/t5/after-effects-beta-discussions/scripting-new-and-updated-apis-for-font-management/td-p/14508673>`_ (March 2024)
********************************************************************************************************************************************************************************************

	- Added: :ref:`FontsObject.favoriteFontFamilyList`
	- Added: :ref:`FontsObject.fontsDuplicateByPostScriptName`
	- Added: :ref:`FontsObject.freezeSyncSubstitutedFonts`
	- Added: :ref:`FontsObject.mruFontFamilyList`
	- Added: :ref:`FontsObject.substitutedFontReplacementMatchPolicy`
	- Added: :ref:`FontsObject.pollForAndPushNonSystemFontFoldersChanges`

`After Effects 24.4 Beta build 6 <https://community.adobe.com/t5/after-effects-beta-discussions/heads-up-revisions-fix-to-missing-font-replacement-behavior/td-p/14466683>`_ (March 2024)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added or changed
	- Changed: :ref:`Project.replaceFont`
	- Changed: :ref:`Project.usedFonts`

`After Effects 24.3 Beta build 25 <https://community.adobe.com/t5/after-effects-beta-discussions/per-character-scripting-public-beta-announcement/m-p/14414997#M3325>`_ (February 2024)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added or changed
	- Changed: :ref:`ParagraphRange object<ParagraphRange>` (all text attributes removed)
	- Added: :ref:`ComposedLineRange object<ComposedLineRange>`
	- Added: :ref:`ParagraphRange.characterRange`
	- Added: :ref:`TextDocument.composedLineCharacterIndexesAt`
	- Added: :ref:`TextDocument.composedLineCount`
	- Added: :ref:`TextDocument.composedLineRange`

`After Effects 24.3 Beta build 20 <https://community.adobe.com/t5/after-effects-beta-discussions/new-text-box-options-available-in-scripting/m-p/14409110>`_ (February 2024)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added or changed
	- Added: :ref:`TextDocument.boxAutoFitPolicy`
	- Added: :ref:`TextDocument.boxFirstBaselineAlignment`
	- Added: :ref:`TextDocument.boxFirstBaselineAlignmentMinimum`
	- Added: :ref:`TextDocument.boxInsetSpacing`
	- Added: :ref:`TextDocument.boxOverflow`
	- Added: :ref:`TextDocument.boxVerticalAlignment`

`After Effects 24.2 <https://helpx.adobe.com/after-effects/using/whats-new/2024-2.html>`_ (February 2024)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added or changed
	- Added: :ref:`LayerCollection.addVerticalText`
	- Added: :ref:`LayerCollection.addVerticalBoxText`
	- Added: :ref:`TextDocument.lineOrientation`
	- Added: :ref:`FontsObject.fontServerRevision`
	- Added: :ref:`FontsObject.getFontByID`
	- Added: :ref:`FontObject.fontID`

`After Effects 24.2 Beta build 17 <https://community.adobe.com/t5/after-effects-beta-discussions/per-character-scripting-public-beta-announcement/m-p/14247138>`_ (November 2023)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added
	- Added: :ref:`CharacterRange object<CharacterRange>`
	- Added: :ref:`ParagraphRange object<ParagraphRange>`
	- Added: :ref:`TextDocument.characterRange`
	- Added: :ref:`TextDocument.paragraphRange`
	- Added: :ref:`TextDocument.paragraphCount`
	- Added: :ref:`TextDocument.paragraphCharacterIndexesAt`

.. _Changelog.24.0:

`After Effects 24.0 Beta build 37 <https://community.adobe.com/t5/after-effects-beta-discussions/new-text-scripting-hooks-for-font-replacement/m-p/14025889>`_ (August 2023)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added
	- Added: :ref:`Project.usedFonts`
	- Added: :ref:`Project.replaceFont`

`After Effects 24.0 <https://helpx.adobe.com/after-effects/using/whats-new/2024.html>`_ (October 2023)
********************************************************************************************************************************************************************************************

- Scripting methods and attributes added
	- Added: :ref:`getEnumAsString`
	- Added: :ref:`app.fonts`
	- Added: :ref:`FontsObject`
	- Added: :ref:`FontsObject.allFonts`
	- Added: :ref:`FontsObject.fontsWithDefaultDesignAxes`
	- Added: :ref:`FontsObject.getFontsByFamilyNameAndStyleName`
	- Added: :ref:`FontsObject.getFontsByPostScriptName`
	- Added: :ref:`FontsObject.missingOrSubstitutedFonts`
	- Added: :ref:`FontObject`
	- Added: :ref:`FontObject.designAxesData`
	- Added: :ref:`FontObject.designVector`
	- Added: :ref:`FontObject.familyPrefix`
	- Added: :ref:`FontObject.hasDesignAxes`
	- Added: :ref:`FontObject.hasSameDict`
	- Added: :ref:`FontObject.postScriptNameForDesignVector`
	- Added: :ref:`FontObject.familyName`
	- Added: :ref:`FontObject.fullName`
	- Added: :ref:`FontObject.isFromAdobeFonts`
	- Added: :ref:`FontObject.isSubstitute`
	- Added: :ref:`FontObject.location`
	- Added: :ref:`FontObject.nativeFamilyName`
	- Added: :ref:`FontObject.nativeFullName`
	- Added: :ref:`FontObject.nativeStyleName`
	- Added: :ref:`FontObject.postScriptName`
	- Added: :ref:`FontObject.styleName`
	- Added: :ref:`FontObject.technology`
	- Added: :ref:`FontObject.type`
	- Added: :ref:`FontObject.version`
	- Added: :ref:`FontObject.writingScripts`
	- Added: :ref:`TextDocument.autoHyphenate`
	- Added: :ref:`TextDocument.autoKernType`
	- Added: :ref:`TextDocument.baselineDirection`
	- Added: :ref:`TextDocument.composerEngine`
	- Added: :ref:`TextDocument.digitSet`
	- Added: :ref:`TextDocument.direction`
	- Added: :ref:`TextDocument.endIndent`
	- Added: :ref:`TextDocument.everyLineComposer`
	- Added: :ref:`TextDocument.firstLineIndent`
	- Added: :ref:`TextDocument.fontBaselineOption`
	- Added: :ref:`TextDocument.fontCapsOption`
	- Added: :ref:`TextDocument.fontObject`
	- Added: :ref:`TextDocument.hangingRoman`
	- Added: :ref:`TextDocument.kerning`
	- Added: :ref:`TextDocument.leadingType`
	- Added: :ref:`TextDocument.ligature`
	- Added: :ref:`TextDocument.lineJoinType`
	- Added: :ref:`TextDocument.noBreak`
	- Added: :ref:`TextDocument.spaceAfter`
	- Added: :ref:`TextDocument.spaceBefore`
	- Added: :ref:`TextDocument.startIndent`

- Scripting attributes updated
	- Updated: :ref:`TextDocument.fauxBold`
	- Updated: :ref:`TextDocument.fauxItalic`
	- Updated: :ref:`TextDocument.justification`

.. _Changelog.23.0:

`After Effects 23.0 <https://helpx.adobe.com/after-effects/using/whats-new/2023.html>`_ (October 2022)
************************************************************************************************************************************

- Scripting methods and attributes added
	- Added: :ref:`AVLayer.setTrackMatte`
	- Added: :ref:`AVLayer.removeTrackMatte`
	- Added: :ref:`AVLayer.trackMatteLayer`

- Scripting attributes updated
	- Updated: :ref:`AVLayer.trackMatteType`
	- Updated: :ref:`AVLayer.isTrackMatte`
	- Updated: :ref:`AVLayer.hasTrackMatte`

.. _Changelog.22.6:

`After Effects 22.6 <https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html>`_ (August 2022)
************************************************************************************************************************************

- Scripting methods added
	- Added: :ref:`Property.keyLabel`
	- Added: :ref:`Property.setLabelAtKey`

.. _Changelog.22.3:

`After Effects 22.3 <https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html>`_ (April 2022)
************************************************************************************************************************************

- Scripting methods added
	- Added: :ref:`Layer.doSceneEditDetection`

----

.. _Changelog.22.0:

`After Effects 22.0 <https://helpx.adobe.com/after-effects/using/whats-new/2022.html>`_ (October 2021)
************************************************************************************************************************************

- Scripting methods added
	- Added: :ref:`Layer.id`
	- Added: :ref:`Project.layerByID`
	- Added: :ref:`Property.essentialPropertySource`
- Scripting Access to Render Queue Notifications
    - Added: :ref:`RenderQueue.queueNotify`
    - Added: :ref:`RenderQueueItem.queueItemNotify`
- Scripting Access to Multi-Frame Rendering, Maximum CPU Percentage Overrides
    - Added: :ref:`app.setMultiFrameRenderingConfig`

----

.. _Changelog.18.0:

`After Effects 18.0 <https://helpx.adobe.com/after-effects/using/whats-new/2021-2.html>`_ (March 2021)
************************************************************************************************************************************

- Scripting methods and attributes to support Media Replacement
	- Added: :ref:`AVItem.isMediaReplacementCompatible`
	- Added: :ref:`AVLayer.addToMotionGraphicsTemplate`
	- Added: :ref:`AVLayer.addToMotionGraphicsTemplateAs`
	- Added: :ref:`AVLayer.canAddToMotionGraphicsTemplate`
	- Added: :ref:`Property.alternateSource`
	- Added: :ref:`Property.canSetAlternateSource`
	- Added: :ref:`Property.setAlternateSource`
	- Added relevant :ref:`match names <matchnames-layer-avlayer>`
- Added :ref:`match name for Essential Properties <matchnames-layer-avlayer>` property group.

----

.. _Changelog.17.1.1:

`After Effects 17.1.1 <https://helpx.adobe.com/after-effects/using/whats-new/2020-1.html>`_ (May 2020)
************************************************************************************************************************************

- Scripting access to Shape Layer Stroke Taper, Stroke Waves, Offset Paths Copies, Offset Path Copy Offset
	- Added relevant :ref:`match names <matchnames-layer-shapelayer>`
- Fixed an issue to allow negative values for :ref:`CompItem.displayStartTime`:
	- Added :ref:`CompItem.displayStartFrame`
	- Now matches the valid range allowed when setting the Start Timecode in the Composition Settings Dialog (-3:00:00:00 to 23:59:00:00).

----

.. _Changelog.17.0.1:

`After Effects 17.0.1 <https://helpx.adobe.com/after-effects/using/whats-new/2020.html>`_ (November 2019)
************************************************************************************************************************************

- Scripted creation and modification of Dropdown Menu Control items:
	- Added: :ref:`Property.isDropdownEffect`
	- Added: :ref:`Property.setPropertyParameters`

----

.. _Changelog.16.1:

`After Effects 16.1`_
************************************************************************************************************************************

- Scripting access to :ref:`ViewOptions` guide and ruler booleans:
	- Added: :ref:`ViewOptions.guidesLocked`
	- Added: :ref:`ViewOptions.guidesSnap`
	- Added: :ref:`ViewOptions.guidesVisibility`
	- Added: :ref:`ViewOptions.rulers`
- Scripting access to add, remove, and set existing guides:
	- Added: :ref:`Item.addGuide`
	- Added: :ref:`Item.removeGuide`
	- Added: :ref:`Item.setGuide`
- Scripting access to additional EGP property attributes:
	- Added: :ref:`CompItem.motionGraphicsTemplateControllerCount`
	- Added: :ref:`CompItem.getMotionGraphicsTemplateControllerName`
	- Added: :ref:`CompItem.setMotionGraphicsControllerName`
	- Added: :ref:`Property.addToMotionGraphicsTemplateAs`

----

.. _Changelog.16.0:

`After Effects 16.0 <https://helpx.adobe.com/after-effects/using/whats-new/2019.html>`_ (October 2018)
************************************************************************************************************************************

- Scripting access to marker label and protectedRegion attributes:
	- Added: :ref:`MarkerValue.label`
	- Added: :ref:`MarkerValue.protectedRegion`
- Scripting access to additional project color management settings:
	- Added: :ref:`Project.workingSpace`
	- Added: :ref:`Project.workingGamma`
	- Added: :ref:`Project.listColorProfiles`
	- Added: :ref:`Project.linearizeWorkingSpace`
	- Added: :ref:`Project.compensateForSceneReferredProfiles`
- Scripting access to the expression engine attribute:
	- Added: :ref:`Project.expressionEngine`
- Added project method :ref:`Project.setDefaultImportFolder`, which sets the folder that will be shown in the file import dialog.
- Added app property :ref:`app.disableRendering`, which disables rendering via the same mechanism as the Caps Lock key.

----

.. _Changelog.15-1:

`After Effects 15.1 <https://helpx.adobe.com/after-effects/using/whats-new/2018.html>`_ (April 2018)
************************************************************************************************************************************

- :ref:`Project.autoFixExpressions` will now fix expression name references in single quotes (ex., ('Effect Name')), as well as double quotes.
- Fixes :ref:`CompItem.exportAsMotionGraphicsTemplate` not returning a boolean as expected

----

.. _Changelog.15-0:

`After Effects 15.0 <https://forums.adobe.com/docs/DOC-8872>`_ (October 2017)
************************************************************************************************************************************

- Scripting Access to motion graphics templates
	- Added: :ref:`CompItem.motionGraphicsTemplateName`
	- Added: :ref:`CompItem.exportAsMotionGraphicsTemplate`
	- Added: :ref:`CompItem.openInEssentialGraphics`
	- Added: :ref:`Property.addToMotionGraphicsTemplate`
	- Added: :ref:`Property.canAddToMotionGraphicsTemplate`

----

.. _Changelog.14-2-1:

`After Effects 14.2.1 (CC 2017.2) <https://blogs.adobe.com/creativecloud/a-june-2017-update-to-after-effects-cc-is-now-available/>`_ (June 2017)
************************************************************************************************************************************************

- Buttons in ScriptUI panels have been reverted to the rectangular appearance seen in After Effects 14.1 and previous releases.
- The :ref:`AVItem.setProxyToNone` scripting method no longer fails with an error message, "After Effects error: AEGP trying to add invalid footage".
- The :ref:`System.callSystem` scripting method now waits for all tasks called by the command to complete, instead of failing when the command takes a long time to complete.

----

.. _Changelog.14-2:

`After Effects 14.2 (CC 2017.1) <https://blogs.adobe.com/creativecloud/after-effects-cc-april-2017-in-depth-scripting-improvements/>`_ (April 2017)
***************************************************************************************************************************************************

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
- The appearance of buttons, sliders, disclosure triangles ("twirly arrow"), scroll bar, progress bar, radio buttons, and checkboxes in ScriptUI embedded panels have been updated to match the appearance of After Effects native controls.
- After Effects no longer crashes when the :ref:`AVLayer.compPointToSource` scripting method is used with a 3D text layer.
- The match name of the Fast Box Blur effect is "ADBE Box Blur2". The older match name "ADBE Box Blur" will continue to work: when used to add the effect, "ADBE Box Blur" will apply the Fast Box Blur effect, but with the older name "Box Blur"; the Iterations parameter will be set to the new default of 3.

----

.. _Changelog.14-0:

`After Effects 14.0 (CC 2017) <https://forums.adobe.com/message/9108589>`_ (November 2016)
******************************************************************************************

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

`After Effects 13.8 (CC 2015.3) <https://blogs.adobe.com/creativecloud/after-effects-cc-2015-3-in-depth-gpu-accelerated-effects/>`_ (June 2016)
***********************************************************************************************************************************************

- Enable GPU effect rendering via scripting
	- Added: :ref:`Project.gpuAccelType`
- New Gaussian Blur effect added w/ matchname ``ADBE Gaussian Blur 2``

----

.. _Changelog.13-6:

`After Effects 13.6 (CC 2015) <https://blogs.adobe.com/creativecloud/whats-new-and-changed-in-the-upcoming-update-to-after-effects-cc-2015/>`_ (November 2015)
**************************************************************************************************************************************************************
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

`After Effects 13.2 (CC 2014.2) <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-2-13-2/>`_ (December 2014)
***********************************************************************************************************************

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
- Layer space / comp space conversion:
    - Added: :ref:`sourcePointToComp() <AVLayer.sourcePointToComp>`
    - Added: :ref:`compPointToSource() <AVLayer.compPointToSource>`

----

.. _Changelog.13-1:

`After Effects 13.1 (CC 2014.1) <https://blogs.adobe.com/creativecloud/after-effects-cc-2014-1-13-1/>`_ (September 2014)
************************************************************************************************************************

- Scripting improvements for text layers (read-only)
	- returns string:
		- Added: :ref:`fontLocation <TextDocument.fontLocation>`
		- Added: :ref:`fontStyle <TextDocument.fontStyle>`
		- Added: :ref:`fontFamily <TextDocument.fontFamily>`
- "Use Legacy UI" toggle implemented

----

.. _Changelog.13-0:

`After Effects 13.0 (CC 2014) <https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/>`_ (June 2014)
**********************************************************************************************************************

- Scripting access to render settings and output module settings
	- Added: RenderQueueItem object :ref:`getSetting <RenderQueueItem.getSetting>`, :ref:`setSetting <RenderQueueItem.setSetting>` methods
	- Added: RenderQueueItem object :ref:`getSettings <RenderQueueItem.getSettings>`, :ref:`setSettings <RenderQueueItem.setSettings>` methods
	- Added: OutputModule object :ref:`getSetting <OutputModule.getSetting>`, :ref:`setSetting <OutputModule.setSetting>` methods
	- Added: OutputModule object :ref:`getSettings <OutputModule.getSettings>`, :ref:`setSettings <OutputModule.setSettings>` methods
- Fetch project item by id: :ref:`Project.itemByID`
- CEP panels implemented

----

.. _Changelog.12-0:

`After Effects 12.0 (CC) <https://blogs.adobe.com/creativecloud/scripting-changes-in-after-effects-cc-12-0-12-2/>`_ (June 2013)
*******************************************************************************************************************************

- Access to effect's internal version string
	- Added: Application effects object's version attribute, see :ref:`app.effects`
- Ability to get and set preview mode
	- Added: :ref:`ViewOptions.fastPreview`
- Access to layer sampling method (see :ref:`samplingQuality <AVLayer.samplingQuality>`)
- Changed preference and settings methods (see :ref:`Settings`)
- ScriptUI is now based on the same controls as the main application.

----

.. _Changelog.11-0:

`After Effects 11.0 (CS6) <https://web.archive.org/web/20120623073355/https://blogs.adobe.com/toddkopriva/2012/06/scripting-changes-in-after-effects-cs6-plus-new-scripting-guide.html/>`_ (April 2012)
*******************************************************************************************************************************************************************************************************

- Added: Access to :ref:`Viewer` object and controls
    - Added: :ref:`app.activeViewer`
    - Added: :ref:`AVLayer.openInViewer` to open a layer in the layer viewer
    - Added: :ref:`CompItem.openInViewer` to open a composition in the composition viewer
    - Added: :ref:`FootageItem.openInViewer` to open a footage item in the footage viewer
- Added: :ref:`Property.canSetExpression`
- Added: :ref:`AVLayer.environmentLayer`
- Added: :ref:`MaskPropertyGroup.maskFeatherFalloff`
- Access to Shape Feather properties via scripting
    - Added: :ref:`Shape.featherSegLocs`
    - Added: :ref:`Shape.featherRelSegLocs`
    - Added: :ref:`Shape.featherRadii`
    - Added: :ref:`Shape.featherInterps`
    - Added: :ref:`Shape.featherTensions`
    - Added: :ref:`Shape.featherTypes`
    - Added: :ref:`Shape.featherRelCornerAngles`

----

.. _Changelog.10-5:

`After Effects 10.5 (CS5.5) <https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/>`_ (April 2011)
***********************************************************************************************************************************************************************

- Added to the :ref:`Project` object:
    - :ref:`Project.framesCountType`
    - :ref:`Project.feetFramesFilmType`
    - :ref:`Project.framesUseFeetFrames`
    - :ref:`Project.footageTimecodeDisplayStartType`
    - :ref:`Project.timeDisplayType`
- Removed from the :ref:`Project` object:
    - ``timecodeDisplayType`` attribute
    - ``timecodeBaseType`` attribute
    - ``timecodeNTSCDropFrame`` attribute
    - ``timecodeFilmType`` attribute
    - ``TimecodeDisplayType`` enum
    - ``TimecodeFilmType`` enum
    - ``TimecodeBaseType`` enum
- Added: :ref:`CompItem.dropFrame`
- Added support for Paragraph Box Text:
    - Added :ref:`LayerCollection.addBoxText`
    - Added :ref:`TextDocument.boxText`
    - Added :ref:`TextDocument.pointText`
    - Added :ref:`TextDocument.boxTextSize`
- Added :ref:`LightLayer.lightType`

----

.. _Changelog.9-0:

`After Effects 9.0 (CS4) <https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/>`_ (September 2008)
************************************************************************************************************************************************************************

- Added: :ref:`app.isoLanguage`
- Added: :ref:`MarkerValue.duration`
- Added: :ref:`OutputModule.includeSourceXMP`
- Added: :ref:`Project.xmpPacket`
- Added the following Property methods and attributes related to the Separate Dimensions feature:
    - :ref:`Property.dimensionsSeparated`
    - :ref:`Property.getSeparationFollower`
    - :ref:`Property.isSeparationFollower`
    - :ref:`Property.isSeparationLeader`
    - :ref:`Property.separationDimension`
    - :ref:`Property.separationLeader`
- Added :ref:`TextDocument` access, including:
    - Added: :ref:`TextDocument.applyFill`
    - Added: :ref:`TextDocument.applyStroke`
    - Added: :ref:`TextDocument.fillColor`
    - Added: :ref:`TextDocument.font`
    - Added: :ref:`TextDocument.fontSize`
    - Added: :ref:`TextDocument.justification`
    - Added: :ref:`TextDocument.resetCharStyle`
    - Added: :ref:`TextDocument.resetParagraphStyle`
    - Added: :ref:`TextDocument.strokeColor`
    - Added: :ref:`TextDocument.strokeOverFill`
    - Added: :ref:`TextDocument.strokeWidth`
