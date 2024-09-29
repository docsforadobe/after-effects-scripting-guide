# Changelog

What’s new and changed for scripting?

---

## [After Effects 25.0 Beta build 26](https://community.adobe.com/t5/after-effects-beta-discussions/new-in-ae-25-0-build-25-scripting-hooks-for-font-fallback-management/m-p/14809794) (August 2024)

- Scripting methods and attributes added
  : - Added: [CharacterRange.pasteFrom()](../text/characterrange.md#characterrange-pastefrom)
    - Added: [FontObject.hasGlyphsFor()](../text/fontobject.md#fontobject-hasglyphsfor)
    - Added: [FontObject.otherFontsWithSameDict()](../text/fontobject.md#fontobject-otherfontswithsamedict)
    - Added: [FontsObject.getCTScriptForString()](../text/fontsobject.md#fontsobject-getctscriptforstring)
    - Added: [FontsObject.getDefaultFontForCTScript()](../text/fontsobject.md#fontsobject-getdefaultfontforctscript)
    - Added: [FontsObject.setDefaultFontForCTScript()](../text/fontsobject.md#fontsobject-setdefaultfontforctscript)

## [After Effects 24.6](https://helpx.adobe.com/after-effects/using/whats-new/2024-6.html) (August 2024)

- Scripting methods and attributes added
  : - Added: [FontsObject.favoriteFontFamilyList](../text/fontsobject.md#fontsobject-favoritefontfamilylist)
    - Added: [FontsObject.fontsDuplicateByPostScriptName](../text/fontsobject.md#fontsobject-fontsduplicatebypostscriptname)
    - Added: [FontsObject.freezeSyncSubstitutedFonts](../text/fontsobject.md#fontsobject-freezesyncsubstitutedfonts)
    - Added: [FontsObject.mruFontFamilyList](../text/fontsobject.md#fontsobject-mrufontfamilylist)
    - Added: [FontsObject.substitutedFontReplacementMatchPolicy](../text/fontsobject.md#fontsobject-substitutedfontreplacementmatchpolicy)
    - Added: [FontsObject.pollForAndPushNonSystemFontFoldersChanges()](../text/fontsobject.md#fontsobject-pollforandpushnonsystemfontfolderschanges)
    - Added: [TextDocument.boxAutoFitPolicy](../text/textdocument.md#textdocument-boxautofitpolicy)
    - Added: [TextDocument.boxFirstBaselineAlignment](../text/textdocument.md#textdocument-boxfirstbaselinealignment)
    - Added: [TextDocument.boxFirstBaselineAlignmentMinimum](../text/textdocument.md#textdocument-boxfirstbaselinealignmentminimum)
    - Added: [TextDocument.boxInsetSpacing](../text/textdocument.md#textdocument-boxinsetspacing)
    - Added: [TextDocument.boxOverflow](../text/textdocument.md#textdocument-boxoverflow)
    - Added: [TextDocument.boxVerticalAlignment](../text/textdocument.md#textdocument-boxverticalalignment)

## [After Effects 24.5](https://helpx.adobe.com/after-effects/using/whats-new/2024-5.html) (May 2024)

- Scripting methods and attributes added
  : - Added: [Project.replaceFont()](../general/project.md#project-replacefont)
    - Added: [Project.usedFonts](../general/project.md#project-usedfonts)

## [After Effects 24.4 Beta build 25](https://community.adobe.com/t5/after-effects-beta-discussions/scripting-new-api-for-3d-model-layers/td-p/14580044) (March 2024)

> - Added: [ThreeDModelLayer object](../layers/threedmodellayer.md#threedmodellayer)

## [After Effects 24.3](https://helpx.adobe.com/after-effects/using/whats-new/2024-3.html) (March 2024)

- Scripting methods and attributes added
  : - Added: [CharacterRange object](../text/characterrange.md#characterrange)
    - Added: [ParagraphRange object](../text/paragraphrange.md#paragraphrange)
    - Added: [ComposedLineRange object](../text/composedlinerange.md#composedlinerange)
    - Added: [TextDocument.characterRange()](../text/textdocument.md#textdocument-characterrange)
    - Added: [TextDocument.composedLineCharacterIndexesAt()](../text/textdocument.md#textdocument-composedlinecharacterindexesat)
    - Added: [TextDocument.composedLineCount](../text/textdocument.md#textdocument-composedlinecount)
    - Added: [TextDocument.composedLineRange()](../text/textdocument.md#textdocument-composedlinerange)
    - Added: [TextDocument.paragraphCharacterIndexesAt()](../text/textdocument.md#textdocument-paragraphcharacterindexesat)
    - Added: [TextDocument.paragraphCount](../text/textdocument.md#textdocument-paragraphcount)
    - Added: [TextDocument.paragraphRange()](../text/textdocument.md#textdocument-paragraphrange)
    - Changed: [app.purge()](../general/application.md#app-purge) - PurgeTarget.ALL_CACHES now includes the disk cache

## [After Effects 24.2](https://helpx.adobe.com/after-effects/using/whats-new/2024-2.html) (February 2024)

- Scripting methods and attributes added or changed
  : - Added: [LayerCollection.addVerticalText()](../layers/layercollection.md#layercollection-addverticaltext)
    - Added: [LayerCollection.addVerticalBoxText()](../layers/layercollection.md#layercollection-addverticalboxtext)
    - Added: [TextDocument.lineOrientation](../text/textdocument.md#textdocument-lineorientation)
    - Added: [FontsObject.fontServerRevision](../text/fontsobject.md#fontsobject-fontserverrevision)
    - Added: [FontsObject.getFontByID()](../text/fontsobject.md#fontsobject-getfontbyid)
    - Added: [FontObject.fontID](../text/fontobject.md#fontobject-fontid)

## [After Effects 24.0](https://helpx.adobe.com/after-effects/using/whats-new/2024.html) (October 2023)

- Scripting methods and attributes added
  : - Added: [getEnumAsString()](../general/globals.md#getenumasstring)
    - Added: [app.fonts](../general/application.md#app-fonts)
    - Added: [Fonts object](../text/fontsobject.md#fontsobject)
    - Added: [FontsObject.allFonts](../text/fontsobject.md#fontsobject-allfonts)
    - Added: [FontsObject.fontsWithDefaultDesignAxes](../text/fontsobject.md#fontsobject-fontswithdefaultdesignaxes)
    - Added: [FontsObject.getFontsByFamilyNameAndStyleName()](../text/fontsobject.md#fontsobject-getfontsbyfamilynameandstylename)
    - Added: [FontsObject.getFontsByPostScriptName()](../text/fontsobject.md#fontsobject-getfontsbypostscriptname)
    - Added: [FontsObject.missingOrSubstitutedFonts](../text/fontsobject.md#fontsobject-missingorsubstitutedfonts)
    - Added: [Font object](../text/fontobject.md#fontobject)
    - Added: [FontObject.designAxesData](../text/fontobject.md#fontobject-designaxesdata)
    - Added: [FontObject.designVector](../text/fontobject.md#fontobject-designvector)
    - Added: [FontObject.familyPrefix](../text/fontobject.md#fontobject-familyprefix)
    - Added: [FontObject.hasDesignAxes](../text/fontobject.md#fontobject-hasdesignaxes)
    - Added: [FontObject.hasSameDict()](../text/fontobject.md#fontobject-hassamedict)
    - Added: [FontObject.postScriptNameForDesignVector()](../text/fontobject.md#fontobject-postscriptnamefordesignvector)
    - Added: [FontObject.familyName](../text/fontobject.md#fontobject-familyname)
    - Added: [FontObject.fullName](../text/fontobject.md#fontobject-fullname)
    - Added: [FontObject.isFromAdobeFonts](../text/fontobject.md#fontobject-isfromadobefonts)
    - Added: [FontObject.isSubstitute](../text/fontobject.md#fontobject-issubstitute)
    - Added: [FontObject.location](../text/fontobject.md#fontobject-location)
    - Added: [FontObject.nativeFamilyName](../text/fontobject.md#fontobject-nativefamilyname)
    - Added: [FontObject.nativeFullName](../text/fontobject.md#fontobject-nativefullname)
    - Added: [FontObject.nativeStyleName](../text/fontobject.md#fontobject-nativestylename)
    - Added: [FontObject.postScriptName](../text/fontobject.md#fontobject-postscriptname)
    - Added: [FontObject.styleName](../text/fontobject.md#fontobject-stylename)
    - Added: [FontObject.technology](../text/fontobject.md#fontobject-technology)
    - Added: [FontObject.type](../text/fontobject.md#fontobject-type)
    - Added: [FontObject.version](../text/fontobject.md#fontobject-version)
    - Added: [FontObject.writingScripts](../text/fontobject.md#fontobject-writingscripts)
    - Added: [TextDocument.autoHyphenate](../text/textdocument.md#textdocument-autohyphenate)
    - Added: [TextDocument.autoKernType](../text/textdocument.md#textdocument-autokerntype)
    - Added: [TextDocument.baselineDirection](../text/textdocument.md#textdocument-baselinedirection)
    - Added: [TextDocument.composerEngine](../text/textdocument.md#textdocument-composerengine)
    - Added: [TextDocument.digitSet](../text/textdocument.md#textdocument-digitset)
    - Added: [TextDocument.direction](../text/textdocument.md#textdocument-direction)
    - Added: [TextDocument.endIndent](../text/textdocument.md#textdocument-endindent)
    - Added: [TextDocument.everyLineComposer](../text/textdocument.md#textdocument-everylinecomposer)
    - Added: [TextDocument.firstLineIndent](../text/textdocument.md#textdocument-firstlineindent)
    - Added: [TextDocument.fontBaselineOption](../text/textdocument.md#textdocument-fontbaselineoption)
    - Added: [TextDocument.fontCapsOption](../text/textdocument.md#textdocument-fontcapsoption)
    - Added: [TextDocument.fontObject](../text/textdocument.md#textdocument-fontobject)
    - Added: [TextDocument.hangingRoman](../text/textdocument.md#textdocument-hangingroman)
    - Added: [TextDocument.kerning](../text/textdocument.md#textdocument-kerning)
    - Added: [TextDocument.leadingType](../text/textdocument.md#textdocument-leadingtype)
    - Added: [TextDocument.ligature](../text/textdocument.md#textdocument-ligature)
    - Added: [TextDocument.lineJoinType](../text/textdocument.md#textdocument-linejointype)
    - Added: [TextDocument.noBreak](../text/textdocument.md#textdocument-nobreak)
    - Added: [TextDocument.spaceAfter](../text/textdocument.md#textdocument-spaceafter)
    - Added: [TextDocument.spaceBefore](../text/textdocument.md#textdocument-spacebefore)
    - Added: [TextDocument.startIndent](../text/textdocument.md#textdocument-startindent)
- Scripting attributes updated
  : - Updated: [TextDocument.fauxBold](../text/textdocument.md#textdocument-fauxbold)
    - Updated: [TextDocument.fauxItalic](../text/textdocument.md#textdocument-fauxitalic)
    - Updated: [TextDocument.justification](../text/textdocument.md#textdocument-justification)

## [After Effects 23.0](https://helpx.adobe.com/after-effects/using/whats-new/2023.html) (October 2022)

- Scripting methods and attributes added
  : - Added: [AVLayer.setTrackMatte()](../layers/avlayer.md#avlayer-settrackmatte)
    - Added: [AVLayer.removeTrackMatte()](../layers/avlayer.md#avlayer-removetrackmatte)
    - Added: [AVLayer.trackMatteLayer](../layers/avlayer.md#avlayer-trackmattelayer)
- Scripting attributes updated
  : - Updated: [AVLayer.trackMatteType](../layers/avlayer.md#avlayer-trackmattetype)
    - Updated: [AVLayer.isTrackMatte](../layers/avlayer.md#avlayer-istrackmatte)
    - Updated: [AVLayer.hasTrackMatte](../layers/avlayer.md#avlayer-hastrackmatte)

## [After Effects 22.6](https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html) (August 2022)

- Scripting methods added
  : - Added: [Property.keyLabel()](../properties/property.md#property-keylabel)
    - Added: [Property.setLabelAtKey()](../properties/property.md#property-setlabelatkey)

## [After Effects 22.3](https://helpx.adobe.com/after-effects/using/whats-new/2022-2.html) (April 2022)

- Scripting methods added
  : - Added: [Layer.doSceneEditDetection()](../layers/layer.md#layer-dosceneeditdetection)

---

## [After Effects 22.0](https://helpx.adobe.com/after-effects/using/whats-new/2022.html) (October 2021)

- Scripting methods added
  : - Added: [Layer.id](../layers/layer.md#layer-id)
    - Added: [Project.layerByID()](../general/project.md#project-layerbyid)
    - Added: [Property.essentialPropertySource](../properties/property.md#property-essentialpropertysource)
- Scripting Access to Render Queue Notifications
  : - Added: [RenderQueue.queueNotify](../renderqueue/renderqueue.md#renderqueue-queuenotify)
    - Added: [RenderQueueItem.queueItemNotify](../renderqueue/renderqueueitem.md#renderqueueitem-queueitemnotify)
- Scripting Access to Multi-Frame Rendering, Maximum CPU Percentage Overrides
  : - Added: [app.setMultiFrameRenderingConfig()](../general/application.md#app-setmultiframerenderingconfig)

---

## [After Effects 18.0](https://helpx.adobe.com/after-effects/using/whats-new/2021-2.html) (March 2021)

- Scripting methods and attributes to support Media Replacement
  : - Added: [AVItem.isMediaReplacementCompatible](../items/avitem.md#avitem-ismediareplacementcompatible)
    - Added: [AVLayer.addToMotionGraphicsTemplate()](../layers/avlayer.md#avlayer-addtomotiongraphicstemplate)
    - Added: [AVLayer.addToMotionGraphicsTemplateAs()](../layers/avlayer.md#avlayer-addtomotiongraphicstemplateas)
    - Added: [AVLayer.canAddToMotionGraphicsTemplate()](../layers/avlayer.md#avlayer-canaddtomotiongraphicstemplate)
    - Added: [Property.alternateSource](../properties/property.md#property-alternatesource)
    - Added: [Property.canSetAlternateSource](../properties/property.md#property-cansetalternatesource)
    - Added: [Property.setAlternateSource()](../properties/property.md#property-setalternatesource)
    - Added relevant [match names](../matchnames/layer/avlayer.md#matchnames-layer-avlayer)
- Added [match name for Essential Properties](../matchnames/layer/avlayer.md#matchnames-layer-avlayer) property group.

---

## [After Effects 17.1.1](https://helpx.adobe.com/after-effects/using/whats-new/2020-1.html) (May 2020)

- Scripting access to Shape Layer Stroke Taper, Stroke Waves, Offset Paths Copies, Offset Path Copy Offset
  : - Added relevant [match names](../matchnames/layer/shapelayer.md#matchnames-layer-shapelayer)
- Fixed an issue to allow negative values for [CompItem.displayStartTime](../items/compitem.md#compitem-displaystarttime):
  : - Added [CompItem.displayStartFrame](../items/compitem.md#compitem-displaystartframe)
    - Now matches the valid range allowed when setting the Start Timecode in the Composition Settings Dialog (-3:00:00:00 to 23:59:00:00).

---

## [After Effects 17.0.1](https://helpx.adobe.com/after-effects/using/whats-new/2020.html) (November 2019)

- Scripted creation and modification of Dropdown Menu Control items:
  : - Added: [Property.isDropdownEffect](../properties/property.md#property-isdropdowneffect)
    - Added: [Property.setPropertyParameters()](../properties/property.md#property-setpropertyparameters)

---

## [After Effects 16.1]()

- Scripting access to [ViewOptions object](../other/viewoptions.md#viewoptions) guide and ruler booleans:
  : - Added: [ViewOptions.guidesLocked](../other/viewoptions.md#viewoptions-guideslocked)
    - Added: [ViewOptions.guidesSnap](../other/viewoptions.md#viewoptions-guidessnap)
    - Added: [ViewOptions.guidesVisibility](../other/viewoptions.md#viewoptions-guidesvisibility)
    - Added: [ViewOptions.rulers](../other/viewoptions.md#viewoptions-rulers)
- Scripting access to add, remove, and set existing guides:
  : - Added: [Item.addGuide()](../items/item.md#item-addguide)
    - Added: [Item.removeGuide()](../items/item.md#item-removeguide)
    - Added: [Item.setGuide()](../items/item.md#item-setguide)
- Scripting access to additional EGP property attributes:
  : - Added: [CompItem.motionGraphicsTemplateControllerCount](../items/compitem.md#compitem-motiongraphicstemplatecontrollercount)
    - Added: [CompItem.getMotionGraphicsTemplateControllerName()](../items/compitem.md#compitem-getmotiongraphicstemplatecontrollername)
    - Added: [CompItem.setMotionGraphicsControllerName()](../items/compitem.md#compitem-setmotiongraphicscontrollername)
    - Added: [Property.addToMotionGraphicsTemplateAs()](../properties/property.md#property-addtomotiongraphicstemplateas)

---

## [After Effects 16.0](https://helpx.adobe.com/after-effects/using/whats-new/2019.html) (October 2018)

- Scripting access to marker label and protectedRegion attributes:
  : - Added: [MarkerValue.label](../other/markervalue.md#markervalue-label)
    - Added: [MarkerValue.protectedRegion](../other/markervalue.md#markervalue-protectedregion)
- Scripting access to additional project color management settings:
  : - Added: [Project.workingSpace](../general/project.md#project-workingspace)
    - Added: [Project.workingGamma](../general/project.md#project-workinggamma)
    - Added: [Project.listColorProfiles()](../general/project.md#project-listcolorprofiles)
    - Added: [Project.linearizeWorkingSpace](../general/project.md#project-linearizeworkingspace)
    - Added: [Project.compensateForSceneReferredProfiles](../general/project.md#project-compensateforscenereferredprofiles)
- Scripting access to the expression engine attribute:
  : - Added: [Project.expressionEngine](../general/project.md#project-expressionengine)
- Added project method [Project.setDefaultImportFolder()](../general/project.md#project-setdefaultimportfolder), which sets the folder that will be shown in the file import dialog.
- Added app property [app.disableRendering](../general/application.md#app-disablerendering), which disables rendering via the same mechanism as the Caps Lock key.

---

## [After Effects 15.1](https://helpx.adobe.com/after-effects/using/whats-new/2018.html) (April 2018)

- [Project.autoFixExpressions()](../general/project.md#project-autofixexpressions) will now fix expression name references in single quotes (ex., (‘Effect Name’)), as well as double quotes.
- Fixes [CompItem.exportAsMotionGraphicsTemplate()](../items/compitem.md#compitem-exportasmotiongraphicstemplate) not returning a boolean as expected

---

## [After Effects 15.0](https://forums.adobe.com/docs/DOC-8872) (October 2017)

- Scripting Access to motion graphics templates
  : - Added: [CompItem.motionGraphicsTemplateName](../items/compitem.md#compitem-motiongraphicstemplatename)
    - Added: [CompItem.exportAsMotionGraphicsTemplate()](../items/compitem.md#compitem-exportasmotiongraphicstemplate)
    - Added: [CompItem.openInEssentialGraphics()](../items/compitem.md#compitem-openinessentialgraphics)
    - Added: [Property.addToMotionGraphicsTemplate()](../properties/property.md#property-addtomotiongraphicstemplate)
    - Added: [Property.canAddToMotionGraphicsTemplate()](../properties/property.md#property-canaddtomotiongraphicstemplate)

---

## [After Effects 14.2.1 (CC 2017.2)](https://blogs.adobe.com/creativecloud/a-june-2017-update-to-after-effects-cc-is-now-available/) (June 2017)

- Buttons in ScriptUI panels have been reverted to the rectangular appearance seen in After Effects 14.1 and previous releases.
- The [AVItem.setProxyToNone()](../items/avitem.md#avitem-setproxytonone) scripting method no longer fails with an error message, “After Effects error: AEGP trying to add invalid footage”.
- The [System.callSystem()](../general/system.md#system-callsystem) scripting method now waits for all tasks called by the command to complete, instead of failing when the command takes a long time to complete.

---

## [After Effects 14.2 (CC 2017.1)](https://blogs.adobe.com/creativecloud/after-effects-cc-april-2017-in-depth-scripting-improvements/) (April 2017)

- Scripting Access to text leading
  : - Added: [TextDocument.leading](../text/textdocument.md#textdocument-leading)
- Scripting Access to Team Projects (Beta)
  : - Added: [Project.newTeamProject()](../general/project.md#project-newteamproject)
    - Added: [Project.openTeamProject()](../general/project.md#project-openteamproject)
    - Added: [Project.shareTeamProject()](../general/project.md#project-shareteamproject)
    - Added: [Project.syncTeamProject()](../general/project.md#project-syncteamproject)
    - Added: [Project.closeTeamProject()](../general/project.md#project-closeteamproject)
    - Added: [Project.convertTeamProjectToProject()](../general/project.md#project-convertteamprojecttoproject)
    - Added: [Project.listTeamProjects()](../general/project.md#project-listteamprojects)
    - Added: [Project.isTeamProjectOpen()](../general/project.md#project-isteamprojectopen)
    - Added: [Project.isAnyTeamProjectOpen()](../general/project.md#project-isanyteamprojectopen)
    - Added: [Project.isTeamProjectEnabled()](../general/project.md#project-isteamprojectenabled)
    - Added: [Project.isLoggedInToTeamProject()](../general/project.md#project-isloggedintoteamproject)
    - Added: [Project.isSyncCommandEnabled()](../general/project.md#project-issynccommandenabled)
    - Added: [Project.isShareCommandEnabled()](../general/project.md#project-issharecommandenabled)
    - Added: [Project.isResolveCommandEnabled()](../general/project.md#project-isresolvecommandenabled)
    - Added: [Project.resolveConflict()](../general/project.md#project-resolveconflict)
- Drop-down menus in ScriptUI panels are no longer clipped on HiDPI displays on Windows.
- The appearance of buttons, sliders, disclosure triangles (“twirly arrow”), scroll bar, progress bar, radio buttons, and checkboxes in ScriptUI embedded panels have been updated to match the appearance of After Effects native controls.
- After Effects no longer crashes when the [AVLayer.compPointToSource()](../layers/avlayer.md#avlayer-comppointtosource) scripting method is used with a 3D text layer.
- The match name of the Fast Box Blur effect is “ADBE Box Blur2”. The older match name “ADBE Box Blur” will continue to work: when used to add the effect, “ADBE Box Blur” will apply the Fast Box Blur effect, but with the older name “Box Blur”; the Iterations parameter will be set to the new default of 3.

---

## [After Effects 14.0 (CC 2017)](https://forums.adobe.com/message/9108589) (November 2016)

- Scripting Access to Tools
  : - Added: [Project.toolType](../general/project.md#project-tooltype)
- Scripting Access to Composition Markers
  : - Added: [CompItem.markerProperty](../items/compitem.md#compitem-markerproperty)
- Scripting Access to Queue in AME
  : - Added: [RenderQueue.queueInAME()](../renderqueue/renderqueue.md#renderqueue-queueiname)
- Scripting Access to Available GPU Acceleration Options
  : - Added: [app.availableGPUAccelTypes](../general/application.md#app-availablegpuacceltypes)

---

## [After Effects 13.8 (CC 2015.3)](https://blogs.adobe.com/creativecloud/after-effects-cc-2015-3-in-depth-gpu-accelerated-effects/) (June 2016)

- Enable GPU effect rendering via scripting
  : - Added: [Project.gpuAccelType](../general/project.md#project-gpuacceltype)
- New Gaussian Blur effect added w/ matchname `ADBE Gaussian Blur 2`

---

## [After Effects 13.6 (CC 2015)](https://blogs.adobe.com/creativecloud/whats-new-and-changed-in-the-upcoming-update-to-after-effects-cc-2015/) (November 2015)

- Scripting access to text baselines
  : - Added: [baselineLocs](../text/textdocument.md#textdocument-baselinelocs)
- New scripting method to generate random numbers
  : - Added: [generateRandomNumber()](../general/globals.md#generaterandomnumber)
- Using the [copyToComp()](../layers/layer.md#layer-copytocomp) scripting method no longer causes After Effects to crash when the layer has a parent.
- The [valueAtTime()](../properties/property.md#property-valueattime) scripting method now waits for time-intensive expressions, like `sampleImage`, to finish evaluating before it returns the result.
- ScriptUI panels now display and resize correctly on high-DPI displays on Windows.
- After Effects no longer crashes when you click OK or Cancel buttons in a scriptUI dialog with tabbed panels.

---

## [After Effects 13.2 (CC 2014.2)](https://blogs.adobe.com/creativecloud/after-effects-cc-2014-2-13-2/) (December 2014)

- Scripting improvements for text layers (read-only)
  : - Returns boolean value:
      : - Added: [fauxBold](../text/textdocument.md#textdocument-fauxbold)
        - Added: [fauxItalic](../text/textdocument.md#textdocument-fauxitalic)
        - Added: [allCaps](../text/textdocument.md#textdocument-allcaps)
        - Added: [smallCaps](../text/textdocument.md#textdocument-smallcaps)
        - Added: [superscript](../text/textdocument.md#textdocument-superscript)
        - Added: [subscript](../text/textdocument.md#textdocument-subscript)
    - Returns float:
      : - Added: [verticalScale](../text/textdocument.md#textdocument-verticalscale)
        - Added: [horizontalScale](../text/textdocument.md#textdocument-horizontalscale)
        - Added: [baselineShift](../text/textdocument.md#textdocument-baselineshift)
        - Added: [tsume](../text/textdocument.md#textdocument-tsume)
    - Returns array of ([X,Y]) position coordinates (paragraph text layers only):
      : - Added: [boxTextPos](../text/textdocument.md#textdocument-boxtextpos)
- Layer space / comp space conversion:
  : - Added: [sourcePointToComp()](../layers/avlayer.md#avlayer-sourcepointtocomp)
    - Added: [compPointToSource()](../layers/avlayer.md#avlayer-comppointtosource)

---

## [After Effects 13.1 (CC 2014.1)](https://blogs.adobe.com/creativecloud/after-effects-cc-2014-1-13-1/) (September 2014)

- Scripting improvements for text layers (read-only)
  : - returns string:
      : - Added: [fontLocation](../text/textdocument.md#textdocument-fontlocation)
        - Added: [fontStyle](../text/textdocument.md#textdocument-fontstyle)
        - Added: [fontFamily](../text/textdocument.md#textdocument-fontfamily)
- “Use Legacy UI” toggle implemented

---

## [After Effects 13.0 (CC 2014)](https://blogs.adobe.com/creativecloud/new-changed-after-effects-cc-2014/) (June 2014)

- Scripting access to render settings and output module settings
  : - Added: RenderQueueItem object [getSetting](../renderqueue/renderqueueitem.md#renderqueueitem-getsetting), [setSetting](../renderqueue/renderqueueitem.md#renderqueueitem-setsetting) methods
    - Added: RenderQueueItem object [getSettings](../renderqueue/renderqueueitem.md#renderqueueitem-getsettings), [setSettings](../renderqueue/renderqueueitem.md#renderqueueitem-setsettings) methods
    - Added: OutputModule object [getSetting](../renderqueue/outputmodule.md#outputmodule-getsetting), [setSetting](../renderqueue/outputmodule.md#outputmodule-setsetting) methods
    - Added: OutputModule object [getSettings](../renderqueue/outputmodule.md#outputmodule-getsettings), [setSettings](../renderqueue/outputmodule.md#outputmodule-setsettings) methods
- Fetch project item by id: [Project.itemByID()](../general/project.md#project-itembyid)
- CEP panels implemented

---

## [After Effects 12.0 (CC)](https://blogs.adobe.com/creativecloud/scripting-changes-in-after-effects-cc-12-0-12-2/) (June 2013)

- Access to effect’s internal version string
  : - Added: Application effects object’s version attribute, see [app.effects](../general/application.md#app-effects)
- Ability to get and set preview mode
  : - Added: [ViewOptions.fastPreview](../other/viewoptions.md#viewoptions-fastpreview)
- Access to layer sampling method (see [samplingQuality](../layers/avlayer.md#avlayer-samplingquality))
- Changed preference and settings methods (see [Settings object](../other/settings.md#settings))
- ScriptUI is now based on the same controls as the main application.

---

## [After Effects 11.0 (CS6)](https://web.archive.org/web/20120623073355/https://blogs.adobe.com/toddkopriva/2012/06/scripting-changes-in-after-effects-cs6-plus-new-scripting-guide.html/) (April 2012)

- Added: Access to [Viewer object](../other/viewer.md#viewer) object and controls
  : - Added: [app.activeViewer](../general/application.md#app-activeviewer)
    - Added: [AVLayer.openInViewer()](../layers/avlayer.md#avlayer-openinviewer) to open a layer in the layer viewer
    - Added: [CompItem.openInViewer()](../items/compitem.md#compitem-openinviewer) to open a composition in the composition viewer
    - Added: [FootageItem.openInViewer()](../items/footageitem.md#footageitem-openinviewer) to open a footage item in the footage viewer
- Added: [Property.canSetExpression](../properties/property.md#property-cansetexpression)
- Added: [AVLayer.environmentLayer](../layers/avlayer.md#avlayer-environmentlayer)
- Added: [MaskPropertyGroup.maskFeatherFalloff](../properties/maskpropertygroup.md#maskpropertygroup-maskfeatherfalloff)
- Access to Shape Feather properties via scripting
  : - Added: [Shape.featherSegLocs](../other/shape.md#shape-featherseglocs)
    - Added: [Shape.featherRelSegLocs](../other/shape.md#shape-featherrelseglocs)
    - Added: [Shape.featherRadii](../other/shape.md#shape-featherradii)
    - Added: [Shape.featherInterps](../other/shape.md#shape-featherinterps)
    - Added: [Shape.featherTensions](../other/shape.md#shape-feathertensions)
    - Added: [Shape.featherTypes](../other/shape.md#shape-feathertypes)
    - Added: [Shape.featherRelCornerAngles](../other/shape.md#shape-featherrelcornerangles)

---

## [After Effects 10.5 (CS5.5)](https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/) (April 2011)

- Added to the [Project object](../general/project.md#project) object:
  : - [Project.framesCountType](../general/project.md#project-framescounttype)
    - [Project.feetFramesFilmType](../general/project.md#project-feetframesfilmtype)
    - [Project.framesUseFeetFrames](../general/project.md#project-framesusefeetframes)
    - [Project.footageTimecodeDisplayStartType](../general/project.md#project-footagetimecodedisplaystarttype)
    - [Project.timeDisplayType](../general/project.md#project-timedisplaytype)
- Removed from the [Project object](../general/project.md#project) object:
  : - `timecodeDisplayType` attribute
    - `timecodeBaseType` attribute
    - `timecodeNTSCDropFrame` attribute
    - `timecodeFilmType` attribute
    - `TimecodeDisplayType` enum
    - `TimecodeFilmType` enum
    - `TimecodeBaseType` enum
- Added: [CompItem.dropFrame](../items/compitem.md#compitem-dropframe)
- Added support for Paragraph Box Text:
  : - Added [LayerCollection.addBoxText()](../layers/layercollection.md#layercollection-addboxtext)
    - Added [TextDocument.boxText](../text/textdocument.md#textdocument-boxtext)
    - Added [TextDocument.pointText](../text/textdocument.md#textdocument-pointtext)
    - Added [TextDocument.boxTextSize](../text/textdocument.md#textdocument-boxtextsize)
- Added [LightLayer.lightType](../layers/lightlayer.md#lightlayer-lighttype)

---

## [After Effects 9.0 (CS4)](https://web.archive.org/web/20121022055915/http://blogs.adobe.com/toddkopriva/2008/12/after-effects-cs4-scripting-ch.html/) (September 2008)

- Added: [app.isoLanguage](../general/application.md#app-isolanguage)
- Added: [MarkerValue.duration](../other/markervalue.md#markervalue-duration)
- Added: [OutputModule.includeSourceXMP](../renderqueue/outputmodule.md#outputmodule-includesourcexmp)
- Added: [Project.xmpPacket](../general/project.md#project-xmppacket)
- Added the following Property methods and attributes related to the Separate Dimensions feature:
  : - [Property.dimensionsSeparated](../properties/property.md#property-dimensionsseparated)
    - [Property.getSeparationFollower()](../properties/property.md#property-getseparationfollower)
    - [Property.isSeparationFollower](../properties/property.md#property-isseparationfollower)
    - [Property.isSeparationLeader](../properties/property.md#property-isseparationleader)
    - [Property.separationDimension](../properties/property.md#property-separationdimension)
    - [Property.separationLeader](../properties/property.md#property-separationleader)
- Added [TextDocument object](../text/textdocument.md#textdocument) access, including:
  : - Added: [TextDocument.applyFill](../text/textdocument.md#textdocument-applyfill)
    - Added: [TextDocument.applyStroke](../text/textdocument.md#textdocument-applystroke)
    - Added: [TextDocument.fillColor](../text/textdocument.md#textdocument-fillcolor)
    - Added: [TextDocument.font](../text/textdocument.md#textdocument-font)
    - Added: [TextDocument.fontSize](../text/textdocument.md#textdocument-fontsize)
    - Added: [TextDocument.justification](../text/textdocument.md#textdocument-justification)
    - Added: [TextDocument.resetCharStyle()](../text/textdocument.md#textdocument-resetcharstyle)
    - Added: [TextDocument.resetParagraphStyle()](../text/textdocument.md#textdocument-resetparagraphstyle)
    - Added: [TextDocument.strokeColor](../text/textdocument.md#textdocument-strokecolor)
    - Added: [TextDocument.strokeOverFill](../text/textdocument.md#textdocument-strokeoverfill)
    - Added: [TextDocument.strokeWidth](../text/textdocument.md#textdocument-strokewidth)
