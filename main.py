import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()