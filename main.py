import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)