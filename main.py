def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result