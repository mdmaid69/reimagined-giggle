import time
def get_current_time():
        return time.ctime()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)