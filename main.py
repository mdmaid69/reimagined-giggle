import collections
def create_user_list():
        return collections.UserList()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)