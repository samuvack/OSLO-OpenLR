# OSLO-OpenLR
OpenLR OSLO converter

## XY2wegsegment
This script searches for the closest road segment from a given shape file with multiple road segments (e.g. wegenregister, openstreetmap, etc.)
Afterward, the script defines the projected point on the closest road segment.

![](https://github.com/samuvack/OSLO-OpenLR/blob/main/images/projected_point.png)

Input:
x = 104565.25
y = 193090.11

Available output:
* geometry: "@value": "<gml:Point srsName="http:\\//www.opengis.net/def/crs/EPSG/0/31370">104541.05309983343 193139.3552721031, 104541.65002783388 193126.81300009415, 104546.12599583715 193081.20397606492, 104547.02301983535 193072.06298405677< gml: coordinates > </gml: coordinates > <gml: Point >, "@type": "geosparql:gmlliteral"'
* offset: 51.38896740223392
* length road segment : 67.56949730731361
* road segment: LINESTRING (104541.05309983343 193139.3552721031, 104541.65002783388 193126.81300009415, 104546.12599583715 193081.20397606492, 104547.02301983535 193072.06298405677)
* Start point:POINT (104541.05309983343 193139.3552721031)
* End point: POINT (104547.02301983535 193072.06298405677)


## XY2virtualline
This script calculates the virtual position of the measuring point between start and end point. Afterward, the virtual road segment is defined.

![](https://github.com/samuvack/OSLO-OpenLR/blob/main/images/virtual_roadsegment.png)

## Direction2virtual line
![](https://github.com/samuvack/OSLO-OpenLR/blob/main/images/direction2virtualline.png)



## latlon2wegsegment
same as  XY2wegsegment, but with transforming from EPSG:4326 to EPSG:31370.

## latlon2virtual line
same as  XY2virtualline, but with transforming from EPSG:4326 to EPSG:31370.

