import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import sys
def add_to_python_path(path):
        sys.path.append(path)