import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import getpass
def get_username():
        return getpass.getuser()