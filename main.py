import getpass
def get_username():
        return getpass.getuser()
import platform
def get_os_info():
        return platform.uname()