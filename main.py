import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import platform
def get_os_info():
        return platform.uname()