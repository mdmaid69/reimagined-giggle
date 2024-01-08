sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)