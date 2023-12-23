import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import os
def list_files_in_directory(path):
        return os.listdir(path)