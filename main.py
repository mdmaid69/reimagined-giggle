def find_difference(list1, list2):
        return set(list1) - set(list2)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()