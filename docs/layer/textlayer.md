# TextLayer object

`app.project.item(index).layer(index)`

#### Description

The TextLayer object represents a text layer within a composition. Create it using the [LayerCollection object's addText method](layercollection.md#layercollectionaddtext). It can be accessed in an item's layer collection either by index number or by a name string.

!!! info
    TextLayer is a subclass of [AVLayer](avlayer.md), which is a subclass of [Layer](layer.md). All methods and attributes of AVLayer and Layer are available when working with TextLayer.

#### AE Properties

TextLayer defines no additional attributes, but has the following AE properties and property groups, in addition to those inherited from AVLayer:

- `Text`
- `SourceText`
- `PathOptions`
- `Path`
- `ReversePath`
- `PerpendicularToPath`
- `ForceAlignment`
- `FirstMargin`
- `LastMargin`
- `MoreOptions`
- `AnchorPointGrouping`
- `GroupingAlignment`
- `Fill&Stroke`
- `InterCharacterBlending`
- `Animators`

#### Unused Properties and Attributes

The `TimeRemapandMotionTrackers` properties, inherited from AVLayer, are not applicable to text layers, and their related AVLayer attributes are not used:

- `canSetTimeRemapEnabled`
- `timeRemapEnabled`
- `trackMatteType`
- `isTrackMatte`
- `hasTrackMatte`
