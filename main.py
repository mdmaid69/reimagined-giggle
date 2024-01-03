import getpass
def get_username():
        return getpass.getuser()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)