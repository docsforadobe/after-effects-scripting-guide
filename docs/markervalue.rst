.. highlight:: javascript
.. _MarkerValue:

MarkerValue object
################################################

``new MarkerValue(comment, chapter, url, frameTarget, cuePointName, params)``

**Description**

The MarkerValue object represents a layer, or composition, marker, which associates a comment, and optionally a chapter reference point, Web-page link, or Flash Video cue point with a particular point in a layer. Create it with the constructor; all arguments except ``comment`` are optional. All arguments are strings that set in the corresponding attributes of the returned MarkerValueo bject, except ``params``. This is an array containing key-value pairs, which can then be accessed with the :ref:`getParameters() <MarkerValue.getParameters>` and :ref:`setParameters() <MarkerValue.setParameters>` methods. A script can set any number of parameter pairs; the order does not reflect the order displayed in the application. To associate a marker with a layer, set the MarkerValue object in the ``Marker`` AE property of the layer: ``layerObject.property("Marker").setValueAtTime(time, markerValueObject);`` For information on the usage of markers see "Using markers" in After Effects Help.

**Examples**

- To set a marker that says "Fade Up" at the 2 second mark:

	::

		var myMarker = new MarkerValue("FadeUp");
		myLayer.property("Marker").setValueAtTime(2, myMarker);

- To get comment values from a particular marker:

	::

		var commentOfFirstMarker = app.project.item(1).layer(1).property("Marker").keyValue(1).comment;
		var commentOfMarkerAtTime4 = app.project.item(1).layer(1).property("Marker").valueAtTime(4.0, true).comment
		var markerProperty = app.project.item(1).layer(1).property("Marker");
		var markerValueAtTimeClosestToTime4 = markerProperty.keyValue(markerProperty.nearestKeyIndex(4.0));
		var commentOfMarkerClosestToTime4 = markerValueAtTimeClosestToTime4.comment;

----

==========
Attributes
==========

.. _MarkerValue.chapter:

MarkerValue.chapter
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).chapter``

**Description**

A text chapter link for this marker. Chapter links initiate a jump to a chapter in a QuickTime movie or in other formats that support chapter marks.

**Type**

String; read/write.

----

.. _MarkerValue.comment:

MarkerValue.comment
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).comment``

**Description**

A text comment for this marker. This comment appears in the Timeline panel next to the layer marker.

**Type**

String; read/write.

----

.. _MarkerValue.cuePointName:

MarkerValue.cuePointName
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).cuePointName``

**Description**

The Flash Video cue point name, as shown in the Marker dialog box.

**Type**

String; read/write.

----

.. _MarkerValue.duration:

MarkerValue.duration
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).duration``

**Description**

The marker’s duration, in seconds. The duration appears in the Timeline panel as a short bar extending from the marker location.

**Type**

Floating point; read/write.

----

.. _MarkerValue.eventCuePoint:

MarkerValue.eventCuePoint
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).eventCuePoint``

**Description**

When true, the FlashVideo cue point is for an event; otherwise, it is for navigation.

**Type**

Boolean; read/write.

----

.. _MarkerValue.frameTarget:

MarkerValue.frameTarget
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).frameTarget``

**Description**

A text frame target for this marker. Together with the URL value, this targets a specific frame within a Web page.

**Type**

String; read/write.

----

.. _MarkerValue.url:

MarkerValue.url
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).url``

**Description**

A URL for this marker. This URL is an automatic link to a Web page.

**Type**

String; read/write.

----

=======
Methods
=======

.. _MarkerValue.getParameters:

MarkerValue.getParameters()
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).getParameters()``

**Description**

Returns the key-value pairs for Flash Video cue-point parameters, for a cue point associated with this marker value.

**Parameters**

None.

**Returns**

An object with an attribute matching each parameter name, containing that parameter’s value.

----

.. _MarkerValue.setParameters:

MarkerValue.setParameters()
*********************************************

``app.project.item(index).layer(index).property("Marker").keyValue(index).setParameters(keyValuePairs)``

**Description**

Associates a set of key-value pairs for Flash Video cue-point parameters, for a cue point associated with this marker value. A cue point can have any number of parameters, but you can add only three through the user interface; use this method to add more than three parameters.

**Parameters**

==================	===========================================================
``keyValuePairs``	An object containing the key-value pairs as attributes and values. The object’s ``toString()`` method is called to assign the string value of each attribute to the named key.
==================	===========================================================

**Returns**

Nothing.

**Example**

::

	var mv = new MarkerValue("MyMarker");
	var parms = new Object;
	parms.timeToBlink = 1;
	parms.assignMe = "A string"
	mv.setParameters(parms);
	myLayer.property("Marker").setValueAtTime(2, mv);
