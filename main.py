import array
def get_array_slice(array, i, j):
        return array[i:j]
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())