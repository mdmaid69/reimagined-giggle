import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import time
def get_current_time():
        return time.time()