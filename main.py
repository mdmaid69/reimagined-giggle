import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import time
def get_time_since_epoch():
        return time.time()