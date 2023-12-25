import array
def append_to_array(array, item):
        array.append(item)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())