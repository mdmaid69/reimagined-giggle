import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height