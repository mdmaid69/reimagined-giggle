import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()