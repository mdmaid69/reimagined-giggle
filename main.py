import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)