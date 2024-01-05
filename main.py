import array
def get_array_slice(array, i, j):
        return array[i:j]
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()