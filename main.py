import os
def change_working_directory(path):
        os.chdir(path)
import getpass
def get_username():
        return getpass.getuser()