import os
def change_working_directory(path):
        os.chdir(path)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)