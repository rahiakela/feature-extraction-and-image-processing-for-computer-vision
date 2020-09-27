from timeit import itertools
from utilities.ImageUtilities import imageReadL, showImageL, createImageL
from utilities.PrintUtilities import printImageRangeL

'''
Parameters:
    pathToDir = Input image directory
    imageName = Input image name
    brightDelta = Increase brightness
    printRange = Image range to print
'''
PATH_TO_DIR = "../Images/Chapter1/Input/"
image_name = "Zebra.png"

bright_delta = 80
print_range = [0, 10]

# Read image into array
input_image, width, height = imageReadL(PATH_TO_DIR + image_name)

# Output image
output_image = createImageL(width, height)

# Set the pixels in the output image
for x, y in itertools.product(range(0, width), range(0, height)):
    out_value = int(input_image[y, x]) + bright_delta
    if out_value < 255:
        output_image[y, x] = out_value
    else:
        output_image[y, x] = 255

# Show images
showImageL(input_image)
showImageL(output_image)

# Print image range
printImageRangeL(input_image, print_range, print_range)
printImageRangeL(output_image, print_range, print_range)