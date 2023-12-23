import array
def get_array_typecode(array):
        return array.typecode
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())