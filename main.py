import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()