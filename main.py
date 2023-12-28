import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)