import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))