import collections
def create_priority_queue():
        return collections.deque()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)