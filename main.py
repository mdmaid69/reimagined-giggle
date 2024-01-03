import os
def get_current_working_directory():
        return os.getcwd()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))