import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import os
def list_files_in_directory(path):
        return os.listdir(path)