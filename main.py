import platform
def get_os_info():
        return platform.uname()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)