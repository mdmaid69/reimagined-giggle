import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()