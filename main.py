import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def insert_into_array(array, i, item):
        array.insert(i, item)