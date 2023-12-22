import os
def get_file_size(filename):
        return os.path.getsize(filename)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)