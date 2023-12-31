import collections
def create_counter():
        return collections.Counter()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)