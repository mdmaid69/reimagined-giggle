import getpass
def get_username():
        return getpass.getuser()
import os
def change_working_directory(path):
        os.chdir(path)