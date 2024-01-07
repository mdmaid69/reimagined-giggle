import os
def change_working_directory(path):
        os.chdir(path)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)