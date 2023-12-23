import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()