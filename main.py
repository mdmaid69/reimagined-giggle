import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def sort_numbers(numbers):
        return sorted(numbers)