import os
def get_file_size(filename):
        return os.path.getsize(filename)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)