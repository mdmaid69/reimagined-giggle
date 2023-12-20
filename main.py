import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)