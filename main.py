import re
def split_string(pattern, string):
        return re.split(pattern, string)
import platform
def get_python_version():
        return platform.python_version()