import os
def get_file_size(filename):
        return os.path.getsize(filename)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))