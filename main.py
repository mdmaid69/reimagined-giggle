import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)