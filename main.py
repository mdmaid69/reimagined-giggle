import platform
def get_python_version():
        return platform.python_version()
import os
def change_working_directory(path):
        os.chdir(path)