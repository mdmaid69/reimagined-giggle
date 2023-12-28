import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)