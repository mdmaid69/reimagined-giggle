import array
def get_array_buffer_info(array):
        return array.buffer_info()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())