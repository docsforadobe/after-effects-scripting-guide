<a id="filesource"></a>

# FileSource object

`app.project.item(index).mainSource`
<br/>
`app.project.item(index).proxySource`
<br/>

**Description**

The FileSource object describes footage that comes from a file.

> FileSource is a subclass of [FootageSource object](footagesource.md#footagesource). All methods and attributes of FootageSource, in addition to those listed below, are available when working with FileSource.

---

## Attributes

<a id="filesource-file"></a>

### FileSource.file

`app.project.item(index).mainSource.file`
<br/>
`app.project.item(index).proxySource.file`
<br/>

**Description**

The [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the file that defines this asset. To change the value:

- If this FileSource is a [proxySource](../items/avitem.md#avitem-proxysource) of an [AVItem](../items/avitem.md#avitem), call [setProxy()](../items/avitem.md#avitem-setproxy) or [setProxyWithSequence()](../items/avitem.md#avitem-setproxywithsequence).
- If this FileSource is a [mainSource](../items/footageitem.md#footageitem-mainsource) of a [FootageItem](../items/footageitem.md#footageitem), call [replace()](../items/footageitem.md#footageitem-replace) or [replaceWithSequence()](../items/footageitem.md#footageitem-replacewithsequence).

**Type**

[File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object; read-only.

---

<a id="filesource-missingfootagepath"></a>

### FileSource.missingFootagePath

`app.project.item(index).mainSource.missingFootagePath`
<br/>
`app.project.item(index).proxySource.missingFootagePath`
<br/>

**Description**

The path and filename of footage that is missing from this asset. See also [AVItem.footageMissing](../items/avitem.md#avitem-footagemissing).

**Type**

String; read-only.

---

## Methods

<a id="filesource-reload"></a>

### FileSource.reload()

`app.project.item(index).mainSource.reload()`

**Description**

Reloads the asset from the file. This method can be called only on a `mainSource`, not a `proxySource`.

**Parameters**

None.

**Returns**

Nothing.
