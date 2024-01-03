import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)