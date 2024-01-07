import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import getpass
def get_username():
        return getpass.getuser()