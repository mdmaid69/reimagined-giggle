import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()