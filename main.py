import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)