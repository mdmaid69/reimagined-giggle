import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time