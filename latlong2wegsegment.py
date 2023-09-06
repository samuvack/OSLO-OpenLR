import pyproj

# Define the input and output coordinate systems using EPSG codes
# Example: EPSG code for Belgian Lambert 72
input_crs = pyproj.CRS("EPSG:31370")
# Example: EPSG code for WGS 84 (latitude/longitude)
output_crs = pyproj.CRS("EPSG:4326")

# Define the point's coordinates in the input coordinate system
input_x = 150000  # Replace with your input x-coordinate
input_y = 170000  # Replace with your input y-coordinate

# Create a pyproj Transformer for the conversion
transformer = pyproj.Transformer.from_crs(
    input_crs, output_crs, always_xy=True)

# Perform the coordinate transformation
output_x, output_y = transformer.transform(input_x, input_y)

print("Input Coordinates (EPSG:31370):", input_x, input_y)
print("Output Coordinates (EPSG:4326):", output_x, output_y)
