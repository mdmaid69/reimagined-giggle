import os
def list_files_in_directory(path):
        return os.listdir(path)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))