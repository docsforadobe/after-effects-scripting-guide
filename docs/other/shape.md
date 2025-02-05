# Shape object

`app.project.item(index).layer(index).property(index).property("maskShape").value`

#### Description

The Shape object encapsulates information describing a shape in a shape layer, or the outline shape of a Mask. It is the value of the "Mask Path" AE properties, and of the "Path" AE property of a shape layer. Use the constructor, `new Shape()`, to create a new, empty Shape object, then set the attributes individually to define the shape.

A shape has a set of anchor points, or vertices, and a pair of direction handles, or tangent vectors, for each anchor point. A tangent vector (in a non-RotoBezier mask) determines the direction of the line that is drawn to or from an anchor point. There is one incoming tangent vector and one outgoing tangent vector associated with each vertex in the shape.

A tangent value is a pair of x,y coordinates specified relative to the associated vertex. For example, a tangent of [-1,-1] is located above and to the left of the vertex and has a 45 degree slope, regardless of the actual location of the vertex. The longer a handle is, the greater its influence; for example, an incoming shape segment stays closer to the vector for an `inTangent` of [-2,-2] than it does for an `inTangent` of [-1,-1], even though both of these come toward the vertex from the same direction.

If a shape is not closed, the `inTangent` for the first vertex and the `outTangent` for the final vertex are ignored. If the shape is closed, these two vectors specify the direction handles of the final connecting segment out of the final vertex and back into the first vertex.

