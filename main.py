import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)