import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import sys
def add_to_python_path(path):
        sys.path.append(path)