import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)