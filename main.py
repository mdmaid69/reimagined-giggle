import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import logging
def setup_logging(level):
        logging.basicConfig(level=level)