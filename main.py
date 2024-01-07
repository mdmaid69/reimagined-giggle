import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import platform
def get_python_version():
        return platform.python_version()