import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)