import time
print(time.time())
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)