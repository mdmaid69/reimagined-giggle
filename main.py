import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a