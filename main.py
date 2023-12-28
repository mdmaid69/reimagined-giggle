import array
def get_array_as_tuple(array):
        return tuple(array)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()