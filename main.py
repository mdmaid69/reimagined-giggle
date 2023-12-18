numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)