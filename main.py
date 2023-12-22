import getpass
def get_username():
        return getpass.getuser()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)