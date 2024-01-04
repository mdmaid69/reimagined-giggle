import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)