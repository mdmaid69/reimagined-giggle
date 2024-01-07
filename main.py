n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)