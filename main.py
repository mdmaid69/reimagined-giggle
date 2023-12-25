import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b