from pixelgen.core import PixelGenerator
from pixelgen.tools import create_pattern, create_circle, create_noise
import numpy as np

def create_pixel_landscape():
    # Initialize a 64x64 canvas
    art = PixelGenerator(64, 64)
    
    # Add background layer
    sky = art.add_layer("sky")
    # Create sky gradient from light blue to darker blue
    sky.fill_area(0, 0, 64, 32, (135, 206, 235))  # Light blue
    sky.fill_area(0, 32, 64, 64, (65, 105, 225))  # Royal blue
    
    # Add sun
    sun_circle = create_circle(8, (255, 223, 0))  # Yellow sun
    art.paste(sun_circle, (45, 10))
    
    # Add clouds
    clouds = art.add_layer("clouds")
    cloud_pattern = create_noise(15, 8, 0.7)
    # Make the noise white for clouds - fixed version
    cloud_pattern[cloud_pattern > 0] = 255  # Set all channels to white where mask is True
    clouds.paste(cloud_pattern, (10, 15))
    clouds.paste(cloud_pattern, (35, 12))
    
    # Add mountains
    mountains = art.add_layer("mountains")
    # Create triangular mountains
    for x, height in [(10, 20), (25, 25), (40, 18)]:
        for y in range(height):
            width = y
            mountains.fill_area(x - width, 40 - y, x + width, 41 - y, (100, 100, 100))
    
    # Add ground
    ground = art.add_layer("ground")
    # Create grass pattern
    grass_pattern = create_pattern(4, (34, 139, 34), (50, 205, 50))  # Dark and light green
    for x in range(0, 64, 4):
        ground.paste(grass_pattern, (x, 40))
    
    # Add trees
    trees = art.add_layer("trees")
    def draw_tree(x, y):
        # Tree trunk
        trees.fill_area(x, y-8, x+2, y, (139, 69, 19))  # Brown
        # Tree leaves
        leaf_circle = create_circle(4, (0, 100, 0))  # Dark green
        trees.paste(leaf_circle, (x-3, y-12))
    
    # Place some trees
    tree_positions = [(15, 40), (50, 40), (30, 42)]
    for x, y in tree_positions:
        draw_tree(x, y)
    
    # Save the final result
    art.save_image("pixel_landscape.png")
    
    return art

if __name__ == "__main__":
    # Create the landscape
    landscape = create_pixel_landscape()
    print("Pixel art landscape has been created and saved as 'pixel_landscape.png'")