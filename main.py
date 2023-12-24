import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import os
def remove_directory(path):
        os.rmdir(path)