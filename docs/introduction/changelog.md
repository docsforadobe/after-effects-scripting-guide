---
toc_depth: 2
---

# Changelog

What's new and changed for scripting?

---

## After Effects 25

### [After Effects 25.2 Beta build 98](https://community.adobe.com/t5/after-effects-beta-discussions/animated-environmental-lights-available-now-in-after-effects-beta/td-p/15130220) (February 2025)

- Scripting methods and attributes added:
    - Updated: [LightLayer.lightSource](../layer/lightlayer.md#lightlayerlightsource)

### [After Effects 25.0 Beta build 26](https://community.adobe.com/t5/after-effects-beta-discussions/new-in-ae-25-0-build-25-scripting-hooks-for-font-fallback-management/m-p/14809794) (August 2024)

- Scripting methods and attributes added:
    - Added: [CharacterRange.pasteFrom()](../text/characterrange.md#characterrangepastefrom)
    - Added: [FontObject.hasGlyphsFor()](../text/fontobject.md#fontobjecthasglyphsfor)
    - Added: [FontObject.otherFontsWithSameDict()](../text/fontobject.md#fontobjectotherfontswithsamedict)
    - Added: [FontsObject.getCTScriptForString()](../text/fontsobject.md#fontsobjectgetctscriptforstring)
    - Added: [FontsObject.getDefaultFontForCTScript()](../text/fontsobject.md#fontsobjectgetdefaultfontforctscript)
    - Added: [FontsObject.setDefaultFontForCTScript()](../text/fontsobject.md#fontsobjectsetdefaultfontforctscript)

---

## After Effects 24

### [After Effects 24.6](https://helpx.adobe.com/after-effects/using/whats-new/2024-6.html) (August 2024)

- Scripting methods and attributes added:
    - Added: [FontsObject.favoriteFontFamilyList](../text/fontsobject.md#fontsobjectfavoritefontfamilylist)
    - Added: [FontsObject.fontsDuplicateByPostScriptName](../text/fontsobject.md#fontsobjectfontsduplicatebypostscriptname)
    - Added: [FontsObject.freezeSyncSubstitutedFonts](../text/fontsobject.md#fontsobjectfreezesyncsubstitutedfonts)
    - Added: [FontsObject.mruFontFamilyList](../text/fontsobject.md#fontsobjectmrufontfamilylist)
    - Added: [FontsObject.substitutedFontReplacementMatchPolicy](../text/fontsobject.md#fontsobjectsubstitutedfontreplacementmatchpolicy)
    - Added: [FontsObject.pollForAndPushNonSystemFontFoldersChanges()](../text/fontsobject.md#fontsobjectpollforandpushnonsystemfontfolderschanges)
    - Added: [TextDocument.boxAutoFitPolicy](../text/textdocument.md#textdocumentboxautofitpolicy)
    - Added: [TextDocument.boxFirstBaselineAlignment](../text/textdocument.md#textdocumentboxfirstbaselinealignment)
    - Added: [TextDocument.boxFirstBaselineAlignmentMinimum](../text/textdocument.md#textdocumentboxfirstbaselinealignmentminimum)
    - Added: [TextDocument.boxInsetSpacing](../text/textdocument.md#textdocumentboxinsetspacing)
    - Added: [TextDocument.boxOverflow](../text/textdocument.md#textdocumentboxoverflow)
    - Added: [TextDocument.boxVerticalAlignment](../text/textdocument.md#textdocumentboxverticalalignment)

### [After Effects 24.5](https://helpx.adobe.com/after-effects/using/whats-new/2024-5.html) (May 2024)

- Scripting methods and attributes added:
    - Added: [Project.replaceFont()](../general/project.md#projectreplacefont)
    - Added: [Project.usedFonts](../general/project.md#projectusedfonts)

### [After Effects 24.4 Beta build 25](https://community.adobe.com/t5/after-effects-beta-discussions/scripting-new-api-for-3d-model-layers/td-p/14580044) (March 2024)

- Added: [ThreeDModelLayer object](../layer/threedmodellayer.md)

### [After Effects 24.3](https://helpx.adobe.com/after-effects/using/whats-new/2024-3.html) (March 2024)

- Scripting methods and attributes added:
    - Added: [CharacterRange object](../text/characterrange.md)
    - Added: [ParagraphRange object](../text/paragraphrange.md)
    - Added: [ComposedLineRange object](../text/composedlinerange.md)
    - Added: [TextDocument.characterRange()](../text/textdocument.md#textdocumentcharacterrange)
    - Added: [TextDocument.composedLineCharacterIndexesAt()](../text/textdocument.md#textdocumentcomposedlinecharacterindexesat)
    - Added: [TextDocument.composedLineCount](../text/textdocument.md#textdocumentcomposedlinecount)
    - Added: [TextDocument.composedLineRange()](../text/textdocument.md#textdocumentcomposedlinerange)
    - Added: [TextDocument.paragraphCharacterIndexesAt()](../text/textdocument.md#textdocumentparagraphcharacterindexesat)
    - Added: [TextDocument.paragraphCount](../text/textdocument.md#textdocumentparagraphcount)
    - Added: [TextDocument.paragraphRange()](../text/textdocument.md#textdocumentparagraphrange)
    - Changed: [app.purge()](../general/application.md#apppurge) - PurgeTarget.ALL_CACHES now includes the disk cache

### [After Effects 24.2](https://helpx.adobe.com/after-effects/using/whats-new/2024-2.html) (February 2024)

- Scripting methods and attributes added or changed:
    - Added: [LayerCollection.addVerticalText()](../layer/layercollection.md#layercollectionaddverticaltext)
    - Added: [LayerCollection.addVerticalBoxText()](../layer/layercollection.md#layercollectionaddverticalboxtext)
    - Added: [TextDocument.lineOrientation](../text/textdocument.md#textdocumentlineorientation)
    - Added: [FontsObject.fontServerRevision](../text/fontsobject.md#fontsobjectfontserverrevision)
    - Added: [FontsObject.getFontByID()](../text/fontsobject.md#fontsobjectgetfontbyid)
    - Added: [FontObject.fontID](../text/fontobject.md#fontobjectfontid)

### [After Effects 24.0](https://helpx.adobe.com/after-effects/using/whats-new/2024.html) (October 2023)

- Scripting methods and attributes added:
    - Added: [getEnumAsString()](../general/globals.md#getenumasstring)
    - Added: [app.fonts](../general/application.md#appfonts)
    - Added: [Fonts object](../text/fontsobject.md)
    - Added: [FontsObject.allFonts](../text/fontsobject.md#fontsobjectallfonts)
    - Added: [FontsObject.fontsWithDefaultDesignAxes](../text/fontsobject.md#fontsobjectfontswithdefaultdesignaxes)
    - Added: [FontsObject.getFontsByFamilyNameAndStyleName()](../text/fontsobject.md#fontsobjectgetfontsbyfamilynameandstylename)
    - Added: [FontsObject.getFontsByPostScriptName()](../text/fontsobject.md#fontsobjectgetfontsbypostscriptname)
    - Added: [FontsObject.missingOrSubstitutedFonts](../text/fontsobject.md#fontsobjectmissingorsubstitutedfonts)
    - Added: [Font object](../text/fontobject.md)
    - Added: [FontObject.designAxesData](../text/fontobject.md#fontobjectdesignaxesdata)
    - Added: [FontObject.designVector](../text/fontobject.md#fontobjectdesignvector)
    - Added: [FontObject.familyPrefix](../text/fontobject.md#fontobjectfamilyprefix)
    - Added: [FontObject.hasDesignAxes](../text/fontobject.md#fontobjecthasdesignaxes)
    - Added: [FontObject.hasSameDict()](../text/fontobject.md#fontobjecthassamedict)
    - Added: [FontObject.postScriptNameForDesignVector()](../text/fontobject.md#fontobjectpostscriptnamefordesignvector)
    - Added: [FontObject.familyName](../text/fontobject.md#fontobjectfamilyname)
    - Added: [FontObject.fullName](../text/fontobject.md#fontobjectfullname)
    - Added: [FontObject.isFromAdobeFonts](../text/fontobject.md#fontobjectisfromadobefonts)
    - Added: [FontObject.isSubstitute](../text/fontobject.md#fontobjectissubstitute)
    - Added: [FontObject.location](../text/fontobject.md#fontobjectlocation)
    - Added: [FontObject.nativeFamilyName](../text/fontobject.md#fontobjectnativefamilyname)
    - Added: [FontObject.nativeFullName](../text/fontobject.md#fontobjectnativefullname)
    - Added: [FontObject.nativeStyleName](../text/fontobject.md#fontobjectnativestylename)
    - Added: [FontObject.postScriptName](../text/fontobject.md#fontobjectpostscriptname)
    - Added: [FontObject.styleName](../text/fontobject.md#fontobjectstylename)
    - Added: [FontObject.technology](../text/fontobject.md#fontobjecttechnology)
    - Added: [FontObject.type](../text/fontobject.md#fontobjecttype)
    - Added: [FontObject.version](../text/fontobject.md#fontobjectversion)
    - Added: [FontObject.writingScripts](../text/fontobject.md#fontobjectwritingscripts)
    - Added: [TextDocument.autoHyphenate](../text/textdocument.md#textdocumentautohyphenate)
    - Added: [TextDocument.autoKernType](../text/textdocument.md#textdocumentautokerntype)
    - Added: [TextDocument.baselineDirection](../text/textdocument.md#textdocumentbaselinedirection)
    - Added: [TextDocument.composerEngine](../text/textdocument.md#textdocumentcomposerengine)
    - Added: [TextDocument.digitSet](../text/textdocument.md#textdocumentdigitset)
    - Added: [TextDocument.direction](../text/textdocument.md#textdocumentdirection)
    - Added: [TextDocument.endIndent](../text/textdocument.md#textdocumentendindent)
    - Added: [TextDocument.everyLineComposer](../text/textdocument.md#textdocumenteverylinecomposer)
    - Added: [TextDocument.firstLineIndent](../text/textdocument.md#textdocumentfirstlineindent)
    - Added: [TextDocument.fontBaselineOption](../text/textdocument.md#textdocumentfontbaselineoption)
    - Added: [TextDocument.fontCapsOption](../text/textdocument.md#textdocumentfontcapsoption)
    - Added: [TextDocument.fontObject](../text/textdocument.md#textdocumentfontobject)
    - Added: [TextDocument.hangingRoman](../text/textdocument.md#textdocumenthangingroman)
    - Added: [TextDocument.kerning](../text/textdocument.md#textdocumentkerning)
    - Added: [TextDocument.leadingType](../text/textdocument.md#textdocumentleadingtype)
    - Added: [TextDocument.ligature](../text/textdocument.md#textdocumentligature)
    - Added: [TextDocument.lineJoinType](../text/textdocument.md#textdocumentlinejointype)
    - Added: [TextDocument.noBreak](../text/textdocument.md#textdocumentnobreak)
    - Added: [TextDocument.spaceAfter](../text/textdocument.md#textdocumentspaceafter)
    - Added: [TextDocument.spaceBefore](../text/textdocument.md#textdocumentspacebefore)
    - Added: [TextDocument.startIndent](../text/textdocument.md#textdocumentstartindent)
- Scripting attributes updated:
    - Updated: [TextDocument.fauxBold](../text/textdocument.md#textdocumentfauxbold)
    - Updated: [TextDocument.fauxItalic](../text/textdocument.md#textdocumentfauxitalic)
    - Updated: [TextDocument.justification](../text/textdocument.md#textdocumentjustification)

---

## After Effects 23

### [After Effects 23.0](https://helpx.adobe.com/after-effects/using/whats-new/2023.html) (October 2022)

- Scripting methods and attributes added:
    - Added: [AVLayer.setTrackMatte()](../layer/avlayer.md#avlayersettrackmatte)
    - Added: [AVLayer.removeTrackMatte()](../layer/avlayer.md#avlayerremovetrackmatte)
    - Added: [AVLayer.trackMatteLayer](../layer/avlayer.md#avlayertrackmattelayer)
- Scripting attributes updated:
    - Updated: [AVLayer.trackMatteType](../layer/avlayer.md#avlayertrackmattetype)
    - Updated: [AVLayer.isTrackMatte](../layer/avlayer.md#avlayeristrackmatte)
    - Updated: [AVLayer.hasTrackMatte](../layer/avlayer.md#avlayerhastrackmatte)

---

## After Effects 22

### [After Effects 22.6](https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html) (August 2022)

- Scripting methods added:
    - Added: [Property.keyLabel()](../property/property.md#propertykeylabel)
    - Added: [Property.setLabelAtKey()](../property/property.md#propertysetlabelatkey)

### [After Effects 22.3](https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html) (April 2022)

- Scripting methods added:
    - Added: [Layer.doSceneEditDetection()](../layer/layer.md#layerdosceneeditdetection)


### [After Effects 22.0](https://helpx.adobe.com/after-effects/using/whats-new/2022.html) (October 2021)

- Scripting methods added:
    - Added: [Layer.id](../layer/layer.md#layerid)
    - Added: [Project.layerByID()](../general/project.md#projectlayerbyid)
    - Added: [Property.essentialPropertySource](../property/property.md#propertyessentialpropertysource)
- Scripting Access to Render Queue Notifications:
    - Added: [RenderQueue.queueNotify](../renderqueue/renderqueue.md#renderqueuequeuenotify)
    - Added: [RenderQueueItem.queueItemNotify](../renderqueue/renderqueueitem.md#renderqueueitemqueueitemnotify)
- Scripting Access to Multi-Frame Rendering, Maximum CPU Percentage Overrides:
    - Added: [app.setMultiFrameRenderingConfig()](../general/application.md#appsetmultiframerenderingconfig)

---

## After Effects 18

### [After Effects 18.0](https://helpx.adobe.com/after-effects/using/whats-new/2021-2.html) (March 2021)

- Scripting methods and attributes to support Media Replacement:
    - Added: [AVItem.isMediaReplacementCompatible](../item/avitem.md#avitemismediareplacementcompatible)
    - Added: [AVLayer.addToMotionGraphicsTemplate()](../layer/avlayer.md#avlayeraddtomotiongraphicstemplate)
    - Added: [AVLayer.addToMotionGraphicsTemplateAs()](../layer/avlayer.md#avlayeraddtomotiongraphicstemplateas)
    - Added: [AVLayer.canAddToMotionGraphicsTemplate()](../layer/avlayer.md#avlayercanaddtomotiongraphicstemplate)
    - Added: [Property.alternateSource](../property/property.md#propertyalternatesource)
    - Added: [Property.canSetAlternateSource](../property/property.md#propertycansetalternatesource)
    - Added: [Property.setAlternateSource()](../property/property.md#propertysetalternatesource)
    - Added relevant [match names](../matchnames/layer/avlayer.md)
- Added [match name for Essential Properties](../matchnames/layer/avlayer.md) property group.

---

## After Effects 17

### [After Effects 17.1.1](https://helpx.adobe.com/after-effects/using/whats-new/2020-1.html) (May 2020)

- Scripting access to Shape Layer Stroke Taper, Stroke Waves, Offset Paths Copies, Offset Path Copy Offset:
    - Added relevant [match names](../matchnames/layer/shapelayer.md)
- Fixed an issue to allow negative values for [CompItem.displayStartTime](../item/compitem.md#compitemdisplaystarttime):
    - Added [CompItem.displayStartFrame](../item/compitem.md#compitemdisplaystartframe)
    - Now matches the valid range allowed when setting the Start Timecode in the Composition Settings Dialog (-3:00:00:00 to 23:59:00:00).

### [After Effects 17.0.1](https://helpx.adobe.com/after-effects/using/whats-new/2020.html) (November 2019)

- Scripted creation and modification of Dropdown Menu Control items:
    - Added: [Property.isDropdownEffect](../property/property.md#propertyisdropdowneffect)
    - Added: [Property.setPropertyParameters()](../property/property.md#propertysetpropertyparameters)

---

## After Effects 16

### After Effects 16.1

- Scripting access to [ViewOptions object](../other/viewoptions.md) guide and ruler booleans:
    - Added: [ViewOptions.guidesLocked](../other/viewoptions.md#viewoptionsguideslocked)
    - Added: [ViewOptions.guidesSnap](../other/viewoptions.md#viewoptionsguidessnap)
    - Added: [ViewOptions.guidesVisibility](../other/viewoptions.md#viewoptionsguidesvisibility)
    - Added: [ViewOptions.rulers](../other/viewoptions.md#viewoptionsrulers)
- Scripting access to add, remove, and set existing guides:
    - Added: [Item.addGuide()](../item/item.md#itemaddguide)
    - Added: [Item.removeGuide()](../item/item.md#itemremoveguide)
    - Added: [Item.setGuide()](../item/item.md#itemsetguide)
- Scripting access to additional EGP property attributes:
    - Added: [CompItem.motionGraphicsTemplateControllerCount](../item/compitem.md#compitemmotiongraphicstemplatecontrollercount)
    - Added: [CompItem.getMotionGraphicsTemplateControllerName()](../item/compitem.md#compitemgetmotiongraphicstemplatecontrollername)
    - Added: [CompItem.setMotionGraphicsControllerName()](../item/compitem.md#compitemsetmotiongraphicscontrollername)
    - Added: [Property.addToMotionGraphicsTemplateAs()](../property/property.md#propertyaddtomotiongraphicstemplateas)

### [After Effects 16.0](https://helpx.adobe.com/after-effects/using/whats-new/2019.html) (October 2018)

- Scripting access to marker label and protectedRegion attributes:
    - Added: [MarkerValue.label](../other/markervalue.md#markervaluelabel)
    - Added: [MarkerValue.protectedRegion](../other/markervalue.md#markervalueprotectedregion)
- Scripting access to additional project color management settings:
    - Added: [Project.workingSpace](../general/project.md#projectworkingspace)
    - Added: [Project.workingGamma](../general/project.md#projectworkinggamma)
    - Added: [Project.listColorProfiles()](../general/project.md#projectlistcolorprofiles)
    - Added: [Project.linearizeWorkingSpace](../general/project.md#projectlinearizeworkingspace)
    - Added: [Project.compensateForSceneReferredProfiles](../general/project.md#projectcompensateforscenereferredprofiles)
- Scripting access to the expression engine attribute:
    - Added: [Project.expressionEngine](../general/project.md#projectexpressionengine)
- Added project method [Project.setDefaultImportFolder()](../general/project.md#projectsetdefaultimportfolder), which sets the folder that will be shown in the file import dialog.
- Added app property [app.disableRendering](../general/application.md#appdisablerendering), which disables rendering via the same mechanism as the Caps Lock key.

---

## After Effects 15

### [After Effects 15.1](https://helpx.adobe.com/after-effects/using/whats-new/2018.html) (April 2018)

- [Project.autoFixExpressions()](../general/project.md#projectautofixexpressions) will now fix expression name references in single quotes (ex., ('Effect Name')), as well as double quotes.
- Fixes [CompItem.exportAsMotionGraphicsTemplate()](../item/compitem.md#compitemexportasmotiongraphicstemplate) not returning a boolean as expected

### [After Effects 15.0](https://forums.adobe.com/docs/DOC-8872) (October 2017)

- Scripting Access to motion graphics templates:
    - Added: [CompItem.motionGraphicsTemplateName](../item/compitem.md#compitemmotiongraphicstemplatename)
    - Added: [CompItem.exportAsMotionGraphicsTemplate()](../item/compitem.md#compitemexportasmotiongraphicstemplate)
    - Added: [CompItem.openInEssentialGraphics()](../item/compitem.md#compitemopeninessentialgraphics)
    - Added: [Property.addToMotionGraphicsTemplate()](../property/property.md#propertyaddtomotiongraphicstemplate)
    - Added: [Property.canAddToMotionGraphicsTemplate()](../property/property.md#propertycanaddtomotiongraphicstemplate)

---

## After Effects 14

### [After Effects 14.2.1 (CC 2017.2)](https://blogs.adobe.com/creativecloud/a-june-2017-update-to-after-effects-cc-is-now-available/) (June 2017)

- Buttons in ScriptUI panels have been reverted to the rectangular appearance seen in After Effects 14.1 and previous releases.
- The [AVItem.setProxyToNone()](../item/avitem.md#avitemsetproxytonone) scripting method no longer fails with an error message, "After Effects error: AEGP trying to add invalid footage".
- The [System.callSystem()](../general/system.md#systemcallsystem) scripting method now waits for all tasks called by the command to complete, instead of failing when the command takes a long time to complete.

### [After Effects 14.2 (CC 2017.1)](https://blogs.adobe.com/creativecloud/after-effects-cc-april-2017-in-depth-scripting-improvements/) (April 2017)

- Scripting Access to text leading:
    - Added: [TextDocument.leading](../text/textdocument.md#textdocumentleading)
- Scripting Access to Team Projects (Beta):
    - Added: [Project.newTeamProject()](../general/project.md#projectnewteamproject)
    - Added: [Project.openTeamProject()](../general/project.md#projectopenteamproject)
    - Added: [Project.shareTeamProject()](../general/project.md#projectshareteamproject)
    - Added: [Project.syncTeamProject()](../general/project.md#projectsyncteamproject)
    - Added: [Project.closeTeamProject()](../general/project.md#projectcloseteamproject)
    - Added: [Project.convertTeamProjectToProject()](../general/project.md#projectconvertteamprojecttoproject)
    - Added: [Project.listTeamProjects()](../general/project.md#projectlistteamprojects)
    - Added: [Project.isTeamProjectOpen()](../general/project.md#projectisteamprojectopen)
    - Added: [Project.isAnyTeamProjectOpen()](../general/project.md#projectisanyteamprojectopen)
    - Added: [Project.isTeamProjectEnabled()](../general/project.md#projectisteamprojectenabled)
    - Added: [Project.isLoggedInToTeamProject()](../general/project.md#projectisloggedintoteamproject)
    - Added: [Project.isSyncCommandEnabled()](../general/project.md#projectissynccommandenabled)
    - Added: [Project.isShareCommandEnabled()](../general/project.md#projectissharecommandenabled)
    - Added: [Project.isResolveCommandEnabled()](../general/project.md#projectisresolvecommandenabled)
    - Added: [Project.resolveConflict()](../general/project.md#projectresolveconflict)
- Drop-down menus in ScriptUI panels are no longer clipped on HiDPI displays on Windows.
- The appearance of buttons, sliders, disclosure triangles ("twirly arrow"), scroll bar, progress bar, radio buttons, and checkboxes in ScriptUI embedded panels have been updated to match the appearance of After Effects native controls.
- After Effects no longer crashes when the [AVLayer.compPointToSource()](../layer/avlayer.md#avlayercomppointtosource) scripting method is used with a 3D text layer.
- The match name of the Fast Box Blur effect is "ADBE Box Blur2". The older match name "ADBE Box Blur" will continue to work: when used to add the effect, "ADBE Box Blur" will apply the Fast Box Blur effect, but with the older name "Box Blur"; the Iterations parameter will be set to the new default of 3.

### [After Effects 14.0 (CC 2017)](https://forums.adobe.com/message/9108589) (November 2016)

- Scripting Access to Tools:
    - Added: [Project.toolType](../general/project.md#projecttooltype)
- Scripting Access to Composition Markers:
    - Added: [CompItem.markerProperty](../item/compitem.md#compitemmarkerproperty)
- Scripting Access to Queue in AME:
    - Added: [RenderQueue.queueInAME()](../renderqueue/renderqueue.md#renderqueuequeueiname)
- Scripting Access to Available GPU Acceleration Options:
    - Added: [app.availableGPUAccelTypes](../general/application.md#appavailablegpuacceltypes)

---

## After Effects 13

### [After Effects 13.8 (CC 2015.3)](https://blogs.adobe.com/creativecloud/after-effects-cc-2015-3-in-depth-gpu-accelerated-effects/) (June 2016)

- Enable GPU effect rendering via scripting:
    - Added: [Project.gpuAccelType](../general/project.md#projectgpuacceltype)
- New Gaussian Blur effect added w/ matchname `ADBE Gaussian Blur 2`

### [After Effects 13.6 (CC 2015)](https://blogs.adobe.com/creativecloud/whats-new-and-changed-in-the-upcoming-update-to-after-effects-cc-2015/) (November 2015)

- Scripting access to text baselines:
    - Added: [baselineLocs](../text/textdocument.md#textdocumentbaselinelocs)
- New scripting method to generate random numbers:
    - Added: [generateRandomNumber()](../general/globals.md#generaterandomnumber)
- Using the [copyToComp()](../layer/layer.md#layercopytocomp) scripting method no longer causes After Effects to crash when the layer has a parent.
- The [valueAtTime()](../property/property.md#propertyvalueattime) scripting method now waits for time-intensive expressions, like `sampleImage`, to finish evaluating before it returns the result.
- ScriptUI panels now display and resize correctly on high-DPI displays on Windows.
- After Effects no longer crashes when you click OK or Cancel buttons in a scriptUI dialog with tabbed panels.

### [After Effects 13.2 (CC 2014.2)](https://blogs.adobe.com/creativecloud/after-effects-cc-2014-2-13-2/) (December 2014)

- Scripting improvements for text layers (read-only):
    - Returns boolean value:
        - Added: [fauxBold](../text/textdocument.md#textdocumentfauxbold)
        - Added: [fauxItalic](../text/textdocument.md#textdocumentfauxitalic)
        - Added: [allCaps](../text/textdocument.md#textdocumentallcaps)
        - Added: [smallCaps](../text/textdocument.md#textdocumentsmallcaps)
        - Added: [superscript](../text/textdocument.md#textdocumentsuperscript)
        - Added: [subscript](../text/textdocument.md#textdocumentsubscript)
    - Returns float:
        - Added: [verticalScale](../text/textdocument.md#textdocumentverticalscale)
        - Added: [horizontalScale](../text/textdocument.md#textdocumenthorizontalscale)
        - Added: [baselineShift](../text/textdocument.md#textdocumentbaselineshift)
        - Added: [tsume](../text/textdocument.md#textdocumenttsume)
    - Returns array of ([X,Y]) position coordinates (paragraph text layers only):
        - Added: [boxTextPos](../text/textdocument.md#textdocumentboxtextpos)
- Layer space / comp space conversion:
    - Added: [sourcePointToComp()](../layer/avlayer.md#avlayersourcepointtocomp)
    - Added: [compPointToSource()](../layer/avlayer.md#avlayercomppointtosource)

### [After Effects 13.1 (CC 2014.1)](https://blogs.adobe.com/creativecloud/after-effects-cc-2014-1-13-1/) (September 2014)

- Scripting improvements for text layers (read-only):
    - returns string:
        - Added: [fontLocation](../text/textdocument.md#textdocumentfontlocation)
        - Added: [fontStyle](../text/textdocument.md#textdocumentfontstyle)
        - Added: [fontFamily](../text/textdocument.md#textdocumentfontfamily)
- "Use Legacy UI" toggle implemented

---

### [After Effects 13.0 (CC 2014)](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/) (June 2014)

- Scripting access to render settings and output module settings:
    - Added: RenderQueueItem object [getSetting](../renderqueue/renderqueueitem.md#renderqueueitemgetsetting), [setSetting](../renderqueue/renderqueueitem.md#renderqueueitemsetsetting) methods
    - Added: RenderQueueItem object [getSettings](../renderqueue/renderqueueitem.md#renderqueueitemgetsettings), [setSettings](../renderqueue/renderqueueitem.md#renderqueueitemsetsettings) methods
    - Added: OutputModule object [getSetting](../renderqueue/outputmodule.md#outputmodulegetsetting), [setSetting](../renderqueue/outputmodule.md#outputmodulesetsetting) methods
    - Added: OutputModule object [getSettings](../renderqueue/outputmodule.md#outputmodulegetsettings), [setSettings](../renderqueue/outputmodule.md#outputmodulesetsettings) methods
- Fetch project item by id: [Project.itemByID()](../general/project.md#projectitembyid)
- CEP panels implemented

---

## After Effects 12

### [After Effects 12.0 (CC)](https://blogs.adobe.com/creativecloud/scripting-changes-in-after-effects-cc-12-0-12-2/) (June 2013)

- Access to effect's internal version string:
    - Added: Application effects object's version attribute, see [app.effects](../general/application.md#appeffects)
- Ability to get and set preview mode:
    - Added: [ViewOptions.fastPreview](../other/viewoptions.md#viewoptionsfastpreview)
- Access to layer sampling method (see [samplingQuality](../layer/avlayer.md#avlayersamplingquality))
- Changed preference and settings methods (see [Settings object](../other/settings.md))
- ScriptUI is now based on the same controls as the main application.

---

## After Effects 11

### [After Effects 11.0 (CS6)](https://web.archive.org/web/20120623073355/https://blogs.adobe.com/toddkopriva/2012/06/scripting-changes-in-after-effects-cs6-plus-new-scripting-guide.html/) (April 2012)

- Added: Access to [Viewer object](../other/viewer.md) object and controls:
    - Added: [app.activeViewer](../general/application.md#appactiveviewer)
    - Added: [AVLayer.openInViewer()](../layer/avlayer.md#avlayeropeninviewer) to open a layer in the layer viewer
    - Added: [CompItem.openInViewer()](../item/compitem.md#compitemopeninviewer) to open a composition in the composition viewer
    - Added: [FootageItem.openInViewer()](../item/footageitem.md#footageitemopeninviewer) to open a footage item in the footage viewer
- Added: [Property.canSetExpression](../property/property.md#propertycansetexpression)
- Added: [AVLayer.environmentLayer](../layer/avlayer.md#avlayerenvironmentlayer)
- Added: [MaskPropertyGroup.maskFeatherFalloff](../property/maskpropertygroup.md#maskpropertygroupmaskfeatherfalloff)
- Access to Shape Feather properties via scripting:
    - Added: [Shape.featherSegLocs](../other/shape.md#shapefeatherseglocs)
    - Added: [Shape.featherRelSegLocs](../other/shape.md#shapefeatherrelseglocs)
    - Added: [Shape.featherRadii](../other/shape.md#shapefeatherradii)
    - Added: [Shape.featherInterps](../other/shape.md#shapefeatherinterps)
    - Added: [Shape.featherTensions](../other/shape.md#shapefeathertensions)
    - Added: [Shape.featherTypes](../other/shape.md#shapefeathertypes)
    - Added: [Shape.featherRelCornerAngles](../other/shape.md#shapefeatherrelcornerangles)

---

## After Effects 10

### [After Effects 10.5 (CS5.5)](https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/) (April 2011)

- Added to the [Project object](../general/project.md) object:
    - [Project.framesCountType](../general/project.md#projectframescounttype)
    - [Project.feetFramesFilmType](../general/project.md#projectfeetframesfilmtype)
    - [Project.framesUseFeetFrames](../general/project.md#projectframesusefeetframes)
    - [Project.footageTimecodeDisplayStartType](../general/project.md#projectfootagetimecodedisplaystarttype)
    - [Project.timeDisplayType](../general/project.md#projecttimedisplaytype)
- Removed from the [Project object](../general/project.md) object:
    - `timecodeDisplayType` attribute
    - `timecodeBaseType` attribute
    - `timecodeNTSCDropFrame` attribute
    - `timecodeFilmType` attribute
    - `TimecodeDisplayType` enum
    - `TimecodeFilmType` enum
    - `TimecodeBaseType` enum
- Added: [CompItem.dropFrame](../item/compitem.md#compitemdropframe)
- Added support for Paragraph Box Text:
    - Added [LayerCollection.addBoxText()](../layer/layercollection.md#layercollectionaddboxtext)
    - Added [TextDocument.boxText](../text/textdocument.md#textdocumentboxtext)
    - Added [TextDocument.pointText](../text/textdocument.md#textdocumentpointtext)
    - Added [TextDocument.boxTextSize](../text/textdocument.md#textdocumentboxtextsize)
- Added [LightLayer.lightType](../layer/lightlayer.md#lightlayerlighttype)

---

## After Effects 9

### [After Effects 9.0 (CS4)](https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/) (September 2008)

- Added: [app.isoLanguage](../general/application.md#appisolanguage)
- Added: [MarkerValue.duration](../other/markervalue.md#markervalueduration)
- Added: [OutputModule.includeSourceXMP](../renderqueue/outputmodule.md#outputmoduleincludesourcexmp)
- Added: [Project.xmpPacket](../general/project.md#projectxmppacket)
- Added the following Property methods and attributes related to the Separate Dimensions feature:
    - [Property.dimensionsSeparated](../property/property.md#propertydimensionsseparated)
    - [Property.getSeparationFollower()](../property/property.md#propertygetseparationfollower)
    - [Property.isSeparationFollower](../property/property.md#propertyisseparationfollower)
    - [Property.isSeparationLeader](../property/property.md#propertyisseparationleader)
    - [Property.separationDimension](../property/property.md#propertyseparationdimension)
    - [Property.separationLeader](../property/property.md#propertyseparationleader)
- Added [TextDocument object](../text/textdocument.md) access, including:
    - Added: [TextDocument.applyFill](../text/textdocument.md#textdocumentapplyfill)
    - Added: [TextDocument.applyStroke](../text/textdocument.md#textdocumentapplystroke)
    - Added: [TextDocument.fillColor](../text/textdocument.md#textdocumentfillcolor)
    - Added: [TextDocument.font](../text/textdocument.md#textdocumentfont)
    - Added: [TextDocument.fontSize](../text/textdocument.md#textdocumentfontsize)
    - Added: [TextDocument.justification](../text/textdocument.md#textdocumentjustification)
    - Added: [TextDocument.resetCharStyle()](../text/textdocument.md#textdocumentresetcharstyle)
    - Added: [TextDocument.resetParagraphStyle()](../text/textdocument.md#textdocumentresetparagraphstyle)
    - Added: [TextDocument.strokeColor](../text/textdocument.md#textdocumentstrokecolor)
    - Added: [TextDocument.strokeOverFill](../text/textdocument.md#textdocumentstrokeoverfill)
    - Added: [TextDocument.strokeWidth](../text/textdocument.md#textdocumentstrokewidth)
