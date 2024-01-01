import array
def get_list_from_array(array):
        return array.tolist()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())