import time
def get_current_time():
        return time.ctime()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable