import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import shutil
def delete_directory(path):
        shutil.rmtree(path)