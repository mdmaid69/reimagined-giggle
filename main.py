import math
def calculate_error_function(x):
        return math.erf(x)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()