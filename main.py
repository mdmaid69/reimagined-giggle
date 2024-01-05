import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)