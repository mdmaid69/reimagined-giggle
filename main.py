import time
def get_current_time():
        return time.ctime()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)