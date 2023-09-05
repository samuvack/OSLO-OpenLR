# OSLO-OpenLR
OpenLR OSLO converter

## XY2wegsegment
This script searches for the closest road segment from a given shape file with multiple road segments (e.g. wegenregister, openstreetmap, etc.)
Afterward, the script defines the projected point on the closest road segment.

![](https://github.com/samuvack/OSLO-OpenLR/blob/main/images/projected_point.png)


## XY2virtualline
This script calculates the virtual position of the measuring point between start and end point. Afterward, the virtual road segment is defined.

![](https://github.com/samuvack/OSLO-OpenLR/blob/main/images/XY2virtualline.png)

## latlon2wegsegment
same as  XY2wegsegment, but with transforming from EPSG:4326 to EPSG:31370.

## latlon2virtual line
same as  XY2virtualline, but with transforming from EPSG:4326 to EPSG:31370.

