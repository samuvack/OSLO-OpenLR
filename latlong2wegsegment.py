import geopandas as gpd
from shapely.geometry import Point, LineString
import time
start_time = time.time()

lines_gdf = gpd.read_file("./shape_wegsegment/Wegsegment.shp")
lines_gdf.sindex

end_time = time.time()
execution_time = end_time - start_time
print("Execution time import read segments:", execution_time)


x = 104562.25
y = 193090.11

# Create a GeoDataFrame with a single example point in EPSG:31370 coordinate system
point_data = {'geometry': [Point(x, y)]}
point_gdf = gpd.GeoDataFrame(point_data, crs='EPSG:31370')

# Initialize variables for finding the closest line
closest_line = None
min_distance = float('inf')

# Loop through each line to find the closest one to the point
for line in lines_gdf.geometry:
    # Calculate the distance between the point and the current line
    distance = point_gdf.geometry.iloc[0].distance(line)

    # Update minimum distance and closest line
    if distance < min_distance:
        min_distance = distance
        closest_line = line

# Output the closest line and its distance to the point
#print(f"The closest line to the point {x},{y} is {closest_line} with a distance of {min_distance}")
print(str(closest_line).replace('LINESTRING (', '"Geometrie.gml": {"@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\">').replace(')', '') +  '< gml: coordinates > </gml: coordinates > <gml: Point >, "@type": "geosparql:gmlliteral"')

  