import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))