import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)