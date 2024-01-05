import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result