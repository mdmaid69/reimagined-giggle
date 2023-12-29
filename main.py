import array
def get_array_as_bytearray(array):
        return bytearray(array)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())