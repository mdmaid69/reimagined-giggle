import os
def change_working_directory(path):
        os.chdir(path)
import collections
def create_queue():
        return collections.deque()