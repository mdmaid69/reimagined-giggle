import array
def get_array_as_complex(array):
        return complex(array[0])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()