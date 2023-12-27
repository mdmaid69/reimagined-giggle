n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)