import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)