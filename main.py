import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def insert_into_array(array, i, item):
        array.insert(i, item)