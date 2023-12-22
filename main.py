def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result