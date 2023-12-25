import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))