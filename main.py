import os
def change_working_directory(path):
        os.chdir(path)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))