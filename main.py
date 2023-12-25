import os
def get_file_size(filename):
        return os.path.getsize(filename)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))