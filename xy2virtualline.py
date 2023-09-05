from shapely.geometry import Point
from shapely.geometry import LineString
import geopandas as gpd
from shapely.geometry import Point, LineString
import time
import matplotlib.pyplot as plt
start_time = time.time()


def calculate_middle_point(point1, point2):
    middle_x = (point1.x + point2.x) / 2
    middle_y = (point1.y + point2.y) / 2
    middle_point = Point(middle_x, middle_y)
    return middle_point



start_coord = (104541.05309983343, 193139.3552721031)
end_coord = (104547.02301983535, 193072.06298405677)

# Create Point objects from coordinates
start_point = Point(start_coord)
end_point = Point(end_coord)



# Calculate the middle point
middle_point = calculate_middle_point(start_point, end_point)

# Create a LineString from the points
roadsegment = LineString([start_point, middle_point, end_point])



# Visualisation
# Create a GeoDataFrame for points
start_gdf = gpd.GeoDataFrame(geometry=[start_point])
end_gdf = gpd.GeoDataFrame(geometry=[end_point])
middle_gdf = gpd.GeoDataFrame(geometry=[middle_point])
line_gdf = gpd.GeoDataFrame(geometry=[roadsegment])


# Plotting using Matplotlib
fig, ax = plt.subplots(figsize=(10, 4))

bounding_gdf = gpd.GeoDataFrame(
    geometry=[roadsegment])


# Calculate the bounding box of all geometries
bbox = bounding_gdf.total_bounds


# Set the x and y limits based on the bounding box
ax.set_xlim(bbox[0]-200, bbox[2]+200)
ax.set_ylim(bbox[1]-50, bbox[3]+50)

# Plot the points and LineString
start_gdf.plot(ax=ax, color='red', markersize=50, label="start point")
end_gdf.plot(ax=ax, color='green', markersize=50, label="end point")
middle_gdf.plot(ax=ax, color='blue', markersize=50, label="middle point")
line_gdf.plot(ax=ax, color='blue', linewidth=3)

# Set plot title
plt.title("Map with measuring points and virtual road segment")

# Show the plot
plt.legend()
# Show the plot
plt.show()
