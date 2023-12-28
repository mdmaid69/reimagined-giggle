import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def pop_from_array(array, i=-1):
        return array.pop(i)