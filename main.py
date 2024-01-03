numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result