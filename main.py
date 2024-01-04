import sys
def print_python_version():
        print(sys.version)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)