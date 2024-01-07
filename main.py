def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result