import array
def get_array_index(array, item):
        return array.index(item)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())