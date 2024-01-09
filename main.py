import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def convert_array_to_bytes(array):
        return array.tobytes()