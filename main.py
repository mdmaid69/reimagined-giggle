import platform
def get_os_info():
        return platform.uname()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)