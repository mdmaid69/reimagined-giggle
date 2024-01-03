import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())