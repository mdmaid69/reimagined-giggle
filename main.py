import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3