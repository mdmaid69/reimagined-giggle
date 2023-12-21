import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result