import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import platform
def get_os_info():
        return platform.uname()