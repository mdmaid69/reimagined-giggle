import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)