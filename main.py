import os
def get_file_size(filename):
        return os.path.getsize(filename)
import platform
def get_os_info():
        return platform.uname()