n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)