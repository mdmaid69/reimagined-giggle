import time
def get_time_since_epoch():
        return time.time()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)