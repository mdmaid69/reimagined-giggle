import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)