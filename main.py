import sys
def add_to_python_path(path):
        sys.path.append(path)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)