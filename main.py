import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def set_array_item(array, i, item):
        array[i] = item