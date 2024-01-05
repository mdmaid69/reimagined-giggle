import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def sort_numbers(numbers):
        return sorted(numbers)