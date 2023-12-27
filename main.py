import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import math
def calculate_combinations(n, k):
        return math.comb(n, k)