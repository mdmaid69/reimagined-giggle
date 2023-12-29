import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
from collections import Counter
print(Counter("hello world"))