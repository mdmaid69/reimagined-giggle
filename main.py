import getpass
def get_username():
        return getpass.getuser()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)