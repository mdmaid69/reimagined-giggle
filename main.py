import sys
def print_python_version():
        return sys.version
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)