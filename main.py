import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()