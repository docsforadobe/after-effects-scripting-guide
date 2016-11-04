Added: ViewOptions fastPreview property to access the state of the Fast Previews menu with the scripting interface. This is a read/write attribute using an enumerated value:

Value	Fast Previews menu option
- ``FastPreviewType.FP_OFF``: Off (Final Quality)
- ``FastPreviewType.FP_ADAPTIVE_RESOLUTION``: Adaptive Resolution
- ``FastPreviewType.FP_DRAFT``: Draft
- ``FastPreviewType.FP_FAST_DRAFT``: Fast Draft
- ``FastPreviewType.FP_WIREFRAME``: Wireframe
If you try to get or set the attribute’s value in the Layer or Footage panel, you’ll get an error message.

The Draft preview mode is only available in ray-traced 3D compositions. If you try to use it in a Classic 3D composition, you’ll get an error: “Cannot set Draft fast preview mode in a Classic 3D composition.”

app.activeViewer.views[0].options.fastPreview == FastPreviewType.FP_ADAPTIVE_RESOLUTION
app.activeViewer.views[0].options.fastPreview == FastPreviewType.FP_DRAFT
app.activeViewer.views[0].options.fastPreview == FastPreviewType.FP_FAST_DRAFT
app.activeViewer.views[0].options.fastPreview == FastPreviewType.FP_OFF
app.activeViewer.views[0].options.fastPreview == FastPreviewType.FP_WIREFRAME
app.language == Language.CHINESE
app.language == Language.KOREAN
app.project.activeItem.layer("Layer Name").samplingQuality == LayerSamplingQuality.BICUBIC
app.project.activeItem.layer("Layer Name").samplingQuality == LayerSamplingQuality.BILINEAR
app.project.activeItem.layer("Text 1").sourceText.value.justification == ParagraphJustification.MULTIPLE_JUSTIFICATIONS
