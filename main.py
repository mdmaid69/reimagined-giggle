import glob
def find_files(pattern):
        return glob.glob(pattern)
import sys
def print_python_version():
        print(sys.version)