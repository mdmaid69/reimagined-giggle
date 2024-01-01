import array
def get_array_buffer_info(array):
        return array.buffer_info()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()