import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])