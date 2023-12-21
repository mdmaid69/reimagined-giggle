import array
def get_array_as_bytearray(array):
        return bytearray(array)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()