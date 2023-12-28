import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)