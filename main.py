import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def append_to_array(array, item):
        array.append(item)