import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import sys
def add_to_python_path(path):
        sys.path.append(path)