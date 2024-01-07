import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)