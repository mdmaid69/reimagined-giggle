import getpass
def get_username():
        return getpass.getuser()
import os
def remove_directory(path):
        os.rmdir(path)