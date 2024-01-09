import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)