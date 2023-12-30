import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)