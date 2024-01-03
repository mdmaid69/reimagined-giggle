import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())