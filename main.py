import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result