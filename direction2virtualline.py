import math
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points
import numpy as np
import geopandas as gpd




# Define the starting point (x, y)
start_point = Point(104565.25, 193090.11)


# Define the direction in degrees (measured clockwise from the north)
direction_degrees = 45  # Replace with your desired direction

# Convert the direction from degrees to radians
direction_radians = math.radians(direction_degrees)

# Define the fixed length
fixed_length = 20  # 20 meters

# Calculate the new coordinates
end_x = start_point.x + fixed_length * math.sin(direction_radians)
end_y = start_point.y + fixed_length * math.cos(direction_radians)

# Create a new Point object based on the calculated coordinates
end_point = Point(end_x, end_y)
print(end_point)
middle_point = Point((end_x+start_point.x)/2, (end_y+start_point.y)/2)
print(middle_point)
roadsegment = LineString([start_point, middle_point, end_point])
print(roadsegment)


true_north = LineString([start_point, Point(
    start_point.x + 100 * math.sin(0), start_point.y + 100 * math.cos(0))])


# Visualisation
# Create a GeoDataFrame for points

start_point_gdf = gpd.GeoDataFrame(geometry=[start_point])
end_point_gdf = gpd.GeoDataFrame(geometry=[end_point])
virtual_line_gdf = gpd.GeoDataFrame(geometry=[roadsegment])
true_north_gdf = gpd.GeoDataFrame(geometry=[true_north])
middle_point_gdf = gpd.GeoDataFrame(geometry=[middle_point])

# Plotting using Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))


# Calculate the bounding box of all geometries
bbox = virtual_line_gdf.total_bounds


# Set the x and y limits based on the bounding box
ax.set_xlim(bbox[0]-50, bbox[2]+50)
ax.set_ylim(bbox[1]-50, bbox[3]+50)


# Plot the points and LineString
start_point_gdf.plot(ax=ax, color='red', markersize=50,
                     label="measuring point")
middle_point_gdf.plot(ax=ax, color='orange', markersize=50,
                     label="measuring point")
end_point_gdf.plot(ax=ax, color='green', markersize=50,
                     label="start point of road segment")
virtual_line_gdf.plot(ax=ax, color='blue', linewidth=3)
true_north_gdf.plot(ax=ax, color='grey', linewidth=1)

# Set plot title
plt.title("Calculating virtual road segment and points based on start point and direction")

# Show the plot
plt.legend()
# Show the plot
plt.show()
