import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import platform
def get_python_version():
        return platform.python_version()