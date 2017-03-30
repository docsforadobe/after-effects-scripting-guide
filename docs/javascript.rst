.. _javascript:

Elements of basic JavaScript relevant to After Effects scripting
################################################################

**JavaScript variables**

Scripting shares a global environment, so any script executed at startup can define variables and functions that are available to all scripts. In all cases, variables and functions, once defined by running a script that contains them, persist in subsequent scripts during a given After Effects session. Once the application is quit, all such globally defined variables and functions are cleared. Scripters should be careful about giving variables in scripts unique names, so that a script does not inadvertently reassign global variables intended to persist throughout a session.

Keywords and Statement Syntax
=============================

=================  ============================================================
Keyword/Statement                    Description
=================  ============================================================
``break``          Standard JavaScript; exit the currently executing loop.
``continue``       JavaScript; cease execution of the current loop iteration.
``case``           Label used in a ``switch`` statement.
``default``        Label used in a ``switch`` statement when a ``case`` label
                   is not found.
``do...while``     Standard JavaScript construct. Similar to the while loop,
                   except loop condition evaluation occurs at the end of the
                   loop.
``false``          Literal representing the Boolean false value.
``for``            Standard JavaScript loop construct.
``for...in``       Standard JavaScript construct. Provides a way to easily
                   loop through the properties of an object.
``function``       Used to define a function.
``if/if...else``   Standard JavaScript conditional constructs.
``new``            Standard JavaScript constructor statement.
``null``           Assigned to a variable, array element, or object property
                   to indicate that it does not contain a legalvalue.
``return``         Standard JavaScript way of returning a value from a
                   function or exiting a function.
``switch``         Standard JavaScript way of evaluating a JavaScript
                   expression and attempting to match the expression's value
                   to a ``case`` label.
``this``           Standard JavaScript method of indicating the current object.
``true``           Literal representing the Boolean true value.
``undefined``      Indicates that the variable, array element, or object
                   property has not yet been assigned a value.
``var``            Standard JavaScript syntax used to declare a local variable.
``while``          Standard JavaScript construct. Similar to the
                   do...whileloop, except loop condition evaluation occurs at
                   the beginning of the loop.
``with``           Standard JavaScript construct used to specify an object to
                   use in subsequent statements.
=================  ============================================================

**JavaScript operators**

The following tables list and describe all operators recognized by the After Effects scripting engine and show the precedence and associativity for all operators.

Description of Operators
========================

==========  ==============================================================
Operators   Description
==========  ==============================================================
``new``     Allocate object.
``delete``  Deallocate object.
``type``    of Returns data type.
``void``    Returns undefined value.
``.``       Structure member.
``[]``      Array element.
``()``      Function call.
``++``      Pre- or post-increment.
``--``      Pre- or post-decrement.
``-``       Unary negation or subtraction.
``~``       Bitwise NOT.
``!``       Logical NOT.
``*``       Multiply.
``/``       Divide.
``%``       Modulo division.
``+``       Add.
``<<``      Bitwise left shift.
``>>``      Bitwise right shift.
``>>>``     Unsigned bitwise right shift.
``<``       Less than.
``<=``      Less than or equal.
``>``       Greater than.
``>=``      Greater than or equal.
``==``      Equal.
``!=``      Not equal.
``&``       Bitwise AND.
``^``       Bitwise XOR.
``|``       Bitwise OR.
``&&``      Logical AND.
``||``      Logical OR.
``?:``      Conditional (ternary).
``=``       Assignment.
``+=``      Assignment with add operation.
``-=``      Assignment with subtract operation.
``*=``      Assignment with multiply operation.
``/=``      Assignment with divide operation.
``%=``      Assignment with modulo division operation.
``<<=``     Assignment with bitwise left shift operation.
``>>=``     Assignment with bitwise right shift operation.
``>>>=``    Assignment with unsigned bitwise right shift operation.
``&=``      Assignment with bitwise AND operation.
``^=``      Assignment with bitwise XOR operation.
``|=``      Assignment with bitwise OR operation.
``,``       Multiple evaluation.
==========  ==============================================================

Operator Precedence
===================

===========================================================  =============
Operators (highest precedence to lowest)                     Associativity
===========================================================  =============
[], (), .                                                    left to right
new, delete, - (unary negation), !, type of, void , ++, --   right to left
\*, /, %                                                     left to right
+, - (subtraction)                                           left to right
<<, >>, >>>                                                  left to right
<, <=, >, >=                                                 left to right
= =, ! =                                                     left to right
&                                                            left to right
^                                                            left to right
\|                                                           left to right
&&                                                           left to right
\|\|                                                         left to right
?:                                                           right to left
==, /=, %=, <<=, >>=, >>>=, &=, ^=, \|=, +=, -=, \*=         right to left
,                                                            left to right
===========================================================  =============
