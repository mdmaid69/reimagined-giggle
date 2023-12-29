import os
def change_working_directory(path):
        os.chdir(path)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)