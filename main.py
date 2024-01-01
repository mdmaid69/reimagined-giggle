import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)