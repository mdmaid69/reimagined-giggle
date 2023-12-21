import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)