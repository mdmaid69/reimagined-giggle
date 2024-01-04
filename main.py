import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import os
def get_file_size(filename):
        return os.path.getsize(filename)