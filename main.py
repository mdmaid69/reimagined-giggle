import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)