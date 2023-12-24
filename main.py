import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import os
def remove_directory(path):
        os.rmdir(path)