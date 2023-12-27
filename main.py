import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)