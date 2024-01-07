import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import os
def get_current_working_directory():
        return os.getcwd()