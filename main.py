def count_words(sentence):
        return len(sentence.split())
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))