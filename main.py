import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)