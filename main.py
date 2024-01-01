import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def get_array_item_count(array, item):
        return array.count(item)