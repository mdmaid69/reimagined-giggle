import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result