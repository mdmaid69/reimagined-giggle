import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)