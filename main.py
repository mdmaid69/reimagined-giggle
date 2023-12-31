import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)