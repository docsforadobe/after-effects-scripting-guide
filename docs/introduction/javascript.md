# Elements of basic JavaScript relevant to After Effects scripting

## Javascript Variables

Scripting shares a global environment, so any script executed at startup can define variables and functions that are available to all scripts. In all cases, variables and functions, once defined by running a script that contains them, persist in subsequent scripts during a given After Effects session. Once the application is quit, all such globally defined variables and functions are cleared. Scripters should be careful about giving variables in scripts unique names, so that a script does not inadvertently reassign global variables intended to persist throughout a session.

### Keywords and Statement Syntax

| Keyword/Statement |                                                             Description                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `break`           | Standard JavaScript; exit the currently executing loop.                                                                              |
| `continue`        | JavaScript; cease execution of the current loop iteration.                                                                           |
| `case`            | Label used in a `switch` statement.                                                                                                  |
| `default`         | Label used in a `switch` statement when a `case` label is not found.                                                                 |
| `do...while`      | Standard JavaScript construct. Similar to the while loop, except loop condition evaluation occurs at the end of the loop.            |
| `false`           | Literal representing the Boolean false value.                                                                                        |
| `for`             | Standard JavaScript loop construct.                                                                                                  |
| `for...in`        | Standard JavaScript construct. Provides a way to easily loop through the properties of an object.                                    |
| `function`        | Used to define a function.                                                                                                           |
| `if/if...else`    | Standard JavaScript conditional constructs.                                                                                          |
| `new`             | Standard JavaScript constructor statement.                                                                                           |
| `null`            | Assigned to a variable, array element, or object property to indicate that it does not contain a legalvalue.                         |
| `return`          | Standard JavaScript way of returning a value from a function or exiting a function.                                                  |
| `switch`          | Standard JavaScript way of evaluating a JavaScript expression and attempting to match the expression's value to a `case` label.      |
| `this`            | Standard JavaScript method of indicating the current object.                                                                         |
| `true`            | Literal representing the Boolean true value.                                                                                         |
| `undefined`       | Indicates that the variable, array element, or object property has not yet been assigned a value.                                    |
| `var`             | Standard JavaScript syntax used to declare a local variable.                                                                         |
| `while`           | Standard JavaScript construct. Similar to the do...while loop, except loop condition evaluation occurs at the beginning of the loop. |
| `with`            | Standard JavaScript construct used to specify an object to use in subsequent statements.                                             |

---

## Javascript Operators

The following tables list and describe all operators recognized by the After Effects scripting engine and show the precedence and associativity for all operators.

### Description of Operators

|         Operators         |                       Description                       |
| ------------------------- | ------------------------------------------------------- |
| `new`                     | Create new object instance.                             |
| `delete`                  | Delete property from an object.                         |
| `typeof`                  | Returns data type.                                      |
| `void`                    | Returns undefined value.                                |
| `.`                       | Object member.                                          |
| `[]`                      | Array element.                                          |
| `()`                      | Function call.                                          |
| `++`                      | Pre- or post-increment.                                 |
| `--`                      | Pre- or post-decrement.                                 |
| `-`                       | Unary negation or subtraction.                          |
| `~`                       | Bitwise NOT.                                            |
| `!`                       | Logical NOT.                                            |
| `*`                       | Multiply.                                               |
| `/`                       | Divide.                                                 |
| `%`                       | Modulo division.                                        |
| `+`                       | Add.                                                    |
| `<<`                      | Bitwise left shift.                                     |
| `>>`                      | Bitwise right shift.                                    |
| `>>>`                     | Unsigned bitwise right shift.                           |
| `<`                       | Less than.                                              |
| `<=`                      | Less than or equal.                                     |
| `>`                       | Greater than.                                           |
| `>=`                      | Greater than or equal.                                  |
| `==`                      | Equal.                                                  |
| `!=`                      | Not equal.                                              |
| `&`                       | Bitwise AND.                                            |
| `^`                       | Bitwise XOR.                                            |
| <code>&#124;</code>       | Bitwise OR.                                             |
| `&&`                      | Logical AND.                                            |
| <code>&#124;&#124;</code> | Logical OR.                                             |
| `?:`                      | Conditional (ternary).                                  |
| `=`                       | Assignment.                                             |
| `+=`                      | Assignment with add operation.                          |
| `-=`                      | Assignment with subtract operation.                     |
| `*=`                      | Assignment with multiply operation.                     |
| `/=`                      | Assignment with divide operation.                       |
| `%=`                      | Assignment with modulo division operation.              |
| `<<=`                     | Assignment with bitwise left shift operation.           |
| `>>=`                     | Assignment with bitwise right shift operation.          |
| `>>>=`                    | Assignment with unsigned bitwise right shift operation. |
| `&=`                      | Assignment with bitwise AND operation.                  |
| `^=`                      | Assignment with bitwise XOR operation.                  |
| <code>&#124;=</code>      | Assignment with bitwise OR operation.                   |
| `,`                       | Multiple evaluation.                                    |

