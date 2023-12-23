import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a