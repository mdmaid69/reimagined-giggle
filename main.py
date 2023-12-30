import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_sign(x):
        return math.copysign(1, x)