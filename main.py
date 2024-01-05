sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)