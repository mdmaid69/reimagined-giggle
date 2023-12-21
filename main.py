import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_array_typecode(array):
        return array.typecode