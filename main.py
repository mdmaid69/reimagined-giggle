sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))