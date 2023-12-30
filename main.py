import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)