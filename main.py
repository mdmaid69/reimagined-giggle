import platform
def get_os_info():
        return platform.uname()
import os
def change_working_directory(path):
        os.chdir(path)