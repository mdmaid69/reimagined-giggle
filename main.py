import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import os
def list_files_in_directory(path):
        return os.listdir(path)