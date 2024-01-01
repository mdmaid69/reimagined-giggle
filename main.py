import collections
def create_queue():
        return collections.deque()
import os
def remove_directory(path):
        os.rmdir(path)