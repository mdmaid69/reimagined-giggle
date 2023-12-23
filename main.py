import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result