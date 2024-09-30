# SolidSource object

`app.project.item(index).mainSource`
<br/>
`app.project.item(index).proxySource`
<br/>

#### Description

The SolidSource object represents a solid-color footage source.

> SolidSource is a subclass of [FootageSource](footagesource.md#footagesource). All methods and attributes of FootageSource, in addition to those listed below, are available when working with SolidSource.

---

## Attributes

### SolidSource.color

`solidSource.color`

#### Description

The color of the solid, expressed as red, green, and blue values.

#### Type

Array of three floating-point values, `[R, G, B]`, in the range `[0.0..1.0]`; read/write.
