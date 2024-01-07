import os
def get_environment_variable(var):
        return os.getenv(var)
import getpass
def get_username():
        return getpass.getuser()