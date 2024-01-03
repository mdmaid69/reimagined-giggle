import platform
def get_python_version():
        return platform.python_version()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)