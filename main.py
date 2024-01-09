import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)