import platform
def get_os_info():
        return platform.uname()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)