import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_logarithm(base, x):
        return math.log(x, base)