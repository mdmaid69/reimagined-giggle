import math
def calculate_error_function(x):
        return math.erf(x)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)