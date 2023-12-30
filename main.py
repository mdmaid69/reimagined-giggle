import shutil
def delete_directory(path):
        shutil.rmtree(path)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)