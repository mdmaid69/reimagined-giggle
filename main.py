import getpass
def get_username():
        return getpass.getuser()
import os
def get_file_size(filename):
        return os.path.getsize(filename)