import collections
def create_stack():
        return collections.deque()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)