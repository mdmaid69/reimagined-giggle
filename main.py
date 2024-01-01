import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)