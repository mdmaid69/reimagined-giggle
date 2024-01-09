import platform
def get_python_version():
        return platform.python_version()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)