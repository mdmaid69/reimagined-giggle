import sys
def print_python_version():
        return sys.version
import shutil
def delete_directory(path):
        shutil.rmtree(path)