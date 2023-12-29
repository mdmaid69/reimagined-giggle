import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import platform
def get_python_version():
        return platform.python_version()