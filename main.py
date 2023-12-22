import glob
def find_files(pattern):
        return glob.glob(pattern)
import platform
def get_python_version():
        return platform.python_version()