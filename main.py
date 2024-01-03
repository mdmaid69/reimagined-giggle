import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)