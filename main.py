import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)