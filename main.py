import platform
def get_os_info():
        return platform.uname()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)