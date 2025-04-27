from pixelgen.core import PixelGenerator
from pixelgen.tools import create_gradient, create_pattern

# Initialize a 32x32 canvas
pixel_art = PixelGenerator(32, 32)

# Set individual pixels
pixel_art.set_pixel(0, 0, (255, 0, 0))  # Red
pixel_art.set_pixel(1, 1, (0, 255, 0))  # Green

# Fill area with color
pixel_art.fill_area(10, 10, 20, 20, (0, 0, 255))  # Blue area

# Save result
pixel_art.save_image("pixel_art_result.png")