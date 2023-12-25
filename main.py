import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import os
def change_working_directory(path):
        os.chdir(path)