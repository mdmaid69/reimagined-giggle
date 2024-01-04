import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)