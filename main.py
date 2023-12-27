import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)