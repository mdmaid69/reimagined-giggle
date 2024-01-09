import math
def calculate_sign(x):
        return math.copysign(1, x)
import glob
def find_files(pattern):
        return glob.glob(pattern)