import os
def list_files_in_directory(path):
        return os.listdir(path)
import getpass
def get_username():
        return getpass.getuser()