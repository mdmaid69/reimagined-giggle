import array
def get_string_from_array(array):
        return array.tobytes()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()