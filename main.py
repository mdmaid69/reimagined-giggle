import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)