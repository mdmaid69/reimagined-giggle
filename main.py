import array
def get_array_itemsize(array):
        return array.itemsize
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())