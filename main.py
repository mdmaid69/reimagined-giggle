import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)