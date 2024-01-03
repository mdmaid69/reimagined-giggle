sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)