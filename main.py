import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)