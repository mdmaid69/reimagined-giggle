import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)