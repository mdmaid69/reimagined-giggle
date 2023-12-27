import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import os
def get_current_working_directory():
        return os.getcwd()