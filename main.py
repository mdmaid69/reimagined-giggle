import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)