import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import os
def list_files_in_directory(path):
        return os.listdir(path)