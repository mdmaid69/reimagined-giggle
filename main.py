import platform
def get_os_info():
        return platform.uname()
import re
def split_string(pattern, string):
        return re.split(pattern, string)