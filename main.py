from collections import Counter
print(Counter("hello world"))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)