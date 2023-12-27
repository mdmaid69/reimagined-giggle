text = "Hello, world!"
print("Words:", len(text.split()))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)