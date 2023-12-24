import os
def list_files_in_directory(path):
        return os.listdir(path)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)