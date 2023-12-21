import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result