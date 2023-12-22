import sys
def add_to_python_path(path):
        sys.path.append(path)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)