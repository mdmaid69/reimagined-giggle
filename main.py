import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import math
def calculate_sign(x):
        return math.copysign(1, x)