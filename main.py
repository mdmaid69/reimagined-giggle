import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result