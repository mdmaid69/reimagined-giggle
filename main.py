import datetime
def get_current_datetime():
        return datetime.datetime.now()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)