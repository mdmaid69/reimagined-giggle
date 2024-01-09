import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array