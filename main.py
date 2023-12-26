import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import os
def get_environment_variable(var):
        return os.getenv(var)