import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a