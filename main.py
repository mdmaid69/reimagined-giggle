import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)