import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))