sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import os
def remove_directory(path):
        os.rmdir(path)