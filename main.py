import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))