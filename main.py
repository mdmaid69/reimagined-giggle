import collections
def create_counter():
        return collections.Counter()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)