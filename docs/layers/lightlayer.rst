.. _LightLayer:

LightLayer object
#################

``app.project.item(index).layer(index)``

**Description**

The LightLayer object represents a light layer within a composition. Create it using the :ref:`LayerCollection.addLight` method. It can be accessed in an item's layer collection either by index number or by a name string.

    LightLayer is a subclass of :ref:`Layer`. All methods and attributes of Layer are available when working with Light-Layer.

**AE Properties**

LightLayer defines no additional attributes, but has different AE properties than other layer types. It has thefollowing properties and property groups:

-  ``Marker``
-  ``Transform``
    -  ``PointofInterest``
    -  ``Position``
    -  ``Scale``
    -  ``Orientation``
    -  ``XRotation``
    -  ``YRotation``
    -  ``Rotation``
    -  ``Opacity``
-  ``LightOptions``
    -  ``Intensity``
    -  ``Color``
    -  ``ConeAngle``
    -  ``ConeFeather``
    -  ``CastsShadows``
    -  ``ShadowDarkness``
    -  ``ShadowDiffusion``

----

==========
Attributes
==========

.. _LightLayer.lightType:

LightLayer.lightType
*********************************************

``app.project.item(index).layer(index).lightType``

**Description**

For a light layer, its light type. Trying to set this attribute for a non-light layer produces an error.

**Type**

A ``LightType`` enumerated value; read/write. One of:

-  ``LightType.PARALLEL``
-  ``LightType.SPOT``
-  ``LightType.POINT``
-  ``LightType.AMBIENT``
