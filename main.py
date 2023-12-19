import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)