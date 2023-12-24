import collections
def create_user_dict():
        return collections.UserDict()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)