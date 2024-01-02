import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}