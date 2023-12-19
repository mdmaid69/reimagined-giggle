import os
def get_current_working_directory():
        return os.getcwd()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)