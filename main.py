import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))