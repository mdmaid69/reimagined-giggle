import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def extend_array(array, iterable):
        array.extend(iterable)