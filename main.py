import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import os
def list_files_in_directory(path):
        return os.listdir(path)