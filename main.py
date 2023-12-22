import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)