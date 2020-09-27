# Set utility functions
from utilities.ImageUtilities import imageReadL, showImageL, createImageF
from utilities.PrintUtilities import printImageRangeL
from utilities.PlotUtilities import plotColorSurface, plot3DColorHistogram

'''
Parameters:
    pathToDir = Input image directory
    imageName = Input image name
'''
PATH_TO_DIR = "../Images/Chapter1/Input/"
image_name = "SmoothSquare.png"

# Read image into array
input_image, width, height = imageReadL(PATH_TO_DIR + image_name)
# Show input image
showImageL(input_image)

# Print pixel's values in an image range
printImageRangeL(input_image, [0, width-1], [0, height-1])

# Create an image to store the z values for surface
outputZ = createImageF(width, height)
# Three float array to store colors of the surface
colorsRGB = createImageF(width, height, 3)

# Set surface and color values
for x in range(0, width):
    for y in range(0, height):
        pixel_value = float(input_image[y, x])
        outputZ[y, x] = 255 - pixel_value
        point_colour = float(input_image[y, x]) / 255.0
        colorsRGB[y, x] = [point_colour, point_colour, point_colour]

# Plot surface
plotColorSurface(outputZ, colorsRGB, [0, 400], 1)
# Plot histogram
plot3DColorHistogram(outputZ, colorsRGB, [0, 400])
