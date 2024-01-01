import array
def get_array_as_bytes(array):
        return bytes(array)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()