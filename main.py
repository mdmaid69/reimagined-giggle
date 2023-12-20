import collections
def create_counter():
        return collections.Counter()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)