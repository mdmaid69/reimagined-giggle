import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)