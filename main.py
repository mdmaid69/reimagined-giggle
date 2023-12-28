import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))