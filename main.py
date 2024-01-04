import sys
def add_to_python_path(path):
        sys.path.append(path)
import shutil
def delete_directory(path):
        shutil.rmtree(path)