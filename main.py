import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)