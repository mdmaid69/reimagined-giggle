import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)