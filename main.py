import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def find_min(numbers):
        return min(numbers)