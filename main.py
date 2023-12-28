import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)