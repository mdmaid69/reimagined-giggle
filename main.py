import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def clear_array(array):
        array *= 0