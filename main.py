sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)