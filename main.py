import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()