text = "Hello, world!"
print("Characters:", len(text))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)