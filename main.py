import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import math
def calculate_sign(x):
        return math.copysign(1, x)