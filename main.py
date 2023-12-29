import platform
def get_python_version():
        return platform.python_version()
import os
def list_files_in_directory(path):
        return os.listdir(path)