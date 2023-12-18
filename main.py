sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)