import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import glob
def find_files(pattern):
        return glob.glob(pattern)