import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)