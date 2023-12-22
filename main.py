import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)