import glob
def find_files(pattern):
        return glob.glob(pattern)
from collections import Counter
print(Counter("hello world"))