sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
def remove_duplicates(lst):
        return list(set(lst))