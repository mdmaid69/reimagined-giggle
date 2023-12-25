import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import os
def remove_directory(path):
        os.rmdir(path)