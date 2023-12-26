import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()