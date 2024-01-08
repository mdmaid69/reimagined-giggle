import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result