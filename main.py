import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)