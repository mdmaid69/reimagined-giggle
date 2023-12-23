def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()