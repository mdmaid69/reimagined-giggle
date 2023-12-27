import sys
def print_python_version():
        return sys.version
import shutil
def move_file(src, dst):
        shutil.move(src, dst)