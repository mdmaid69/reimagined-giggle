import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()