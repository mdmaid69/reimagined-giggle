import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def find_max(numbers):
        return max(numbers)