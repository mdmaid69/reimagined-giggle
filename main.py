import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)