import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)