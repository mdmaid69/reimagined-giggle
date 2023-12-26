import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)