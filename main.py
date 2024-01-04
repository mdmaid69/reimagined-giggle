import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)