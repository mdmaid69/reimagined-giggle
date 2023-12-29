import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)