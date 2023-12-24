import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import os
def get_environment_variable(var):
        return os.getenv(var)