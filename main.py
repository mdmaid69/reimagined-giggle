import array
def get_array_as_memoryview(array):
        return memoryview(array)
import time
def get_current_time():
        return time.ctime()