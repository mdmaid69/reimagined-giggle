import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity