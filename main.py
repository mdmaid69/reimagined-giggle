import sys
def print_python_version():
        return sys.version
import glob
def find_files(pattern):
        return glob.glob(pattern)