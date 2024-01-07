import array
def get_bytes_from_array(array):
        return array.tobytes()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)