import platform
def get_os_info():
        return platform.uname()
import sys
def add_to_python_path(path):
        sys.path.append(path)