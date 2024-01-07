def count_characters(sentence):
        return len(sentence)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))