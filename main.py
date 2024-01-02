import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
def split_string(pattern, string):
        return re.split(pattern, string)