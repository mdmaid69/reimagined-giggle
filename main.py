import collections
def create_user_list():
        return collections.UserList()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)