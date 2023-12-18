import sys
def add_to_python_path(path):
        sys.path.append(path)
import getpass
def get_username():
        return getpass.getuser()