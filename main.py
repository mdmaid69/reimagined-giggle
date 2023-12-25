def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()