import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import os
def get_file_size(filename):
        return os.path.getsize(filename)