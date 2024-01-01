import collections
def create_queue():
        return collections.deque()
import os
def list_files_in_directory(path):
        return os.listdir(path)