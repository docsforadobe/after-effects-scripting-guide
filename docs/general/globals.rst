.. highlight:: javascript
.. _globals:

Global functions
################

These globally available functions that are specific to After Effects. Any JavaScript object or function can call these functions, which allow you to display text in a small (3-line) area of the Info panel, to convert numeric time values to and from string values, or to generate a random number.


==========================  ===================================================
Global function             Description
==========================  ===================================================
``clearOutput()``           Clears text from the Info panel.
``currentFormatToTime()``   Converts string time value to a numeric time value.
``generateRandomNumber()``  Generates a random number.
``timeToCurrentFormat()``   Converts a numeric time value to a string time
                            value.
``write()``                 Writes text to the Info panel, with no line break
                            added.
``writeLn()``               Writes text to the Info panel, adding a line break
                            at the end.
``isValid()``               When true, the specified object exists.
==========================  ===================================================

Additional global functions for standard user I/O (``alert``, ``confirm`` , and ``prompt``) and static functions for file I/O, are defined by ExtendScript; for detailed reference information, see the JavaScript Tools Guide (available from the ExtendScript Toolkit's Help menu).

----

.. _clearOutput:

clearOutput()
*************

``clearOutput()``

**Description**

Clears the output in the Info panel.

**Parameters**

None.

**Returns**

Nothing.

----

.. _currentFormatToTime:

currentFormatToTime()
*********************

``currentFormatToTime(formattedTime, fps[, isDuration])``

**Description**

Converts a formatted string for a frame time value to a number of seconds, given a specified frame rate. For example, if the formatted frame time value is 0:00:12 (the exact string format is determined by a project setting), and the frame rate is 24 fps, the time would be 0.5 seconds (12/24). If the frame rate is 30 fps, the time would be 0.4 seconds (12/30). If the time is a duration, the frames are counted from 0. Otherwise, the frames are counted from the project's starting frame (see :ref:`Project.displayStartFrame`).

**Parameters**

=================  ============================================================
``formattedTime``  The frame time value, a string specifying a number of
                   frames in the project's current time display format.
``fps``            The frames-per-second, a floating-point value.
``isDuration``     Optional. When true, the time is a duration (measured from
                   frame 0). When false (the default), the time is measured
                   from the project's starting frame.
=================  ============================================================

**Returns**

Floating-point value, the number of seconds.

----

.. _generateRandomNumber:

generateRandomNumber()
**********************

``generateRandomNumber()``

.. note::
   This functionality was added in After Effects 13.6 (CC 2015)

**Description**

Generates random numbers. This function is recommended instead of ``Math.random`` for generating random numbers that will be applied as values in a project (e.g., when using setValue).

This method avoids a problem where ``Math.random`` would not return random values in After Effects CC 2015 (13.5.x) due to a concurrency issue with multiple CPU threads.

**Returns**

Floating-point, pseudo-random number in the range [0, 1].

**Example**

::

    // change the position X of all layers with random number

    var myComp = app.project.activeItem;
    var x = 0;

    for (var i = 1; i <= myComp.numLayers; i++) {
        // If you use Math.random(), this does not work
        // x = 400*(Math.random()) – 200;
        // use new generateRandomNumber() instead

        x = 400*(generateRandomNumber()) – 200;
        currentPos = myComp.layer(i).property(“Position”).value;
        myComp.layer(i).property(“Position”).setValue([currentPos[0]+x,currentPos[1]]);
    }

----

.. _isValid:

isValid()
*********

``isValid(obj)``

**Description**

Determines if the specified After Effects object (e.g., composition, layer, mask, etc.) still exists. Some operations, such as :ref:`PropertyBase.moveTo`, might invalidate existing variable assignments to related objects. This function allows you to test whether those assignments are still valid before attempting to access them.

**Parameters**

=======  ===============================================
``obj``  The After Effects object to check for validity.
=======  ===============================================

**Returns**

Boolean.

**Example**

::

    var layer = app.project.activeItem.layer(1); // assume layer has three masks
    alert(isValid(layer)); // displays "true"
    var mask1 = layer.mask(1);
    var mask2 = layer.mask(2);
    var mask3 = layer.mask(3);
    mask3.moveTo(1); // move the third mask to the top of the mask stack
    alert(isValid(mask1)); // displays "false"; mask2 and mask3 do as well

----

.. _timeToCurrentFormat:

timeToCurrentFormat()
*********************

``timeToCurrentFormat(time, fps[, isDuration])``

**Description**

Converts a numeric time value (a number of seconds) to a frame time value; that is, a formatted string thatshows which frame corresponds to that time, at the specified rate. For example, if the time is 0.5 seconds, andthe frame rate is 24 fps, the frame would be 0:00:12 (when the project is set to display as timecode). If the framerate is 30 fps, the frame would be 0:00:15. The format of the timecode string is determined by a project setting. If the time is a duration, the frames are counted from 0. Otherwise, the frames are counted from the project's starting frame (see :ref:`Project displayStartFrame <project.displayStartFrame>` attribute).

**Parameters**

==============  ===============================================================
``time``        The number of seconds, a floating-point value.
``fps``         The frames-per-second, a floating-point value.
``isDuration``  Optional. When true, the time is a duration (measured from
                frame 0). When false (the default), the time is measured from
                the project's starting frame.
==============  ===============================================================

**Returns**

String in the project's current time display format.

----

.. _write:

write()
*******

``write(text)``

**Description**

Writes output to the Info panel, with no line break added.

**Parameters**

``text`` The string to display. Truncated if too long for the Info panel.

**Returns**

Nothing.

**Example**

::

    write("This text appears in Info panel ");
    write("with more on same line.");

----

.. _writeLn:

writeLn()
*********

``writeLn(text)``

**Description**

Writes output to the Info panel and adds a line break at the end.

**Parameters**

``text`` The string to display.

**Returns**

Nothing.

**Example**

::

    writeln("This text appears on first line");
    writeln("This text appears on second line");
