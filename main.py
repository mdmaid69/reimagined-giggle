import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))