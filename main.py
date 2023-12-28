import os
def get_file_size(filename):
        return os.path.getsize(filename)
import math
def calculate_sign(x):
        return math.copysign(1, x)