import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def divide_numbers(x, y):
        return x / y