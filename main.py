import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)