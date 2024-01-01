import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])