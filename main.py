import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)