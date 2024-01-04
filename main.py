import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result