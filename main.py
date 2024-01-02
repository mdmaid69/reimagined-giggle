import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_array_item_count(array, item):
        return array.count(item)