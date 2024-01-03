import sys
def add_to_python_path(path):
        sys.path.append(path)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))