import platform
def get_os_info():
        return platform.uname()
import os
def get_environment_variable(var):
        return os.getenv(var)