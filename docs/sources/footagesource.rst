.. _FootageSource:

FootageSource object
################################################

|  ``app.project.item(index).mainSource``
|  ``app.project.item(index).proxySource``

**Description**

The FootageSource object holds information describing the source of some footage. It is used as the ``mainSource`` of a :ref:`FootageItem`, or the ``proxySource`` of a :ref:`CompItem` or FootageItem.

    FootageSource is the base class for :ref:`SolidSource`, so FootageSource attributes and methods are available when working with SolidSource objects.

----

==========
Attributes
==========

.. _FootageSource.alphaMode:

FootageSource.alphaMode
*********************************************

|  ``app.project.item(index).mainSource.alphaMode``
|  ``app.project.item(index).proxySource.alphaMode``

**Description**

Defines how the alpha information in the footage is interpreted. If ``hasAlpha`` is false, this attribute has no relevant meaning.

**Type**

An Alpha Mode enumerated value; (read/write). One of:

-  ``AlphaMode.IGNORE``
-  ``AlphaMode.STRAIGHT``
-  ``AlphaMode.PREMULTIPLIED``

----

.. _FootageSource.conformFrameRate:

FootageSource.conformFrameRate
*********************************************

|  ``app.project.item(index).mainSource.conformFrameRate``
|  ``app.project.item(index).proxySource.conformFrameRate``

**Description**

A frame rate to use instead of the ``nativeFrameRate`` value. If set to 0, the ``nativeFrameRate`` is used instead. It is an error to set this value if :ref:`FootageSource.isStill` is true. It is an error to set this value to 0 if :ref:`removePulldown <FootageSource.removePulldown>` is not set to ``PulldownPhase.OFF``. If this is 0 when you set ``removePulldown`` to a value other than ``PulldownPhase.OFF``, then this is automatically set to the value of ``nativeFrameRate``.

**Type**

Floating-point value in the range ``[0.0..99.0]``; read/write.

----

.. _FootageSource.displayFrameRate:

FootageSource.displayFrameRate
*********************************************

|  ``app.project.item(index).mainSource.displayFrameRate``
|  ``app.project.item(index).proxySource.displayFrameRate``

**Description**

The effective frame rate as displayed and rendered in compositions by After Effects. If :ref:`removePulldown <FootageSource.removePulldown>` is ``PulldownPhase.OFF``, then this is the same as the ``conformFrameRate`` (if non-zero) or the ``nativeFrameRate`` (if ``conformFrameRate`` is 0). If ``removePulldown`` is not ``PulldownPhase.OFF``, this is ``conformFrameRate * 0.8``, the effective frame rate after removing 1 of every 5 frames.

**Type**

Floating-point value in the range ``[0.0..99.0]``; read-only.

----

.. _FootageSource.fieldSeparationType:

FootageSource.fieldSeparationType
*********************************************

|  ``app.project.item(index).mainSource.fieldSeparationType``
|  ``app.project.item(index).proxySource.fieldSeparationType``

**Description**

How the fields are to be separated in non-still footage. It is an error to set this attribute if ``isStill`` is true. It is an error to set this value to ``FieldSeparationType.OFF`` if :ref:`removePulldown <FootageSource.removePulldown>` is not ``PulldownPhase.OFF``.

**Type**

A ``FieldSeparationType`` enumerated value; read/write. One of:

-  ``FieldSeparationType.OFF``
-  ``FieldSeparationType.UPPER_FIELD_FIRST``
-  ``FieldSeparationType.LOWER_FIELD_FIRST``

----

.. _FootageSource.hasAlpha:

FootageSource.hasAlpha
*********************************************

|  ``app.project.item(index).mainSource.hasAlpha``
|  ``app.project.item(index).proxySource.hasAlpha``

**Description**

When true, the footage has an alpha component. In this case, the attributes ``alphaMode``, ``invertAlpha``, and ``premulColor`` have valid values. When ``false``, those attributes have no relevant meaning for the footage.

**Type**

Boolean; read-only.

----

.. _FootageSource.highQualityFieldSeparation:

FootageSource.highQualityFieldSeparation
*********************************************

|  ``app.project.item(index).mainSource.highQualityFieldSeparation``
|  ``app.project.item(index).proxySource.highQualityFieldSeparation``

**Description**

When true, After Effects uses special algorithms to determine how to perform high-quality field separation. It is an error to set this attribute if ``isStill`` is true, or if ``fieldSeparationType`` is ``FieldSeparationType.OFF``.

**Type**

Boolean; read/write.

----

.. _FootageSource.invertAlpha:

FootageSource.invertAlpha
*********************************************

