import array
def get_array_as_complex(array):
        return complex(array[0])
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())