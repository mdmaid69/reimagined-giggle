import sys
def print_python_version():
        return sys.version
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)