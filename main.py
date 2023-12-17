import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_sign(x):
        return math.copysign(1, x)