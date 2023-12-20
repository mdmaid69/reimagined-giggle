sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
import glob
def find_files(pattern):
        return glob.glob(pattern)