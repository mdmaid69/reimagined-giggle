import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import collections
def create_user_string():
        return collections.UserString()