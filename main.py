x = 10
y = 20
print("Sum:", x + y)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)