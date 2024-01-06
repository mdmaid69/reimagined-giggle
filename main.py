import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def remove_duplicates(lst):
        return list(set(lst))