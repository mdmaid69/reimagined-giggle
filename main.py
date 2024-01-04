import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)