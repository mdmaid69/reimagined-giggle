import os
def remove_directory(path):
        os.rmdir(path)
import getpass
def get_username():
        return getpass.getuser()