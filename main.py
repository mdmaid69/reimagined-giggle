import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)