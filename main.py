for i in range(5):
        print(i)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)