|  ``app.project.item(index).mainSource.invertAlpha``
|  ``app.project.item(index).proxySource.invertAlpha``

**Description**

When true, an alpha channel in a footage clip or proxy should be inverted. This attribute is valid only if an alpha is present. If ``hasAlpha`` is false, or if ``alphaMode`` is ``AlphaMode.IGNORE``, this attribute is ignored.

**Type**

Boolean; read/write.

----

.. _FootageSource.isStill:

FootageSource.isStill
*********************************************

|  ``app.project.item(index).mainSource.isStill``
|  ``app.project.item(index).proxySource.isStill``

**Description**

When true the footage is still; when false, it has a time-based component. Examples of still footage are JPEG files, solids, and placeholders with a duration of 0. Examples of non-still footage are movie files, sound files, sequences, and placeholders of non-zero duration.

**Type**

Boolean; read-only.

----

.. _FootageSource.loop:

FootageSource.loop
*********************************************

|  ``app.project.item(index).mainSource.loop``
|  ``app.project.item(index).proxySource.loop``

**Description**

The number of times that the footage is to be played consecutively when used in a composition. It is an error to set this attribute if ``isStill`` is true.

**Type**

Integer in the range ``[1..9999]``; default is 1; read/write.

----

.. _FootageSource.nativeFrameRate:

FootageSource.nativeFrameRate
*********************************************

|  ``app.project.item(index).mainSource.nativeFrameRate``
|  ``app.project.item(index).proxySource.nativeFrameRate``

**Description**

The native frame rate of the footage.

**Type**

Floating-point; read-only.

----

.. _FootageSource.premulColor:

FootageSource.premulColor
*********************************************

|  ``app.project.item(index).mainSource.premulColor``
|  ``app.project.item(index).proxySource.premulColor``

**Description**

The color to be premultiplied. This attribute is valid only if the ``alphaMode`` is ``alphaMode.PREMULTIPLIED``.

**Type**

Array of three floating-point values ``[R, G, B]``, in the range ``[0.0..1.0]``; read/write.

----

.. _FootageSource.removePulldown:

FootageSource.removePulldown
*********************************************

|  ``app.project.item(index).mainSource.removePulldown``
|  ``app.project.item(index).proxySource.removePulldown``

**Description**

How the pulldowns are to be removed when field separation is used. It is an error to set this attribute if ``isStill`` is true. It is an error to attempt to set this to a value other than ``PulldownPhase.OFF`` in the case where ``fieldSeparationType`` is ``FieldSeparationType.OFF``.

**Type**

A ``PulldownPhase`` enumerated value; read/write. One of:

-  ``PulldownPhase.RemovePulldown.OFF``
-  ``PulldownPhase.RemovePulldown.WSSWW``
-  ``PulldownPhase.RemovePulldown.SSWWW``
-  ``PulldownPhase.RemovePulldown.SWWWS``
-  ``PulldownPhase.RemovePulldown.WWWSS``
-  ``PulldownPhase.RemovePulldown.WWSSW``
-  ``PulldownPhase.RemovePulldown.WSSWW_24P_ADVANCE``
-  ``PulldownPhase.RemovePulldown.SSWWW_24P_ADVANCE``
-  ``PulldownPhase.RemovePulldown.SWWWS_24P_ADVANCE``
-  ``PulldownPhase.RemovePulldown.WWWSS_24P_ADVANCE``
-  ``PulldownPhase.RemovePulldown.WWSSW_24P_ADVANCE``

----

=======
Methods
=======

.. _FootageSource.guessAlphaMode:

FootageSource.guessAlphaMode()
*********************************************

|  ``app.project.item(index).mainSource.guessAlphaMode()``
|  ``app.project.item(index).proxySource.guessAlphaMode()``

**Description**

Sets ``alphaMode``, ``premulColor``, and ``invertAlpha`` to the best estimates for this footage source. If ``hasAlpha`` is false, no change is made.

**Parameters**

None.

**Returns**

Nothing.

----

.. _FootageSource.guessPulldown:

FootageSource.guessPulldown()
*********************************************

|  ``app.project.item(index).mainSource.guessPulldown(method)``
|  ``app.project.item(index).proxySource.guessPulldown(method)``

**Description**

Sets ``fieldSeparationType`` and :ref:`removePulldown <FootageSource.removePulldown>` to the best estimates for this footage source. If ``isStill`` is true, no change is made.

**Parameters**

==========  =================================================================
``method``  The method to use for estimation. A ``PulldownMethod`` enumerated
            value, one of:

            -  ``PulldownMethod.PULLDOWN_3_2``
            -  ``PulldownMethod.ADVANCE_24P``
==========  =================================================================

**Returns**

Nothing.
