import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))