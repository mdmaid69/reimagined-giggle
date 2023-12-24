import getpass
def get_username():
        return getpass.getuser()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)