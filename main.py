import os
def list_files_in_directory(path):
        return os.listdir(path)
import collections
def create_stack():
        return collections.deque()