import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))