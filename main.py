n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result