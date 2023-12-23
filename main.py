import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import os
def get_file_size(filename):
        return os.path.getsize(filename)