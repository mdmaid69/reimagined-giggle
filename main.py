import os
def get_current_working_directory():
        return os.getcwd()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))