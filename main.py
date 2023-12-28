import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))