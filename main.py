import os
def get_file_size(filename):
        return os.path.getsize(filename)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)