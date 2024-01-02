import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()