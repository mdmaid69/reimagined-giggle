import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_bytes_from_array(array):
        return array.tobytes()