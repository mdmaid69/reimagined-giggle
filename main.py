import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)