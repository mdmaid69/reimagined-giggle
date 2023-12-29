import os
def remove_directory(path):
        os.rmdir(path)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)