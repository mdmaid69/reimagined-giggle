import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import glob
def find_files(pattern):
        return glob.glob(pattern)