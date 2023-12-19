import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def find_union(list1, list2):
        return set(list1) | set(list2)