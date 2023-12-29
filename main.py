import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result