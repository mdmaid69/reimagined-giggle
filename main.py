i = 0
while i < 5:
        print(i)
        i += 1
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)