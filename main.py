import time
def get_time_since_epoch():
        return time.time()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a