import os
def remove_directory(path):
        os.rmdir(path)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)