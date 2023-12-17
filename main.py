import getpass
def get_username():
        return getpass.getuser()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)