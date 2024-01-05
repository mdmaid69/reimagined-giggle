import time
def get_time_since_epoch():
        return time.time()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}