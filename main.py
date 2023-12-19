import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import sys
def add_to_python_path(path):
        sys.path.append(path)