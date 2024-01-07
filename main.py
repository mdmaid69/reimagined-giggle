sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import os
def change_working_directory(path):
        os.chdir(path)