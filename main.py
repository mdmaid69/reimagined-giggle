n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)