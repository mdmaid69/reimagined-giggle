import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import platform
def get_os_info():
        return platform.uname()