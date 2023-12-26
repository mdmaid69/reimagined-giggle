import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)