# FileSource object

`app.project.item(index).mainSource`

`app.project.item(index).proxySource`


#### Description

The FileSource object describes footage that comes from a file.

!!! info
    FileSource is a subclass of [FootageSource object](footagesource.md). All methods and attributes of FootageSource, in addition to those listed below, are available when working with FileSource.

---

## Attributes

### FileSource.file

`app.project.item(index).mainSource.file`

`app.project.item(index).proxySource.file`


#### Description

The [Extendscript File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object for the file that defines this asset. To change the value:

- If this FileSource is a [proxySource](../item/avitem.md#avitemproxysource) of an [AVItem](../item/avitem.md), call [setProxy()](../item/avitem.md#avitemsetproxy) or [setProxyWithSequence()](../item/avitem.md#avitemsetproxywithsequence).
- If this FileSource is a [mainSource](../item/footageitem.md#footageitemmainsource) of a [FootageItem](../item/footageitem.md), call [replace()](../item/footageitem.md#footageitemreplace) or [replaceWithSequence()](../item/footageitem.md#footageitemreplacewithsequence).

#### Type

[File](https://extendscript.docsforadobe.dev/file-system-access/file-object.html) object; read-only.

---

### FileSource.missingFootagePath

`app.project.item(index).mainSource.missingFootagePath`

`app.project.item(index).proxySource.missingFootagePath`


#### Description

The path and filename of footage that is missing from this asset. See also [AVItem.footageMissing](../item/avitem.md#avitemfootagemissing).

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
