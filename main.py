import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b