import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
n = 10
print("Square numbers:", [x**2 for x in range(n)])