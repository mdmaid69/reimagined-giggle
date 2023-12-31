import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)