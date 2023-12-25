import getpass
def get_username():
        return getpass.getuser()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)