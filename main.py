import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)