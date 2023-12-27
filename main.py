import math
def calculate_error_function(x):
        return math.erf(x)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)