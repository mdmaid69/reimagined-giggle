import sys
def add_to_python_path(path):
        sys.path.append(path)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)