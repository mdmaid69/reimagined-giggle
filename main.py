import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import platform
def get_os_info():
        return platform.uname()