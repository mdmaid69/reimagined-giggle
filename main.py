import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import platform
def get_python_version():
        return platform.python_version()