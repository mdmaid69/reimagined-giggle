import sys
def add_to_python_path(path):
        sys.path.append(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)