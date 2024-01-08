import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import sys
def add_to_python_path(path):
        sys.path.append(path)