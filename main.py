import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)