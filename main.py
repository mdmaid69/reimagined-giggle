import sys
def add_to_python_path(path):
        sys.path.append(path)
import platform
def get_python_version():
        return platform.python_version()