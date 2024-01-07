import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import platform
def get_os_info():
        return platform.uname()