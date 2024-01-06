def find_unique_words(sentence):
        return set(sentence.split())
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))