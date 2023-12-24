import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def sort_list(lst):
        return sorted(lst)