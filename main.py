import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import getpass
def get_username():
        return getpass.getuser()