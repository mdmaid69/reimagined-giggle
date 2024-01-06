import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)