RotoBezier masks calculate their tangents automatically. (See [MaskPropertyGroup.rotoBezier](../property/maskpropertygroup.md#maskpropertygrouprotobezier)) If a shape is used in a RotoBezier mask, the tangent values are ignored. This means that, for RotoBezier masks, you can construct a shape by setting only the `vertices` attribute and setting both `inTangents` and `outTangents` to `null`. When you access the new shape, its tangent values are filled with the automatically calculated tangent values.

For closed mask shapes, variable-width mask feather points can exist anywhere along the mask path. Feather points are part of the Mask Path property. Reference a specific feather point by the number of the mask path segment (portion of the path between adjacent vertices) where it appears.

!!! tip
    The feather points on a mask are listed in an array in the order that they were created.

#### Examples

- Create a square mask. A square is a closed shape with 4 vertices. The `inTangents` and `outTangents` for connected straight-line segments are 0, the default, and do not need to be explicitly set.
    ```javascript
    var myShape = new Shape();
    myShape.vertices = [[0,0], [0,100], [100,100], [100,0]];
    myShape.closed = true;
    ```
- Create a "U" shaped mask. A "U" is an open shape with the same 4 vertices used in the square.
    ```javascript
    var myShape = new Shape();
    myShape.vertices = [[0,0], [0,100], [100,100], [100,0]];
    myShape.closed = false;
    ```
- Create an oval. An oval is a closed shape with 4 vertices and with inTangent and outTangent values.
    ```javascript
    var myShape = new Shape();
    myShape.vertices = [[300,50], [200,150],[300,250],[400,150]];
    myShape.inTangents = [[55.23,0],[0,-55.23],[-55.23,0],[0,55.23]];
    myShape.outTangents = [[-55.23,0],[0,55.23],[55.23,0],[0,-55.23]];
    myShape.closed = true;
    ```
- Create a square mask with two feather points. A large square mask with two feather points, one closer to the left end the second mask segment (off the bottom edge) with a radius of 30 pixels and the other one centered the third mask segment (off the right edge) with a larger radius of 100 pixels.
    ```javascript
    var myShape = new Shape();
    myShape.vertices = [[100,100], [100,400], [400,400], [400,100]]; // segments drawn counter clockwise
    myShape.closed = true;
    myShape.featherSegLocs = [1, 2]; // segments are numbered starting at 0, so second segment is 1
    myShape.featherRelSegLocs = [0.15, 0.5]; // 0.15 is closer to the lower-left corner of the square
    myShape.featherRadii = [30, 100]; // second feather point (onright-sidesegment) has a larger radius
    ```

---

## Attributes

### Shape.closed

`shapeObject.value.closed`

#### Description

When `true`, the first and last vertices are connected to form a closed curve. When `false`, the closing segment is not drawn.

#### Type

Boolean; read/write.

---

### Shape.featherInterps

`shapeObject.value.featherInterps`

#### Description

An array containing each feather point's radius interpolation type (0 for non-Hold feather points, 1 for Hold feather points).

!!! tip
    Values are stored in the array in the order that feather points are created.

#### Type

Array of integers (0 or 1); read/write.

---

### Shape.featherRadii

`shapeObject.value.featherRadii`

#### Description

An array containing each feather point's radius (feather amount); inner feather points have negative values.

!!! tip
    Values are stored in the array in the order that feather points are created.

#### Type

Array of floating-point values; read/write.

---

### Shape.featherRelCornerAngles

`shapeObject.value.featherRelCornerAngles`

#### Description

An array containing each feather point's relative angle percentage between the two normals on either side of a curved outer feather boundary at a corner on a mask path. The angle value is 0% for feather points not at corners.

!!! tip
    Values are stored in the array in the order that feather points are created.

#### Type

Array of floating-point percentage values (0 to 100); read/write.

---

### Shape.featherRelSegLocs

`shapeObject.value.featherRelSegLocs`

#### Description

An array containing each feather point's relative position, from 0 to 1, on its mask path segment (section of the mask path between vertices, numbered starting at 0).

!!! tip
    Values are stored in the array in the order that feather points are created. To move a feather point to a different mask path segment, first change the [featherSegLocs](#shapefeatherseglocs) attribute value, then this attribute.

#### Type

Array of floating-point values (0 to 1); read/write.

---

### Shape.featherSegLocs

`shapeObject.value.featherSegLocs`

#### Description

An array containing each feather point's mask path segment number (section of the mask path between vertices, numbered starting at 0).

!!! tip
    Values are stored in the array in the order that feather points are created. Move a feather point to a different segment by changing both its segment number (this attribute) and, optionally, its [featherRelSegLocs](#shapefeatherrelseglocs) attribute value.

#### Type

Array of integers; read/write.

#### Example

```javascript
// Assuming a rectangle closed mask (segments numbered 0-3) has 3 mask feather points,
// move all 3 feather points to the first mask segment.

// Get the Shape object for the mask, assumed here to be the first mask on the layer.
var my_maskShape = layer.mask(1).property("ADBE Mask Shape").value;

// Check where mask feather points are located.
// Note: They are stored in the order that they are added.
var where_are_myMaskFeatherPoints = my_maskShape.featherSegLocs;

// Move all 3 feather points to the first mask segment (numbered 0).
my_maskShape.featherSegLocs = [0, 0, 0];

// Update the mask path.
layer.mask(1).property("ADBE Mask Shape").setValue(my_maskShape);
```

---

### Shape.featherTensions

`shapeObject.value.featherTensions`

#### Description

An array containing each feather point's tension amount, from 0 (0% tension) to 1 (100% tension).

!!! tip
    Values are stored in the array in the order that feather points are created.

#### Type

Array of floating-point values (0 to 1); read/write.

---

### Shape.featherTypes

`shapeObject.value.featherTypes`

#### Description

An array containing each feather point's direction, either 0 (outer feather point) or 1 (inner feather point).

!!! tip
    You cannot change the direction of a feather point after it has been created.
    Values are stored in the array in the order that feather points are created.

#### Type

Array of integers (0 or 1); read/write.

---

### Shape.inTangents

`shapeObject.value.inTangents`

#### Description

The incoming tangent vectors, or direction handles, associated with the vertices of the shape. Specify each vector as an array of two floating-point values, and collect the vectors into an array the same length as the `vertices` array.

Each tangent value defaults to [0,0]. When the mask shape is not RotoBezier, this results in a straight line segment.

If the shape is in a RotoBezier mask, all tangent values are ignored and the tangents are automatically calculated.

#### Type

Array of floating-point pair arrays; read/write.

---

### Shape.outTangents

`shapeObject.value.outTangents`

#### Description

The outgoing tangent vectors, or direction handles, associated with the vertices of the shape. Specify each vector as an array of two floating-point values, and collect the vectors into an array the same length as the `vertices` array.

Each tangent value defaults to [0,0]. When the mask shape is not RotoBezier, this results in a straight line segment.

If the shape is in a RotoBezier mask, all tangent values are ignored and the tangents are automatically calculated.

#### Type

Array of floating-point pair arrays; read/write.

---

### Shape.vertices

`shapeObject.value.vertices`

#### Description

The anchor points of the shape. Specify each point as an array of two floating-point values, and collect the point pairs into an array for the complete set of points.

#### Example

```javascript
myShape.vertices = [[0,0], [0,1], [1,1], [1,0]];
```

#### Type

Array of floating-point pair arrays; read/write.
