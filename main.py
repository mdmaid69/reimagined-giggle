import platform
def get_os_info():
        return platform.uname()
import os
def remove_directory(path):
        os.rmdir(path)