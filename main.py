def greet(name):
        print(f"Hello, {name}!")
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)