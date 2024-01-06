import platform
def get_python_version():
        return platform.python_version()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)