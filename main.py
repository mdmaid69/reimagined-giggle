import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import platform
def get_python_version():
        return platform.python_version()