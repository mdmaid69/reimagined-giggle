import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()