import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()