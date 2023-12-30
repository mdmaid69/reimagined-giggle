import glob
def find_files(pattern):
        return glob.glob(pattern)
import sys
def add_to_python_path(path):
        sys.path.append(path)