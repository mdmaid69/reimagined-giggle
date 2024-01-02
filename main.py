  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()