### Operator Precedence

|                  Operators (highest precedence to lowest)                  | Associativity |
| -------------------------------------------------------------------------- | ------------- |
| `[]`, `()`, `.`                                                            | left to right |
| `new`, `delete`, `-` (unary negation), `!`, `typeof`, `void`, `++`, `--`   | right to left |
| `*`, `/`, `%`                                                              | left to right |
| `+`, `-` (subtraction)                                                     | left to right |
| `<<`, `>>`, `>>>`                                                          | left to right |
| `<`, `<=`, `>`, `>=`                                                       | left to right |
| `==`, `!=`                                                                 | left to right |
| `&`                                                                        | left to right |
| `^`                                                                        | left to right |
| `\`                                                                        | left to right |
| `&&`                                                                       | left to right |
| <code>&#124;&#124;</code>                                                  | left to right |
| `?:`                                                                       | right to left |
| `==`, `/=`, `%=`, `<<=`, `>>=`, `>>>=`, `&=`, `^=`, `\=`, `+=`, `-=`, `*=` | right to left |
| `,`                                                                        | left to right |

---

## Javascript Classes

### Class Inheritance

This is section gives you a brief overview in oriented programming and inheritance. If you already know about this, you can skip this section.

In Javascript/Extendscript, Class Inheritance is the idea that you can define some properties or methods for a given object, and then create a *subclass* (or "child class") that inherits all of those properties & methods and adds more, further refining it.

For example, "automobile" could be one base class, with "cars" being a subclass of the "automobile" base class, with "sedan" and "convertible" being two subclasses of the "car" base class. Any properties or methods from "automobile" are also accessible by "convertible," because there's a direct inheritance from "automobile" -> "car" -> "convertible".

### Class Inheritance in After Effects

As a script developer, this is useful to know because many elements in the After Effects scripting environment follows this pattern.

As a user, you can see this in After Effects layers; every layer exists in the timeline, has a Name and Index and Label Color, but some types of layers have different properties than others - for example, Audio layers can't be enable/disabled, and Camera and Light layers can't have effects. They share the base "Layer" features, but are each **subclasses** with their own properties.

The same idea exists in After Effects scripting. Many API-accessible elements are part of class hierarchies that inherit and refine properties & methods. This lets the After Effects developers use existing structures to create new API-accessible components, and it allows script developers to use this same hierarchy to work with the After Effects DOM.

For the same example above, [Layer object](../layer/layer.md) (itself a subclass of [PropertyGroup object](../property/propertygroup.md)) is the *base class* for [AVLayer object](../layer/avlayer.md), [CameraLayer object](../layer/cameralayer.md), and [LightLayer object](../layer/lightlayer.md). This means that CameraLayer inherits everything from the Layer object, which inherits everything from the PropertyGroup object, which inherits everything from the PropertyBase object.

This is why you won't see the `name` property on the Layer page, but you can still use `layer.name` in your script; `name` is inherited from [PropertyBase.name](../property/propertybase.md#propertybasename).

!!! warning
    In a few specific cases, properties & methods are **removed** with inheritance, not just added. Those cases are noted on the relevant object page.

### Checking Classes

Typically in Javascript, you can use `instanceof` to check whether any given element matches an expected object type.

Keep in mind that you will need to check against the *most specific* class possible; an AE Text Layer will only return `true` for `layer instanceof TextLayer`, and `false` for all parent classes (`layer instanceof AVLayer`, `layer instanceof Layer`, etc.)

With that said, there exist some elements in the API that are *only* base classes for other classes; they exist to hold inherited properties & methods, but no DOM element is exactly of this type.

When checking `object instanceof {class}` with these classes, AE will either throw an error that `{class} is undefined` or return `false`, depending on how the class was implemented. The list below documents which base-only classes report which behaviours.
