import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))