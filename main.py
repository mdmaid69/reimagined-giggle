import os
def get_environment_variable(var):
        return os.getenv(var)
import sys
def add_to_python_path(path):
        sys.path.append(path)