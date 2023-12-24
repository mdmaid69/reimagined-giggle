import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)