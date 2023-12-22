import random
print(random.randint(0, 100))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)