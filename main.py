import os
def get_environment_variable(var):
        return os.getenv(var)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))