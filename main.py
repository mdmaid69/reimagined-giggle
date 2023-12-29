import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)