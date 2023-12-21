import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)