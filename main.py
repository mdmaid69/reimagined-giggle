import os
def remove_directory(path):
        os.rmdir(path)
import collections
def create_stack():
        return collections.deque()