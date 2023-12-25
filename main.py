import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)