import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])