import collections
def create_priority_queue():
        return collections.deque()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)