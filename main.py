import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))