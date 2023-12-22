import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_array_as_list(array):
        return list(array)