import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)