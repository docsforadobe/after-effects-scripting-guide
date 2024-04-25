.. highlight:: javascript

.. _ThreeDModelLayer:

ThreeDModelLayer object
################################################

``app.project.item(index).layer(index)``

.. note::
   This functionality was added in After Effects (Beta) 24.4 and is subject to change while it remains in Beta.

**Description**

The ThreeDModelLayer object represents a 3D Model layer within a composition. 

ThreeDModelLayer is a subclass of :ref:`AVLayer`. All methods and attributes of AVLayer are available when working with ThreeDModelLayer.

**AE Properties**

ThreeDModelLayer inherits the following properties and property groups from :ref:`AVLayer`:

-  Marker
-  Time Remap
-  Transform

   -  Anchor Point
   -  Position
   -  Scale
   -  Orientation
   -  X Rotation
   -  Y Rotation
   -  Rotation
   -  Opacity

-  Layer Styles
-  Audio

   -  AudioLevels

**Example**

If the first item in the project is a CompItem, and the first layer of that CompItem is an ThreeDModelLayer, the following checks its type.

.. code:: javascript

    var modelLayer = app.project.item(1).layer(1);
    if (modelLayer instanceof ThreeDModelLayer)
    {
       // do something
    }
    
    

