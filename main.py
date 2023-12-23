import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()