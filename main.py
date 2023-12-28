import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_sign(x):
        return math.copysign(1, x)