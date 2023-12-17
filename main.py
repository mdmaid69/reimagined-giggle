import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"