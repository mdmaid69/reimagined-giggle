import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)