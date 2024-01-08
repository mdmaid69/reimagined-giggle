import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()