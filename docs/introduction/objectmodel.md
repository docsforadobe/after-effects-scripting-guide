# The After Effects Object Model

As you look through this reference section, which is organized alphabetically by object, you can refer to the following diagrams for an overview of where the various objects fall within the hierarchy, and their correspondence to the user interface.

![After Effects Object Model](introduction/_static/objectmodel.png)

Hierarchy diagram of the main After Effects scripting objects

Note that the [File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html), Folder, and Socket objects are defined by ExtendScript, and are documented in the [JavaScript Tools Guide](https://extendscript.docsforadobe.dev/). ExtendScript also defines the ScriptUI module, a set of window and user-interface control objects, which are available to After Effects scripts. These are also documented in the [JavaScript Tools Guide](https://extendscript.docsforadobe.dev/). The hierarchy of objects in scripting corresponds to the hierarchy in the user interface.

![After Effects User Interface](introduction/_static/application.png)

The application contains a Project panel, which displays a project. The project contains compositions, which contain layers. The source for a layer can be a footage file, placeholder, or solid, also listed in the Project panel. Each layer contains settings known as properties, and these can contain markers and keyframes. The renderqueue contains render-queue items as well as render settings and output modules. All of these entities are represented by objects in scripting.

#### NOTE
To avoid ambiguity, this manual uses the term “attribute” to refer to JavaScript object properties, and the term “property” or “AE property” to refer to After Effects layer properties.

**Object summary**

The following table lists all objects alphabetically, with links to the documentation page for each.

| Object                                                                           | Description                                                                                                                                                 |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Global functions](../general/globals.md#globals)                                | Globally available functions that allow you to<br/>display text for script debugging purposes, and help<br/>convert time values between seconds and frames. |
| [Application object](../general/application.md#application)                      | A single global object, available by its name (app),<br/>that provides access to objects and application<br/>settings within the After Effects application. |
| [AVItem object](../items/avitem.md#avitem)                                       | Represents audio/visual files imported into After<br/>Effects.                                                                                              |
| [AVLayer object](../layers/avlayer.md#avlayer)                                   | Represents those layers that contain AVItem objects<br/>(composition layers, footage layers, solid layers,<br/>text layers, and sound layers).              |
| [CameraLayer object](../layers/cameralayer.md#cameralayer)                       | Represents a camera layer within a composition.                                                                                                             |
| [Collection object](../other/collection.md#collection)                           | Associates a set of objects or values as a logical<br/>group and provides access to them by index.                                                          |
| [CompItem object](../items/compitem.md#compitem)                                 | Represents a composition, and allows you to<br/>manipulate it and get information about it.                                                                 |
| [FileSource object](../sources/filesource.md#filesource)                         | Describes footage that comes from a file.                                                                                                                   |
| [FolderItem object](../items/folderitem.md#folderitem)                           | Represents a folder in the Project panel.                                                                                                                   |
| [FootageItem object](../items/footageitem.md#footageitem)                        | Represents a footage item imported into a project,<br/>which appears in the Project panel.                                                                  |
| [FootageSource object](../sources/footagesource.md#footagesource)                | Describes the file source of some footage.                                                                                                                  |
| [ImportOptions object](../other/importoptions.md#importoptions)                  | Encapsulates options for importing files into After<br/>Effects.                                                                                            |
| [Item object](../items/item.md#item)                                             | Represents an item in a project that appears in the<br/>Project panel.                                                                                      |
| [ItemCollection object](../items/itemcollection.md#itemcollection)               | Collects items in a project.                                                                                                                                |
| [KeyframeEase object](../other/keyframeease.md#keyframeease)                     | Encapsulates keyframe ease values in an After Effects<br/>property.                                                                                         |
| [Layer object](../layers/layer.md#layer)                                         | A base class for layer classes.                                                                                                                             |
| [LayerCollection object](../layers/layercollection.md#layercollection)           | Collects layers in a project.                                                                                                                               |
| [LightLayer object](../layers/lightlayer.md#lightlayer)                          | Represents a light layer within a composition.                                                                                                              |
| [MarkerValue object](../other/markervalue.md#markervalue)                        | Encapsulates marker values in an After Effects<br/>property.                                                                                                |
| [MaskPropertyGroup object](../properties/maskpropertygroup.md#maskpropertygroup) | Encapsulates mask attributes in a layer.                                                                                                                    |
| [OMCollection object](../renderqueue/omcollection.md#omcollection)               | Collects output modules in a render queue.                                                                                                                  |
| [OutputModule object](../renderqueue/outputmodule.md#outputmodule)               | Represents an output module for a render queue.                                                                                                             |
| [PlaceholderSource object](../sources/placeholdersource.md#placeholdersource)    | Describes a placeholder for footage.                                                                                                                        |
| [Project object](../general/project.md#project)                                  | Represents an After Effects project.                                                                                                                        |
| [Property object](../properties/property.md#property)                            | Represents an After Effects property.                                                                                                                       |
| [PropertyBase object](../properties/propertybase.md#propertybase)                | A base class for After Effects property and property<br/>group classes.                                                                                     |
| [PropertyGroup object](../properties/propertygroup.md#propertygroup)             | Represents an After Effects property group.                                                                                                                 |
| [RenderQueue object](../renderqueue/renderqueue.md#renderqueue)                  | Represents the After Effects render queue.                                                                                                                  |
| [RenderQueueItem object](../renderqueue/renderqueueitem.md#renderqueueitem)      | Represents a renderable item in a render queue.                                                                                                             |
| [RenderQueueItem object](../renderqueue/renderqueueitem.md#renderqueueitem)      | Collects render-queue items in a render queue.                                                                                                              |
| [RQItemCollection object](../renderqueue/rqitemcollection.md#rqitemcollection)   | Provides access to application settings and<br/>preferences.                                                                                                |
| [Shape object](../other/shape.md#shape)                                          | Encapsulates the outline shape information for a<br/>mask.                                                                                                  |
| [ShapeLayer object](../layers/shapelayer.md#shapelayer)                          | Represents a shape layer within a composition.                                                                                                              |
| [SolidSource object](../sources/solidsource.md#solidsource)                      | Describes a solid color that is the source of some<br/>footage.                                                                                             |
| [System object](../general/system.md#system)                                     | Provides access to the operating system from the<br/>application.                                                                                           |
| [TextDocument object](../text/textdocument.md#textdocument)                      | Encapsulates the text in a text layer.                                                                                                                      |
| [TextLayer object](../layers/textlayer.md#textlayer)                             | Represents a text layer within a composition.                                                                                                               |
| [Viewer object](../other/viewer.md#viewer)                                       | Represents a Composition, Layer, or Footage panel.                                                                                                          |
