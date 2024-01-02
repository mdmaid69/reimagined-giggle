import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def is_odd(n):
        return n % 2 != 0