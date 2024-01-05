import os
def list_files_in_directory(path):
        return os.listdir(path)
import platform
def get_os_info():
        return platform.uname()