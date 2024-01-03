import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def add_numbers(a, b):
        return a + b