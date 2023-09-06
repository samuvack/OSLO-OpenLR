import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points
import numpy as np
from shapely.geometry import Point
from shapely.geometry import LineString
import geopandas as gpd
from shapely.geometry import Point, LineString
import time
start_time = time.time()

print("Importing road segment data and adding indexes on the data")


lines_gdf = gpd.read_file("./example_roadsegment/Wegsegment44021.shp")
lines_gdf.sindex

end_time = time.time()
execution_time = end_time - start_time

print("Execution time import road segments:", execution_time)


x = 104565.25
y = 193090.11

measuring_point = Point(x, y)

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
roadsegment = str(closest_line).replace('LINESTRING (', '"Geometrie.gml": {"@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\">').replace(')', '') +  '< gml: coordinates > </gml: coordinates > <gml: Point >, "@type": "geosparql:gmlliteral"'

first = Point(closest_line.coords[0])
last = Point(closest_line.coords[-1])

print(first)
print(last)

output = [roadsegment, closest_line, first, last]

print(output)

# Find the nearest points on the LineString
projected_point = nearest_points(closest_line, measuring_point)[0]

offset = closest_line.project(projected_point)
print(offset)
print(closest_line.length)

print(closest_line)

# Visualisation

# Create a GeoDataFrame for points



point_geoms = [measuring_point, projected_point]
start_geoms = [first]
point_gdf = gpd.GeoDataFrame(geometry=point_geoms)
start_point_gdf = gpd.GeoDataFrame(geometry=start_geoms)

# Create a GeoDataFrame for the LineString
line_gdf = gpd.GeoDataFrame(geometry=[closest_line])

# Plotting using Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))

bounding_gdf = gpd.GeoDataFrame(
    geometry=[closest_line, measuring_point, projected_point])


# Calculate the bounding box of all geometries
bbox = bounding_gdf.total_bounds


# Set the x and y limits based on the bounding box
ax.set_xlim(bbox[0]-50, bbox[2]+50)
ax.set_ylim(bbox[1]-50, bbox[3]+50)



# Plot the points and LineString
point_gdf.plot(ax=ax, color='red', markersize=50, label="measuring point")
start_point_gdf.plot(ax=ax, color='green', markersize=50, label="start point of road segment")
line_gdf.plot(ax=ax, color='blue', linewidth=3)
lines_gdf.plot(ax=ax, color='grey', linewidth=1)

# Set plot title
plt.title("Map with measuring points and road segment")

# Show the plot
plt.legend()
# Show the plot
plt.show()

