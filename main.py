import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)