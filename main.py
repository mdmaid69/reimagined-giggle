import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)