import getpass
def get_username():
        return getpass.getuser()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)