import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def find_max(lst):
        return max(lst)