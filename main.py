import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])