# FileSource object

`app.project.item(index).mainSource`
<br/>
`app.project.item(index).proxySource`
<br/>

#### Description

The FileSource object describes footage that comes from a file.

> FileSource is a subclass of [FootageSource object](footagesource.md#footagesource). All methods and attributes of FootageSource, in addition to those listed below, are available when working with FileSource.

---

## Attributes

### FileSource.file

`app.project.item(index).mainSource.file`
<br/>
`app.project.item(index).proxySource.file`
<br/>

#### Description

The [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the file that defines this asset. To change the value:

- If this FileSource is a [proxySource](../items/avitem.md#avitemproxysource) of an [AVItem](../items/avitem.md#avitem), call [setProxy()](../items/avitem.md#avitemsetproxy) or [setProxyWithSequence()](../items/avitem.md#avitemsetproxywithsequence).
- If this FileSource is a [mainSource](../items/footageitem.md#footageitemmainsource) of a [FootageItem](../items/footageitem.md#footageitem), call [replace()](../items/footageitem.md#footageitemreplace) or [replaceWithSequence()](../items/footageitem.md#footageitemreplacewithsequence).

#### Type

[File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object; read-only.

---

### FileSource.missingFootagePath

`app.project.item(index).mainSource.missingFootagePath`
<br/>
`app.project.item(index).proxySource.missingFootagePath`
<br/>

#### Description

The path and filename of footage that is missing from this asset. See also [AVItem.footageMissing](../items/avitem.md#avitemfootagemissing).

#### Type

String; read-only.

---

## Methods

### FileSource.reload()

`app.project.item(index).mainSource.reload()`

#### Description

Reloads the asset from the file. This method can be called only on a `mainSource`, not a `proxySource`.

#### Parameters

None.

#### Returns

Nothing.