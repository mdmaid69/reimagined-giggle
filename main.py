import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")