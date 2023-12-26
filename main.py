import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result