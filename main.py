import platform
def get_python_version():
        return platform.python_version()
import os
def remove_directory(path):
        os.rmdir(path)