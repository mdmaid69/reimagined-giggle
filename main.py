import os
def remove_directory(path):
        os.rmdir(path)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)