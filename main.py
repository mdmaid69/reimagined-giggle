import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import platform
def get_python_version():
        return platform.python_version()