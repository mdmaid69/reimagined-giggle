import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import platform
def get_python_version():
        return platform.python_version()