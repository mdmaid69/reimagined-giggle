import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def reverse_list(lst):
        return lst[::-1]