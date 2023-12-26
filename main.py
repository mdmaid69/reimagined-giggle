import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()