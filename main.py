import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def remove_from_array(array, item):
        array.remove(item)