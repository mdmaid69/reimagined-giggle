import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import getpass
def get_username():
        return getpass.getuser()