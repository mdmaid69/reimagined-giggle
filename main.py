import shutil
def delete_directory(path):
        shutil.rmtree(path)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))