import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import sys
def print_python_version():
        print(sys.version)