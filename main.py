import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)