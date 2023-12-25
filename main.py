import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()