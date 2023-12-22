import collections
def create_queue():
        return collections.deque()
import os
def get_file_size(filename):
        return os.path.getsize(filename)