import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
from collections import Counter
print(Counter("hello world"))