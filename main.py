import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)