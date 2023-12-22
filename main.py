import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))