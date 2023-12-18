import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())