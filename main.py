import platform
def get_os_info():
        return platform.uname()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)