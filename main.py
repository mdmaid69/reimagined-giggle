def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a