sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)