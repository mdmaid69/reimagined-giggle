import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}