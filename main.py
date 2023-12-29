import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()