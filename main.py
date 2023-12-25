import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)