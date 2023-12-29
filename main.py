import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])