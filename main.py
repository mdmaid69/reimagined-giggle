import math
def calculate_sign(x):
        return math.copysign(1, x)
import os
def remove_directory(path):
        os.rmdir(path)