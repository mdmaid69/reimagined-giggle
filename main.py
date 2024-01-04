import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)